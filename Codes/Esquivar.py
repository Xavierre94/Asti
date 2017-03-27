# -*- coding: utf-8 -*-
import servos, time, math
import RPi.GPIO as GPIO
import Adafruit_PCA9685
import Adafruit_ADS1x15
import struct

import sys
from Tkinter import *
GPIO.setwarnings(False)
GPIO.setmode (GPIO.BOARD) 
#inicializar puertos y PCA9685
pwm = Adafruit_PCA9685.PCA9685()
#libreria ADC
adc = Adafruit_ADS1x15.ADS1115()
GAIN=1
#motor pins
Enable1=36
Enable2=38
GPIO.setup(Enable1,GPIO.OUT)
GPIO.setup(Enable2,GPIO.OUT)
pwmMax=4095
pwm.set_pwm_freq (60)
pwm.set_pwm(0,0,pwmMax) 
global speed
speed=50
global vmax
vmax = 75
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
FT=29
FE=31
LCT=33
LCE=35
global obstaculo
global pastillas
global giro1
global izquierda
global giro2
global angul
izquierda=False
giro1=False
obstaculo = False
pastillas=False
izquierda = False
giro2 = False
angul = 45
servos.init()
GPIO.setup(33,GPIO.OUT)
GPIO.setup(32,GPIO.IN)
GPIO.setup(FT,GPIO.OUT)
GPIO.setup(FE,GPIO.IN)
##GPIO.setup(LEDROJO,GPIO.OUT)
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

def stop():
    global speed
    GPIO.output(Enable1,True)
    GPIO.output(Enable2,True)
    p.ChangeDutyCycle(0)
    q.ChangeDutyCycle(0)
    a.ChangeDutyCycle(0)
    b.ChangeDutyCycle(0)
    p.ChangeFrequency(5)
    a.ChangeFrequency(5)
def backwards():
    global speed
    global obstaculo
    obstaculo=False
    GPIO.output(Enable1,True)
    GPIO.output(Enable2,True)
    yk=0
    yk3=0
    Y=0.0
    distan=float(distancia.get())
    conver1=0.215
    conver2=0.27
    file = open( "/dev/input/mouse1", "rb" )
    file1 = open( "/dev/input/mouse0", "rb" )
    at=time.time()         
    q.ChangeDutyCycle(0)
    p.ChangeDutyCycle(speed)
    b.ChangeDutyCycle(0)
    a.ChangeDutyCycle(speed)
    p.ChangeFrequency(speed + 5)
    a.ChangeFrequency(speed + 5)
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
	Y=(abs(yk1*conver1)+abs(yk2*conver2))/2
        p.ChangeDutyCycle(speed)
        a.ChangeDutyCycle(speed)
        p.ChangeFrequency(speed + 5)
        a.ChangeFrequency(speed + 5)
	if Y<distan/2.0:
             speed = speed + 1
             if speed > vmax:
                speed = vmax
        if Y > distan-distan/2.0:
             speed = speed - 1
             if speed < 50:
                speed = 50
    p.ChangeDutyCycle(0)
    a.ChangeDutyCycle(0)
    p.ChangeFrequency(0+5)
    a.ChangeFrequency(0+5)
    speed=40

def fordward():
    global giro1
    global giro2
    global speed
    global obstaculo
    global distan
    global pastillas
    global Y
    global izquierda
    GPIO.output(Enable1,True)
    GPIO.output(Enable2,True)
    yk=0
    yk3=0
    Y=0.0
    if pastillas == False :
        distan=float(distancia.get())
    conver1=0.215
    conver2=0.27
    file = open( "/dev/input/mouse1", "rb" )
    file1 = open( "/dev/input/mouse0", "rb" )
    at=time.time()         
    p.ChangeDutyCycle(0)
    q.ChangeDutyCycle(speed)
    a.ChangeDutyCycle(0)
    b.ChangeDutyCycle(speed)
    q.ChangeFrequency(speed + 5)
    b.ChangeFrequency(speed + 5)
    while (Y<distan and (obstaculo==False or giro1==True or giro2== True)):
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
	Y=(yk1*conver1+yk2*conver2)*2.2/2
	if giro1==False and giro2 == False and pastillas==True:
            obstaculoFrente()
        elif giro1==True or giro2 == True:
            obstaculoIzda()
        q.ChangeDutyCycle(speed)
        b.ChangeDutyCycle(speed)
        q.ChangeFrequency(speed+5)
        b.ChangeFrequency(speed+5)
	if Y<distan/2.0:
             speed = speed + 1
             if speed > vmax:
                speed = vmax
        if Y > distan-distan/2.0:
             speed = speed - 1
             if speed < 50:
                speed = 50
    q.ChangeDutyCycle(0)
    b.ChangeDutyCycle(0)
    q.ChangeFrequency(0+5)
    b.ChangeFrequency(0+5)
    speed=40        
		
