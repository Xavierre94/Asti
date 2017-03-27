# -*- coding: utf-8 -*-
import servos, time, math
import RPi.GPIO as GPIO
import Adafruit_PCA9685
import struct

import sys

GPIO.setwarnings(False)
GPIO.setmode (GPIO.BOARD) 
#inicializar puertos y PCA9685
pwm = Adafruit_PCA9685.PCA9685()
#motor pins
Enable1=36
Enable2=38
GPIO.setup(Enable1,GPIO.OUT)
GPIO.setup(Enable2,GPIO.OUT)
pwmMax=4095
pwm.set_pwm_freq (60)
pwm.set_pwm(0,0,pwmMax) 
global speed
speed=40
global vmax
vmax = 70
global q1ant
global q2ant
global q3ant
global q4ant
q1ant=0.0
q2ant=90.0
q3ant=0.0
q4ant=0.0
global q1
global q2
global q3
global q4
q1=0.0
q2=0.0
q3=0.0
q4=0.0
#Cambiar al probar
#Ultrasonic sensor (definir aqui los pines de entrada y salida de US)
RCT=40
RCE=37
LEDROJO=35
##LCT=
##LCE=
##LST=
##LSE=
L1=1
L2=1
L3=1
L4=1

servos.init()
GPIO.setup(RCT,GPIO.OUT)
GPIO.setup(RCE,GPIO.IN)
GPIO.setup(LEDROJO,GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
p = GPIO.PWM(12, 20)
p.start(0)

GPIO.setup(11, GPIO.OUT)
q = GPIO.PWM(11, 20)
q.start(0)

GPIO.setup(15, GPIO.OUT)
a = GPIO.PWM(15, 20)
a.start(0)

GPIO.setup(13, GPIO.OUT)
b = GPIO.PWM(13, 20)
b.start(0)
def getDistanceRight():
    GPIO.output (RCT,True)
    time.sleep (0.00001)
    GPIO.output (RCT, False)
    start= time.time()
    while GPIO.input (RCE) == 0:
        start =time.time()
    while GPIO.input (RCE) == 1:
        stop =time.time()
    t_trans= stop-start
    distancia = (t_trans*34300)/2
    time.sleep(1)
    return distancia


def automatico():
#   fordward()
#   continua=1
#   while(continua):
#         distance=getDistanceRight()
#   	 if distance<30:
#		GPIO.output(LEDROJO,True)
#		stop()
#time.sleep(0.3)
	SpinRight()
	time.sleep(2)
#		continua=0
#		GPIO.output(LEDROJO,False)
def stop():
    global speed
    GPIO.output(Enable1,True)
    GPIO.output(Enable2,True)
    p.ChangeDutyCycle(0)
    q.ChangeDutyCycle(0)
    a.ChangeDutyCycle(0)
    b.ChangeDutyCycle(0)
    p.ChangeFrequency(speed + 5)
    a.ChangeFrequency(speed + 5)
def backwards():
    global speed
    GPIO.output(Enable1,True)
    GPIO.output(Enable2,True)
    p.ChangeDutyCycle(speed)
    q.ChangeDutyCycle(0)
    a.ChangeDutyCycle(speed)
    b.ChangeDutyCycle(0)
    p.ChangeFrequency(speed + 5)
    a.ChangeFrequency(speed + 5)
    #file = open( "/dev/input/mouse1", "rb" );
    #X=0
    #Y=0
    #i=0
    #final=time.time()
    #while (i<50):
		#i=i+1
		#buf = file.read(3)
		#dx,dy=struct.unpack( "bb" ,buf[1:] )
		#transcurrido=time.time()-final
		#final=time.time()
		#if transcurrido < 0.6:
			#X=X+(dx*transcurrido)
			#Y=Y+(dy*transcurrido)
		#print Y
    


def fordward():
    global speed
    GPIO.output(Enable1,True)
    GPIO.output(Enable2,True)
    yk=0
    yk3=0
    Y=0.0
    distan=float(distancia.get())
    conver1=0.27
    conver2=0.2524
    file = open( "/dev/input/mouse1", "rb" )
    file1 = open( "/dev/input/mouse0", "rb" )
    at=time.time()         
    p.ChangeDutyCycle(0)
    q.ChangeDutyCycle(speed)
    a.ChangeDutyCycle(0)
    b.ChangeDutyCycle(speed)
    q.ChangeFrequency(speed + 5)
    b.ChangeFrequency(speed + 5)
    while (Y<distan):
	buf=file.read(3)
	buf1=file1.read(3)
	dx,dy=struct.unpack("bb",buf[1:])
	dx1,dy1=struct.unpack("bb",buf1[1:])
	yk1=dy
	yk2=dy1
        #D_x(k+1) = D_x(k) + h/2 * (DATA(k+1, 2) + DATA(k,2)) 
	yk1 = yk+(time.time()-at)*yk1
	yk2= yk3+(time.time()-at)*yk2
	at=time.time()
	yk=yk1
	yk3=yk2
	print yk1
	print yk2
	Y=(yk1*conver1+yk2*conver2)/2
        q.ChangeDutyCycle(speed)
        b.ChangeDutyCycle(speed-15)
        q.ChangeFrequency(speed + 5)
        b.ChangeFrequency(speed-15 + 5)
	if Y<distan/2.0:
             speed = speed + 1
             if speed > vmax:
                speed = vmax
        if Y > distan-distan/2.0:
             speed = speed - 1
             if speed < 40:
                speed = 40
    q.ChangeDutyCycle(0)
    b.ChangeDutyCycle(0)
    q.ChangeFrequency(0+5)
    b.ChangeFrequency(0+5)
    speed=40
                
                    
		
def SpinRight():
    global speed
    speed=85
    GPIO.output(Enable1,True)
    GPIO.output(Enable2,True)
    yk=0
    xk=0
    xk3=0
    yk3=0
    Lraton=11
    L2raton=7
    p.ChangeDutyCycle(0)
    q.ChangeDutyCycle(speed)
    a.ChangeDutyCycle(speed)
    b.ChangeDutyCycle(0)
    q.ChangeFrequency(speed + 5)
    a.ChangeFrequency(speed + 5)
    at2=time.time()
    at1=time.time()
    angul=float(angulo.get())
    calculoang=0.0
    convery2=0.08
    converx2=0.25
    convery1=0.105
    converx1=0.275
    file = open("/dev/input/mouse1","rb")
    file1 = open("/dev/input/mouse0","rb")
    while (calculoang<angul):
		buf = file.read(3)
		buf1=file1.read(3)
		dx,dy=struct.unpack( "bb" ,buf[1:] )
		dx1,dy1=struct.unpack("bb",buf1[1:])
		yk2=dy1
		xk2=dx1
		yk1=dy
		xk1=dx
		xk2=xk3+(time.time()-at2)*xk2
                xk1= xk+(time.time()-at2)*xk1
		at2=time.time()
		xk3=xk2
		xk=xk1
		yk2=yk3+(time.time()-at1)*yk2
		yk1= yk+(time.time()-at1)*yk1
		at1=time.time()
		yk3=yk2
		yk=yk1
		Y1=abs(yk1*convery1)
		X1=abs(xk1*converx1)
		X2=abs(xk2*converx2)
		Y2=abs(yk2*convery2)
		calpart1 = math.pi/2
		calpart11 = math.atan2((Lraton - Y1),X1)
		calpart12=math.atan2((L2raton-Y2),X2)
                calculoang = (calpart1 - (calpart11+calpart12)/2)*180/math.pi
		print X1
		print X2
		print Y1
		print Y2
		print calculoang
    #            q.ChangeDutyCycle(speed+5)
    #            a.ChangeDutyCycle(speed-10)
    #            q.ChangeFrequency(speed+5 + 5)
    #            a.ChangeFrequency(speed-10 + 5)
    #		if calculoang < angul/2.0:
    #                speed = speed + 1
    #                if speed >85 :
    #                    speed = 85
#                if calculoang > angul-angul/2.0:
 #                   speed = speed -1
  #                  if speed < 65:
   #                     speed = 65
    q.ChangeDutyCycle(0)
    a.ChangeDutyCycle(0)
    q.ChangeFrequency(5)
    a.ChangeFrequency(5)
    
def SpinLeft():
    GPIO.output(Enable1,True)
    GPIO.output(Enable2,True)
    p.ChangeDutyCycle(0)
    q.ChangeDutyCycle(speed)
    a.ChangeDutyCycle(speed)
    b.ChangeDutyCycle(0)
    p.ChangeFrequency(speed + 5)
    a.ChangeFrequency(speed + 5)
def turn():
    servotimefin=450
    pwm.set_pwm(3,0,servotimefin)
    pwm.set_pwm(0,0,servotimefin)
def exit():
    GPIO.cleanup()
    print "quit"


#ultrasonic sensors functions  
def getDistanceRight():
    GPIO.output (RCT,True)
    time.sleep (0.00001)
    GPIO.output (RCT, False)
    start= time.time()
    while GPIO.input (RCE) == 0:
        start =time.time()
    while GPIO.input (RCE) == 1:
        stop =time.time()
    t_trans= stop-start
    distancia = (t_trans*34300)/2
    print distancia
try:    
    while(1):
        turn()
##def getDistanceLeft():
##    GPIO.output (LCT,True) 
##    time.sleep (0.00001)            
##    GPIO.output (LCT, False) 
##    start= time.time()                
##    while GPIO.input (lCE) == 0: 
##        start =time.time()             
##    while GPIO.input (LCE) == 1: 
##        stop =time.time()              
##    t_trans= stop-start                
##    distancia = (t_trans*34300)/2
##    #print distancia
##    time.sleep(1)
##    return distancia
##def getDistanceSide():
##    GPIO.output (LST,True) 
##    time.sleep (0.00001)            
##    GPIO.output (LST, False) 
##    start= time.time()                
##    while GPIO.input (LSE) == 0: 
##        start =time.time()             
##    while GPIO.input (LSEE) == 1: 
##        stop =time.time()              
##    t_trans= stop-start                
##    distancia = (t_trans*34300)/2
##    #print distancia
##    time.sleep(1)
##    return distancia

##try:
##        move(1.299,2.25,0.5,0.433,0.75,-0.5)
    
    ##while (1):
        ##forward()
	#turnRight(45)
##	distancia=getDistanceRight()      
##        if distancia<30:
##		if primera==1: 
##		turnRight(45)
##		time.sleep(0.1)
##		turnLeft(0)
##		primera=0
##		girado=1
##	else if distancia>30 && girado=1
##        	primera=1
##		girado=0


##        DR=servos.getDistanceRight()
##        DL=servos.getDistanceLeft()
##        DS=servos.getDistanceSide()
##        if DR <=10 and DL > 10
##            obstacleRight= True
##        if DL<=10 and DR > 10
##            obstacleleft = True
##        if DL <=10 and DL<=10
##            obstacleCentre=True
##        if obstacleRight
##            servos.stop()
##            servos.turnLeft()
##            #servos.forward()
##        if obstacleLeft
##            servos.stop()
##            servos.turnRight()
##            #servos.forward()
##        if obstacleCentre
##            servos.stop()
##            servos.turnRight()
##            #servos.forward()
##        
except KeyboardInterrupt:
    GPIO.cleanup()
    print "quit"
    
       

