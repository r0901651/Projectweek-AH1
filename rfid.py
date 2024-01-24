from time import sleep
import sys
from mfrc522 import SimpleMFRC522
reader = SimpleMFRC522()

try:
    while True:
        print("Hold a tag near the reader")
        id, _ = reader.read()
        print("ID: %s" % (id))
        sleep(5)
except KeyboardInterrupt:
    GPIO.cleanup()
    raise