def SpinLeft():
    global speed
    global angul
    speed=85
    GPIO.output(Enable1,True)
    GPIO.output(Enable2,True)
    yk=0
    xk=0
    xk3=0
    dx=0
    dx1=0
    dy=0
    dy1=0
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
    if pastillas == False :
        angul=float(angulo.get())
    calculoang=0.0
    convery2=0.012
    converx2=0.25
    convery1=0.13
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
                calculoang = ((calpart1 - (calpart11+calpart12)/2)*180/math.pi)*90/65
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
    
def SpinRight():
    global speed
    global angul
    speed=85
    GPIO.output(Enable1,True)
    GPIO.output(Enable2,True)
    yk=0
    dx=0
    dx1=0
    dy=0
    dy1=0
    xk=0
    xk3=0
    yk3=0
    Lraton=11
    L2raton=7
    q.ChangeDutyCycle(0)
    p.ChangeDutyCycle(speed)
    b.ChangeDutyCycle(speed)
    a.ChangeDutyCycle(0)
    p.ChangeFrequency(speed + 5)
    b.ChangeFrequency(speed + 5)
    at2=time.time()
    at1=time.time()
    if pastillas == False :
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
                calculoang = (calpart1 - (calpart11+calpart12)/2)*180/math.pi*2*90/65
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
    p.ChangeDutyCycle(0)
    b.ChangeDutyCycle(0)
    p.ChangeFrequency(5)
    b.ChangeFrequency(5)

def obstaculoFrente():
    global obstaculo
    distancia=getDistanceFront()
    #print distancia
    if(distancia<45):
        obstaculo=True
        stop()

def obstaculoIzda():
    global izquierda
    global giro1
    global giro2
    distancia = getDistanceLeft()
    if distancia > 70:
        izquierda = True
        giro1 =False
        giro2= False
        
def turn(channel,anglefinal,servo):
    if servo==1:
        servotimefin=int(2.44*anglefinal+480)
    elif servo==2:
        servotimefin=int(3*anglefinal+320)
    elif servo==3:
        servotimefin=int(-2.22*anglefinal+160)
        print servotimefin
    elif servo==4:
        servotimefin=int(-1.87*anglefinal+300)
    pwm.set_pwm(channel,0,servotimefin)
    
def move():
    global q1ant
    global q2ant
    global q3ant
    global q4ant
    global q1
    global q2
    global q3
    global q4
    x=float(x1.get())
    y=float(y1.get())
    z=float(z1.get())
    ax=float(ax2.get())
    ay=float(ay2.get())
    az=float(az2.get())
    L4=0.1
    mx=x-L4*ax
    print mx
    my=y-L4*ay
    print my
    mz=z-L4*az
    print mz
    L1=0.19
    L2=0.075
    L3=0.094
    
    if (mx==0 and my==0):
        q1=0
    elif (mx==0 and my>0):
	q1=math.pi/2
    elif (mx==0 and my<0):
	q1=-math.pi/2
    else:
        q1=math.atan(my/mx)
    if q1 > 60*math.pi/180:
        q1=60*math.pi/180
    elif q1 < -120*math.pi/180:
        q1 = -120*math.pi/180
    print q1*180/math.pi
    p=math.cos(q1)
    c=math.sin(q1)
    r=math.sqrt((mx/p)**2+(mz-L1)**2)
    if mx==0:
        FI=math.pi/2
    else:    
        FI = math.atan((mz-L1)*p/mx)
    q2=FI+math.acos(((mx/p)**2+L2**2-L3**2+mz**2+L1**2-2*mz*L1)/(2*L2*r))
    if abs(q2)<0.1:
        q2=0
    if q2 < 40*math.pi/180:
        q2=40*math.pi/180
    elif q2 > 100*math.pi/180:
        q2 = 100*math.pi/180
    print q2*180/math.pi
    t=L2*math.cos(q2)
    j=L2*math.sin(q2)
    k=math.cos(q1)
    if mx/p-t==0:
        q3=math.pi/2-q2
    else:
        q3= math.atan2((mz-L1-j),(mx/p-t))-q2
        #-q2
    if abs(q3)<0.1:
        q3=0
    if q3< -90 *math.pi/180:
        q3=-90*math.pi/180
    elif q3>15*math.pi/180:
        q3=15*math.pi/180
    print q3*180/math.pi
    a=math.cos(q2+q3)
    b=math.sin(q2+q3)
    q4=math.atan2(-(ax*b*p - az*a + ay*b*c),(az*b + ax*a*p + ay*a*c))
    if abs(q4)<0.1:
        q4=0
    if q4 > 5*math.pi/180:
        q4 =5*math.pi/180
    elif q4 < -75*math.pi/180:
        q4 = -75*math.pi/180
    print q4*180/math.pi
    q1=q1*180/math.pi
    q2=q2*180/math.pi
    q3=q3*180/math.pi
    q4=q4*180/math.pi
    paso=10.0
    i=0
    movimiento1=(q1-q1ant)/paso
    movimiento2=(q2-q2ant)/paso
    movimiento3=(q3-q3ant)/paso
    movimiento4=(q4-q4ant)/paso
    while i<10:
        q1ant=q1ant+movimiento1
        turn(0,q1ant,1)
        q2ant=q2ant+movimiento2
        turn(1,q2ant,2)
        q3ant=q3ant+movimiento3
        turn(2,q3ant,3)
        q4ant=q4ant+movimiento4
        turn(3,q4ant,4)
        i=i+1
        #time.sleep(0.1)
