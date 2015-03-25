import RPi.GPIO as GPIO
import time
import random

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

led1 = 23
led2 = 24

GPIO.setup(led1,GPIO.OUT)
GPIO.setup(led2,GPIO.OUT)

while True:
	GPIO.output(led2,0)
	GPIO.output(led1,1)
	print("led 1 blinking")
	time.sleep(1)
	GPIO.output(led1,0)
	GPIO.output(led2,1)
	print("led2 blinking")
	time.sleep(1)

GPIO.cleanup()