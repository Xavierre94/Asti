from __future__ import division
import RPi.GPIO as GPIO, time
import Adafruit_PCA9685

#initialize PCA9685 module
pwm = Adafruit_PCA9685.PCA9685()
# Motor Pins definition
#Motor Left
L1=11
L2=10
EL=36
#motor right
R1=9
R2=8
ER=38
#steering servo
pwmMax=4095 #maximum pwm value
#Ultrasonic sensor (definir aqui los pines de entrada y salida de US)
##RCT=
##RCE=
##LCT=
##LCE=
##LST=
##LSE=
#Function definiton
#initailisae pins and switch motors off
def init():
    #default adress for PCA9685
    pwm.set_pwm_freq (60) 
    #physical numbering of GPIO pins
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(EL,GPIO.OUT)
    GPIO.setup(ER,GPIO.OUT)
    #configuration of pins ultrasonic sensors
##    GPIO.setup(RCT,GPIO.OUT)
##    GPIO.setup(LCT,GPIO.OUT)
##    GPIO.setup(RCE,GPIO.IN)
##    GPIO.setup(LCE,GPIO.IN)
    #enable motors
    
        
def enableMotors():
    GPIO.output (EL,True)
    GPIO.output (ER,True)
    
    #clean sets all motors off and sets GPIo standar values
def cleanup():
    stop()
    #stopServos()
    time.sleep(1)
    GPIO.cleanup()
    
    #Motor Functions
def stop():
    pwm.set_pwm(L1,0,pwmMax)
    pwm.set_pwm(L2,0,pwmMax)
    pwm.set_pwm(R1,0,pwmMax)
    pwm.set_pwm(R2,0,pwmMax)
    
def forward(speed):
    duty= int(speed/100)
    high=int(duty*pwmMax)
    low=int((1-duty)*pwmMax)
    pwm.set_pwm(L1,high,low)
    pwm.set_pwm(L2,0,pwmMax)
    pwm.set_pwm(R1,high,low)
    pwm.set_pwm(R2,0,pwmMax)
    freq=speed+5
    pwm.set_pwm_freq(freq)
    
    
#Steering servo
def turnRight(angle):
    duty = float(angle) / 10.0 + 2.5
    high = int(duty*pwmMax)
    low= int (pwmMax*(1-duty))
    pwm.set_pwm(0,high,low)
    
def turnLeft(angle):
    duty = float(angle) / 10.0 + 2.5
    high = int(1-duty)*pwmMax
    low= int(pwmMax*duty)
    pwm.set_pwm(0,high,low)
#ultrasonic sensors functions
##def getDistanceRight():
##    GPIO.output (RCT,True) 
##        time.sleep (0.00001)            
##        GPIO.output (RCT, False) 
##        start= time.time()                
##        while GPIO.input (RCE) == 0: 
##            start =time.time()             
##        while GPIO.input (RCE) == 1: 
##            stop =time.time()              
##        t_trans= stop-start                
##        distancia = (t_trans*34300)/2
##        #print distancia
##        time.sleep(1)
##        return distancia
##def getDistanceLeft():
##        GPIO.output (LCT,True) 
##        time.sleep (0.00001)            
##        GPIO.output (LCT, False) 
##        start= time.time()                
##        while GPIO.input (lCE) == 0: 
##            start =time.time()             
##        while GPIO.input (LCE) == 1: 
##            stop =time.time()              
##        t_trans= stop-start                
##        distancia = (t_trans*34300)/2
##        #print distancia
##        time.sleep(1)
##        return distancia
##def getDistanceSide():
##        GPIO.output (LST,True) 
##        time.sleep (0.00001)            
##        GPIO.output (LST, False) 
##        start= time.time()                
##        while GPIO.input (LSE) == 0: 
##            start =time.time()             
##        while GPIO.input (LSEE) == 1: 
##            stop =time.time()              
##        t_trans= stop-start                
##        distancia = (t_trans*34300)/2
##        #print distancia
##        time.sleep(1)
##        return distancia
    
    
