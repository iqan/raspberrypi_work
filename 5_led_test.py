import RPi.GPIO as GPIO
import time
import random

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

led5 = 5
led4 = 6
led3 = 13
led2 = 19
led1 = 26


GPIO.setup(led1,GPIO.OUT)
GPIO.setup(led2,GPIO.OUT)
GPIO.setup(led3,GPIO.OUT)
GPIO.setup(led4,GPIO.OUT)
GPIO.setup(led5,GPIO.OUT)


while True:
	GPIO.output(led5,1)
	GPIO.output(led4,1)
	GPIO.output(led3,1)
	GPIO.output(led2,1)
	GPIO.output(led1,0)
	print("led 1 blinking")
	time.sleep(1)
	
	GPIO.output(led5,1)
	GPIO.output(led4,1)
	GPIO.output(led3,1)
	GPIO.output(led2,0)
	GPIO.output(led1,1)
	print("led 2 blinking")
	time.sleep(1)

	GPIO.output(led5,1)
	GPIO.output(led4,1)
	GPIO.output(led3,0)
	GPIO.output(led2,1)
	GPIO.output(led1,1)
	print("led 3 blinking")
	time.sleep(1)

	GPIO.output(led5,1)
	GPIO.output(led4,0)
	GPIO.output(led3,1)
	GPIO.output(led2,1)
	GPIO.output(led1,1)
	print("led 4 blinking")
	time.sleep(1)

	GPIO.output(led5,0)
	GPIO.output(led4,1)
	GPIO.output(led3,1)
	GPIO.output(led2,1)
	GPIO.output(led1,1)
	print("led 5 blinking")
	time.sleep(1)

GPIO.cleanup()