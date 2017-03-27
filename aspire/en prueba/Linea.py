import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
lineLeft=40
lineRight=38
GPIO.setup(38, GPIO.IN)
GPIO.setup(40, GPIO.IN)
def irLeftLine():
    if GPIO.input(lineLeft)==0:
        return True
    else:
        return False
    
# irRightLine(): Returns state of Right IR Line sensor
def irRightLine():
    if GPIO.input(lineRight)==0:
        return True
    else:
        return False
try:
    while True:
        izq=irLeftLine()
        drcha=irRightLine()
        if izq== drcha
            forward()
        elif izq = True
        print izq
        print drcha
except KeyboardInterrupt:
    p.stop()
    GPIO.cleanup()    
