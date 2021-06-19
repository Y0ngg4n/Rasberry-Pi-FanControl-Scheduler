import time
import RPi.GPIO as GPIO

def turn_off():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(4, GPIO.OUT)
    time.sleep(0.5)
    GPIO.output(4, GPIO.LOW)
    time.sleep(0.5)
    GPIO.setup(6, GPIO.OUT)
    time.sleep(0.5)
    GPIO.output(6, GPIO.LOW)


if __name__ == '__main__':
    turn_off()