def abrepinza():
	pwm.set_pwm(4,0,250)
def cierrapinza():
    angulo = 250
    angulomin=600
    while (angulo< angulomin):
         lectura = adc.read_adc(1, gain=GAIN)
         pwm.set_pwm(4,0,angulo)
         angulo=angulo+1
##            print 'no hay pico'
    cerrada = 1
def coge():
    pos1=0.18
    pos2=-0.05
    pos3=0.26
    or1=1
    or2=0
    or3=0
    abrepinza()
##    move (pos1,pos2,pos3,or1,or2,or3)
    time.sleep(0.1)
    cierrapinza()
##    move (0.19,0.1,0.265,1,0,0)
    
def exit():
    GPIO.cleanup()
    print "quit"


#ultrasonic sensors functions
def getDistanceFront():
    GPIO.output (FT,True)
    time.sleep (0.00001)
    GPIO.output (FT, False)
    start= time.time()
    while GPIO.input (FE) == 0:
        start =time.time()
    while GPIO.input (FE) == 1:
        stop =time.time()
    t_trans= stop-start
    distancia = (t_trans*32100)/2
    time.sleep(0.01)
    return distancia
def getDistanceLeft():
    GPIO.output (33, True)
    time.sleep(0.00001)
    GPIO.output (33, False)
    #startleft = time.time()
    while GPIO.input (32) == False:
##        print '0'
        startleft= time.time() 
    while GPIO.input (32) == True:
##        print '1'
        stopleft =time.time()
    t_transleft= stopleft-startleft               
    distancialeft = (t_transleft*32100)/2
    time.sleep(0.01)
    return distancialeft
    
def automaticopastillas():
        global obstaculo
        global pastillas
        global distan
        global Y
        global angul
        global izquierda
        global giro1
        global giro2
        pastillas = True
        #valor de control del pinza 
        valor_pinza=1300
        chn_pinza = 4 #channel de la pinza en el pwm
        #inicializamos valor del adc
        values_adc = 0
        #distan = ¿Dónde queremos ir?
         #objeto se encuentra en 10
        objeto = 150
        distan = objeto
        angul =45
        
        fordward()
        if obstaculo == True:
            angul = 45
            giro1=True
            inicio = Y #guarda posicion original en que se encuentra el coche
            SpinLeft()
            SpinLeft()
            fordward()
            if izquierda == True:
                fin = Y
                distancia_esquivar = fin -inicio
                SpinRight()
                SpinRight()
                obstaculo = False
                distan = 80
                fordward()
                obstaculo = True
                giro2=True
                #izquierda=False
                distan = 100
                fordward()
                fin2= Y+20
                SpinRight()
                SpinRight()
                obstaculo= False
                distan=distancia_esquivar
                fordward ()
                SpinLeft()
                SpinLeft()
                distan= objeto - (inicio+fin2)
                fordward()
        
##    except KeyboardInterrupt:
##        GPIO.cleanup()
##        print "quit"
    
       

