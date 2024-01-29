#!/usr/bin/env python
from time import sleep
from mfrc522 import SimpleMFRC522
import requests
import json
from datetime import datetime, time, timedelta
import wiringpi
import spidev
from ch7_ClassLCD import LCD
import recognize
import os
import mail

reader = SimpleMFRC522()
print("reading")

try:
    while True:
        print("Hold a tag near the reader")

        uid, text = reader.read()
        sleep(0.5)
        print(uid)

        response = requests.get(f'https://api.nas64.be/student/{uid}')
        student = response.json()
        student_id = student["id"]
        student_naam = student["naam"]
        r_nummer = student["r_nummer"]
        print(student_naam)


        incheck_response = requests.get(f'https://api.nas64.be/incheck/{student_id}')
        uitcheck_response = requests.get(f'https://api.nas64.be/uitcheck/{student_id}')

        huidige_tijd = datetime.now().time()
        upload_tijd = huidige_tijd.strftime("%H:%M:%S")

        examen_response = requests.get(f'https://api.nas64.be/examen/1')
        examen = examen_response.json()
        examen_naam = examen["naam"]
        examen_start = examen["startuur"]
        time_format = "%H:%M"
        minimale_tijd = datetime.strptime("00:30", time_format)
        start = datetime.strptime(examen_start, time_format)
        minimal = start + timedelta(minutes=minimale_tijd.minute, hours=minimale_tijd.hour)
        starttijd = start.time()
        min = minimal.time()
        #naam = recognize.capture_and_recognize()
        naam = "Anthony Van Roy"

        inschrijving_response = requests.get(f'https://api.nas64.be/inschrijving/{student_id}/1')

        if student_naam == naam:

            if inschrijving_response.status_code == 200:
                print("You are registred for this exam!")

                if starttijd > huidige_tijd:
                    print("exam hasnt started yet!")

                elif starttijd < huidige_tijd < min and incheck_response.status_code == 404:
                    post_incheck = requests.post(f'https://api.nas64.be/incheck/', json={"incheck": upload_tijd, "student_id": student_id, "examen_id": 1})
                    print("post incheck: " + str(post_incheck))
                    #mail.incheck(r_nummer, examen_naam, upload_tijd)
                    responses = requests.get(f'https://api.nas64.be/incheck/{student_id}')
                    incheck = responses.json()
                    print("normale incheck: " + str(incheck))

                elif starttijd < huidige_tijd < min and incheck_response.status_code == 200:
                    print("You cant end your exam yet")

                elif huidige_tijd > min and incheck_response.status_code == 200 and uitcheck_response.status_code == 404:
                    post_uitcheck = requests.post(f'https://api.nas64.be/uitcheck/', json={"uitcheck": upload_tijd, "student_id": student_id, "examen_id": 1})
                    print(post_uitcheck)
                    #mail.uitcheck(r_nummer, examen_naam, upload_tijd)
                    responses = requests.get(f'https://api.nas64.be/uitcheck/{student_id}')
                    uitcheck = responses.json()
                    print("print uitcheck: " + str(uitcheck))

                elif uitcheck_response.status_code == 200:
                    print("You already ended your exam")

                else:
                    print("Exam has already started!")

            else:
                print("You are not registered for this exam!")

        else:
            print("You aren't the owner of the card!")

        #os.remove("captured_image.jpg")
        sleep(5)

except KeyboardInterrupt:
    print("\nProgram terminated")

