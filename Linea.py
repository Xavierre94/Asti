import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
lineLeft1=40
lineRight1=38
lineLeft2=36
lineRight2=37
center=35
GPIO.setup(38, GPIO.IN)
GPIO.setup(40, GPIO.IN)
GPIO.setup(36, GPIO.IN)
GPIO.setup(37, GPIO.IN)
GPIO.setup(35, GPIO.IN)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(21, GPIO.OUT)
speed=8.5
p = GPIO.PWM(33, 50)  
p.start(7.5)

q = GPIO.PWM(31, 50) 
q.start(7.5)
def forward()
   
def irLeftLine1():
    if GPIO.input(lineLeft1)==0:
        return True
    else:
        return False
    

def irRightLine1():
    if GPIO.input(lineRight1)==0:
        return True
    else:
        return False
def irLeftLine2():
    if GPIO.input(lineLeft2)==0:
        return True
    else:
        return False
def irRightLine1():
    if GPIO.input(lineRight2)==0:
        return True
    else:
        return False
def irRightLine2():
    if GPIO.input(lineRight2)==0:
        return True
    else:
        return False
def center():
    if GPIO.input(lineRight2)==0:
        return True
    else:
        return False  
try:
    raw_input("Press Enter")
    p.ChangeDutyCycle(speed)
    q.ChangeDutyCycle (speed)
    while True:
        izq1=irRightLine1()
        izq2=irLeftLine2()
        drcha1=irRightLine1()
        drcha2=irRightLine2()
        ctro=center()
        if (center==True and drcha1== False and izda1 == False)
             speedr=speedr+0.1
             speedl=speedl+0.1
             if speedr > 10
                 speedr = 10
             if speedl > 10
                 speedl = 10
        elif (center == True and izda1 ==True )
            speedr=speedr+0.1
             speedl=speedl-0.1
             if speedr > 10
                 speedr = 10
             if speedl < 0
                 speedl = 0
        elif (center == True and drcha1 ==True )
            speedr=speedr-0.1
            speedl=speedl+0.1
             if speedr < 0
                 speedr = 0
             if speedl > 10
                 speedl = 10
        elif (drcha1 == True or drcha 2 == True)
            speedr=speedr-0.2
            speedl=speedl+0.2
             if speedr < 0
                 speedr = 0
             if speedl > 10
                 speedl = 10 
        elif (izda1 == True or izda2 == True)
            speedr=speedr+0.2
            speedl=speedl-0.2
             if speedl < 0
                 speedl = 0
             if speedr > 10
                 speedr = 10 
        else
            speedr=speedr+0.2
            speedl=speedl-0.2
             if speedl < 0
                 speedl = 0
             if speedr > 10
                 speedr = 10 turnall()

        p.ChangeDutyCycle(speedr)
        q.ChangeDutyCycle (speedl)
except KeyboardInterrupt:
    p.stop()
    GPIO.cleanup()    