ventana = Tk()
ventana.geometry("656x426")
ventana.title("interfaz brazo")
##imagenL=PhotoImage(file="Sin.PNG")
##lblimagen=Label(ventana,image=imagenL).place(x=0,y=0)

#definicion de la ventana

#ventana.grid(column=0, row=0, padx=(100,100), pady=(100,100))
#ventana.columnconfigure(0,weight=1)
#ventana.rowconfigure(0,weight=1)
#slider
q1 = Scale(ventana, from_=0, to=360, orient=HORIZONTAL)
q1.place(x=91,y=225)

q2 = Scale(ventana, from_=-50, to=200, orient=HORIZONTAL)
q2.place(x=91,y=265)
#
q3 = Scale(ventana, from_=-50, to=200, orient=HORIZONTAL)
q3.place(x=91,y=305)
#
q4 = Scale(ventana, from_=-90, to=90, orient=HORIZONTAL)
q4.place(x=91,y=345)
#

##Cuadros para introducir valores 
posx = ""
x1 = Entry(ventana, width=5, textvariable=posx)
x1.place(x=31,y=94)
#
posy = ""
y1 = Entry(ventana, width=5, textvariable=posy)
y1.place(x=71,y=94)
#
posz = ""
z1 = Entry(ventana, width=5, textvariable=posz)
z1.place(x=111,y=94)
ax1 = ""
ax2 = Entry(ventana, width=5, textvariable=ax1)
ax2.place(x=157,y=93)
#
#
distancia = ""
distancia = Entry(ventana, width=5, textvariable=distancia)
distancia.place(x=428,y=40)

angulo = ""
angulo = Entry(ventana, width=5, textvariable=angulo)
angulo.place(x=458,y=40)

ay1 = ""
ay2 = Entry(ventana, width=5, textvariable=ay1)
ay2.place(x=190,y=93)
#
#
az1 = ""
az2 = Entry(ventana, width=5, textvariable=az1)
az2.place(x=225,y=93)
#
##Botones
mover = Button(ventana, command=move, text="Start", width=5)
mover.place(x=22,y=112)
#

#
ini = Button(ventana, text="Home", width=5)
ini.place(x=68,y=139)
#
##botones coche
#
automatico = Button(ventana, text="Traer agua", command=automaticopastillas, width=10)
automatico.place(x=400,y=300)

automatico1 = Button(ventana, text="Traer medicación", width=15)
automatico1.place(x=500,y=300)

avanza = Button(ventana,command=fordward, text="Avanza", width=10)
avanza.place(x=448,y=64)
#
retro = Button(ventana, command=backwards, text="Retroceder", width=10)
retro.place(x=448,y=140)
#
girai = Button(ventana, command=SpinLeft, text="Gira Izquierda", width=10)
girai.place(x=368,y=98)
#
Stop1 = Button(ventana, command=stop, text="Stop", width=10)
Stop1.place(x=448,y=98)
#
girad = Button(ventana, command=SpinRight, text="Gira Derecha ", width=10)
girad.place(x=528,y=98)
#
abre= Button(ventana,command=abrepinza, text="Abrir Pinza", width=10)
abre.place(x=170,y=130)
cierra= Button (ventana, command =cierrapinza, text= "Cerrar Pinza", width = 10)
cierra.place(x=170,y=160)

##Calibraciones ratones
raton1X= ""
xavanza = Entry(ventana, width=5, textvariable=raton1X)
xavanza.place(x=350,y=350)
#
raton2X= ""
xavanza2 = Entry(ventana, width=5, textvariable=raton2X)
xavanza2.place(x=400,y=350)
#
raton1Y= ""
yavanza1 = Entry(ventana, width=5, textvariable=raton1Y)
yavanza1.place(x=350,y=380)
#
raton2Y= ""
yavanza2 = Entry(ventana, width=5, textvariable=raton2Y)
yavanza2.place(x=400,y=380)

##Calibraciones ratones giro
raton1girax= ""
xgira1 = Entry(ventana, width=5, textvariable=raton1girax)
xgira1.place(x=500,y=350)
#
raton2girax= ""
xgira2 = Entry(ventana, width=5, textvariable=raton2girax)
xgira2.place(x=550,y=350)
#
raton1Y= ""
ygira1= Entry(ventana, width=5, textvariable=raton1Y)
ygira1.place(x=500,y=380)
#
raton2Y= ""
ygira2 = Entry(ventana, width=5, textvariable=raton2Y)
ygira2.place(x=550,y=380)

ventana.mainloop()
ventana.mainloop()

