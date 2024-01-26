#!/usr/bin/env python
from time import sleep
from mfrc522 import SimpleMFRC522
import requests
import json
from datetime import datetime, time
import wiringpi
import spidev
from ch7_ClassLCD import LCD
import recognize
import os

reader = SimpleMFRC522()
print("reading")

def ActivateLCD():
    wiringpi.digitalWrite(pin_CS_lcd, 0)       # Actived LCD using CS
    sleep(0.000005)

def DeactivateLCD():
    wiringpi.digitalWrite(pin_CS_lcd, 1)       # Deactived LCD using CS
    sleep(0.000005)

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
        id, text = reader.read()
        sleep(0.5)
        print(id)
        response = requests.get(f'http://100.65.2.33:8000/student/{id}')
        student = response.json()
        student_id = student["id"]
        student_naam = student["naam"]
        print(student_naam)
        lcd_1.clear()
        lcd_1.go_to_xy(0, 0)
        lcd_1.put_string('Thanks for scanning \nName on display:\n' + student_naam) #display the text
        lcd_1.refresh()
        sleep(2)
        incheck_response = requests.get(f'http://100.65.2.33:8000/incheck/{student_id}')
        huidige_tijd = datetime.now().time()
        upload_tijd = huidige_tijd.strftime("%H:%M:%S")
        start = time(12, 45)
        minimal = time(13, 0)
        naam = recognize.capture_and_recognize()
        if student_naam == naam:
            lcd_1.clear()
            lcd_1.go_to_xy(0, 0)
            lcd_1.put_string('Facia\nrecognition\nCompleted' + naam) #display the text
            lcd_1.refresh()
            if start > huidige_tijd:
                lcd_1.clear()
                lcd_1.go_to_xy(0, 0)
                lcd_1.put_string('Error \nexam hasnt started yet' + student["naam"]) #display the text
                lcd_1.refresh()
                print("exam hasnt started yet")
            elif start < huidige_tijd < minimal and incheck_response.status_code == 404:
                post_incheck = requests.post(f'http://100.65.2.33:8000/incheck/', json={"incheck": upload_tijd, "student_id": student_id})
                print("post incheck: " + str(post_incheck))
                lcd_1.clear()
                lcd_1.go_to_xy(0, 0)
                lcd_1.put_string('\npostincheck:' + str(post_incheck)) #display the text
                lcd_1.refresh()
                responses = requests.get(f'http://100.65.2.33:8000/incheck/{student_id}')
                incheck = responses.json()
                print("normale incheck: " + str(incheck))
                lcd_1.clear()
                lcd_1.go_to_xy(0, 0)
                lcd_1.put_string('\npostincheck:' + str(incheck)) #display the text
                lcd_1.refresh()
            elif start < huidige_tijd < minimal and incheck_response.status_code == 200:
                print("You cant end your exam yet")
                lcd_1.clear()
                lcd_1.go_to_xy(0, 0)
                lcd_1.put_string("You can't end your exam just yet " + student["naam"]) #display the text
                lcd_1.refresh()
            elif huidige_tijd > minimal and incheck_response.status_code == 200:
                post_uitcheck = requests.post(f'http://100.65.2.33:8000/uitcheck/', json={"uitcheck": upload_tijd, "student_id": student_id})
                print(post_uitcheck)
                responses = requests.get(f'http://100.65.2.33:8000/uitcheck/{student_id}')
                uitcheck = responses.json()
                print("print uitcheck: " + str(uitcheck))
                lcd_1.clear()
                lcd_1.go_to_xy(0, 0)
                lcd_1.put_string("uitcheck" + str(uitcheck)) #display the text
                lcd_1.refresh()
            else:
                print("Exam has already started")
                lcd_1.clear()
                lcd_1.go_to_xy(0, 0)
                lcd_1.put_string("Exam has already started" ) #display the text
                lcd_1.refresh()
        else:
            print("You aren't the owner of the card!")
            lcd_1.clear()
            lcd_1.go_to_xy(0, 0)
            lcd_1.put_string("You aren't the owner of the card!" )
            lcd_1.refresh()
        os.remove("captured_image.jpg") 
        sleep(5)

except KeyboardInterrupt:
    lcd_1.clear()
    lcd_1.refresh()
    lcd_1.set_backlight(0)
    DeactivateLCD()
    print("\nProgram terminated")

