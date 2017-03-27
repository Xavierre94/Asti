import RPi.GPIO as GPIO 
import time 
GPIO.setmode (GPIO.BOARD) 
GPIO_TRIGGER = 35
GPIO_ECHO = 33
GPIO.setup(GPIO_TRIGGER,GPIO.OUT) 
GPIO.setup(GPIO_ECHO,GPIO.IN) 
try:
    while(1):
           
        GPIO.output (GPIO_TRIGGER, True)
        time.sleep(0.00001)
        GPIO.output (GPIO_TRIGGER, False)
        while GPIO.input (GPIO_ECHO) == 0:
            start= time.time() 
        while GPIO.input (GPIO_ECHO) == 1: 
            stop =time.time()
        t_trans= stop-start                
        distancia = (t_trans*32100)/2
        print distancia
        time.sleep(0.05)

except KeyboardInterrupt:
    GPIO.output (GPIO_TRIGGER, False)
    GPIO.cleanup()
        
