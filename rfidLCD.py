from time import sleep
import sys
from mfrc522 import SimpleMFRC522
import time
import wiringpi
import spidev
from ch7_ClassLCD import LCD
import Adafruit_Nokia_LCD as LCD
import Adafruit_GPIO.SPI as SPI

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


reader = SimpleMFRC522()

# Raspberry Pi hardware SPI config:
DC = 23
RST = 24
SPI_PORT = 0
SPI_DEVICE = 0


# Hardware SPI usage:
disp = LCD.PCD8544(DC, RST, spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE, max_speed_hz=4000000))

# Software SPI usage (defaults to bit-bang SPI interface):
#disp = LCD.PCD8544(DC, RST, SCLK, DIN, CS)

# Initialize library.
disp.begin(contrast=60)

# Clear display.
disp.clear()
disp.display()

# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
image = Image.new('1', (LCD.LCDWIDTH, LCD.LCDHEIGHT))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Load default font.
font = ImageFont.load_default()

# Write some text.
draw.text((8,30), 'Hello World!', font=font)

try:
    # Clear display.
    disp.clear()
    disp.display()
    while True:
        disp.clear()
        draw.text((8,30), 'Hold card against reader', font=font)
        print("Hold a tag near the reader")
        id, _ = reader.read()
        print("ID: %s" % (id))
        disp.clear()
        disp.display()
        draw.text((8,30), 'id: '+str(id), font=font)
        sleep(5)
except KeyboardInterrupt:
    GPIO.cleanup()
    raise