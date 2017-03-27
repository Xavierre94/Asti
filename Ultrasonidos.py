import RPi.GPIO as GPIO #Importamos la librería para el manejo de los pines
import time #Importamos la librería para manejo de tiempo
GPIO.setmode (GPIO.BCM) #Cambiamos el modo de la placa a BCM
GPIO_TRIGGER = 25       # El pin 25 se usa como TRIGGER
GPIO_ECHO = 7           #Usamos el pin 7 como ECHO
GPIO.setup (GPIO_TRIGGER, GPIO.OUT) #Configuramos el GPIO asociado al TRIGGER como salida
GPIO.setup (GPIO_ECHO, GPIO.IN) #GPIO asociado a ECHO como entrada
GPIO.output(GPIO_TRIGGER,False)
try:
    while (1):                    #iniciamos un bucle infinito
        GPIO.output (GPIO_TRIGGER,True) #enviamos un pulso de ultrasonido
        time.sleep (0.00001)            #esperamso 0.01 ms
        GPIO.output (GPIO_TRIGGER, False) #Apamos el pulso
        start= time.time()                #Guardamos el tiempo actual mediante time.time
        while GPIO.input (GPIO_ECHO) == 0: # Mientras no se reciba señal
            start =time.time()             #Mantenemos el tiempo actual mediante time.time
        while GPIO.input (GPIO_ECHO) == 1: #Si se recibe una señal
            stop =time.time()              #Guardamos el tiempo en el que se ha recibido la señal
        t_trans= stop-start                #Tiempo de retorno de la señal
        distancia = (t_trans*34300)/2       #Distancia en cms es igual a velocidad por tiempo
        time.sleep(1)                        #pausamos para que no se sature el procesador
        GPIO.cleanup()
        break


