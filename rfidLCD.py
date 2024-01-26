import time
import wiringpi
import spidev
from ch7_ClassLCD import LCD
from mfrc522 import SimpleMFRC522
reader = SimpleMFRC522()


def ActivateLCD():
    wiringpi.digitalWrite(pin_CS_lcd, 0)       # Actived LCD using CS
    time.sleep(0.000005)

def DeactivateLCD():
    wiringpi.digitalWrite(pin_CS_lcd, 1)       # Deactived LCD using CS
    time.sleep(0.000005)

PIN_OUT     =   {  
                'SCLK'  :   14,
                'DIN'   :   12,
                'DC'    :   11, 
                'CS'    :   3, #We will not connect this pin! --> we use w13
                'RST'   :   15,
                'LED'   :   31, #backlight   
}

#IN THIS CODE WE USE W13 (PIN 22) AS CHIP SELECT
pin_CS_lcd = 18
wiringpi.wiringPiSetup() 
wiringpi.wiringPiSPISetupMode(1, 0, 400000)  #(channel, port, speed, mode)
wiringpi.pinMode(pin_CS_lcd , 1)                # Set pin to mode 1 ( OUTPUT )
ActivateLCD()
lcd_1 = LCD(PIN_OUT)
wiringpi.wiringPiSPISetupMode (1,0,500000)

try:
    lcd_1.clear()
    lcd_1.set_backlight(1)
    while True:
        print("Hold a tag near the reader")
        id, _ = reader.read()
        print("ID: %s" % (id))
        ActivateLCD()
        lcd_1.clear()
        lcd_1.go_to_xy(0, 0)
        lcd_1.put_string('Thanks for checking in \nid display \nid = ' + str(id)) #display the text
        lcd_1.refresh()
        DeactivateLCD()
        time.sleep(3)

except KeyboardInterrupt:
    lcd_1.clear()
    lcd_1.refresh()
    lcd_1.set_backlight(0)
    DeactivateLCD()
    print("\nProgram terminated")

# End of Program