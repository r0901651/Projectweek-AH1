from time import sleep
import sys
from mfrc522 import SimpleMFRC522
import time
import wiringpi
import spidev
from ch7_ClassLCD import LCD

reader = SimpleMFRC522()
def ActivateLCD():
    wiringpi.digitalWrite(pin_CS_lcd, 0)       # Actived LCD using CS
    time.sleep(0.000005)

def DeactivateLCD():
    wiringpi.digitalWrite(pin_CS_lcd, 1)       # Deactived LCD using CS
    time.sleep(0.000005)

PIN_OUT     =   {  
                'SCLK'  :   14,
                'DIN'   :   11,
                'DC'    :   9, 
                'CS'    :   13, #We will not connect this pin! --> we use w13
                'RST'   :   10,
                'LED'   :   6, #backlight   
}

#IN THIS CODE WE USE W13 (PIN 22) AS CHIP SELECT
pin_CS_lcd = 13
wiringpi.wiringPiSetup() 
wiringpi.wiringPiSPISetupMode(1, 0, 400000, 0)  #(channel, port, speed, mode)
wiringpi.pinMode(pin_CS_lcd , 1)                # Set pin to mode 1 ( OUTPUT )
ActivateLCD()
lcd_1 = LCD(PIN_OUT)

try:
    lcd_1.clear()
    lcd_1.set_backlight(1)
    while True:
        ActivateLCD()
        lcd_1.clear()
        lcd_1.go_to_xy(0, 0)
        lcd_1.put_string('Hold a tag near the reader')
        lcd_1.refresh()
        print("Hold a tag near the reader")
        id, _ = reader.read()
        print("ID: %s" % (id))
        lcd_1.clear()
        lcd_1.go_to_xy(0, 0)
        lcd_1.put_string('id:\n'+ id + '\ningecheckt: \ndone \n'+time.strftime("%H:%M:%S"))
        lcd_1.refresh()
        DeactivateLCD()
        sleep(5)
except KeyboardInterrupt:
    GPIO.cleanup()
    raise