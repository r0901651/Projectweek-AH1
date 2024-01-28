#!/usr/bin/env python
from time import sleep
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import requests
import json
import recognize
import cv2
from datetime import datetime, time
reader = SimpleMFRC522()
print("reading")
while True:
    id, text = reader.read()
    sleep(0.5)
    print(id)
    response = requests.get(f'http://100.65.2.33:8000/student/{id}')
    student = response.json()
    student_id = student["id"]
    student_naam = student["naam"]
    print(student_naam)
    incheck_response = requests.get(f'http://100.65.2.33:8000/incheck/{student_id}')
    uitcheck_response = requests.get(f'http://100.65.2.33:8000/uitcheck/{student_id}')
    huidige_tijd = datetime.now().time()
    upload_tijd = huidige_tijd.strftime("%H:%M:%S")
    start = time(13, 15)
    minimal = time(13, 45)
    naam = recognize.capture_and_recognize()
    print(naam)
    if student_naam == naam:
        if start > huidige_tijd:
            print("exam hasnt started yet")
        elif start < huidige_tijd < minimal and incheck_response.status_code == 404:
            post_incheck = requests.post(f'http://100.65.2.33:8000/incheck/', json={"incheck": upload_tijd, "student_id": student_id})
            print(post_incheck)
            responses = requests.get(f'http://100.65.2.33:8000/incheck/{student_id}')
            incheck = responses.json()
            print(incheck)
        elif start < huidige_tijd < minimal and incheck_response.status_code == 200:
            print("You cant end your exam yet")
        elif huidige_tijd > minimal and incheck_response.status_code == 200 and uitcheck_response.status_code == 404:
            post_uitcheck = requests.post(f'http://100.65.2.33:8000/uitcheck/', json={"uitcheck": upload_tijd, "student_id": student_id})
            print(post_uitcheck)
            responses = requests.get(f'http://100.65.2.33:8000/uitcheck/{student_id}')
            uitcheck = responses.json()
            print(uitcheck)
        elif huidige_tijd > minimal and incheck_response.status_code == 200 and uitcheck_response.status_code == 200:
            print("You already submitted your exam")
        else:
            print("Exam has already started")
    else:
        print("You aren't the owner of the card!")