#!/usr/bin/env python
from time import sleep
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

try:
        id, text = reader.read()
        print(id)
        print(text)
        sleep(5)

finally:
        GPIO.cleanup()