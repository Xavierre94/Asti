import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(21, GPIO.OUT)

p = GPIO.PWM(21, 50)  # channel=12 frequency=50Hz
p.start(7.5)
try:
    while 1:
            p.ChangeDutyCycle(10)
            time.sleep(1)
except KeyboardInterrupt:
    p.stop()
    GPIO.cleanup()
