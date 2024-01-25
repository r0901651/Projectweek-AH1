#!/usr/bin/env python
from time import sleep
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import requests
import json
from datetime import datetime, time
reader = SimpleMFRC522()
startijd = time(14, 0)
minimal = time(14, 30)
try:
    while True:
        id, text = reader.read()
        print(id)
        response = requests.get(f'http://100.66.184.34:8000/student/{id}')
        print(response)
        student = response.json()
        print(student)
        id = student['id']
        incheck_response = requests.get(f'http://100.66.184.34:8000/incheck/{id}')
        incheck = incheck_response.json()
        inchecktijd = incheck["incheck"]
        huidige_tijd = datetime.now().strftime('%H:%M')
        if huidige_tijd < startijd:
            print("Exam not started")
        elif startijd < huidige_tijd < minimal and inchecktijd is None:
            requests.post(f'http://100.66.184.34:8000/incheck/', json={"incheck": huidige_tijd, "student_id": id})
        elif huidige_tijd > minimal:
            requests.post(f'http://100.66.184.34:8000/uitcheck/', json={"uicheck": huidige_tijd, "student_id": id})
        sleep(3)
finally:
        GPIO.cleanup()
