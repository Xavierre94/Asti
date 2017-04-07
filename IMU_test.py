#
#solenero.tech@gmail.com
#solenerotech.wordpress.com

#solenerotech 2013.07.31

#2013.10.1 ImU Test 2

from time import sleep,time
import numpy
from kalmanfilter import KalmanFilterLinear
from lowpassfilter import lowpassfilter
#import pylab

try:
    from MPU6050 import MPU6050
    #print ('MPimport ok')
except ImportError:
    print ('import nok')


#logger = logging.getLogger(__name__)
IMU=MPU6050()
IMU.updateOffsets('IMU_offset.txt')
IMU.readOffsets('IMU_offset.txt')
print ('IMU ready!')



#Kalman filter parameters for a 1-dim case x 3
#dimension with error distribution = gaussian
#
A = numpy.eye(3)
H = numpy.eye(3)
B = numpy.eye(3)*0
Q = numpy.eye(3)*0.001
#play with Q to tune the smoothness
R = numpy.eye(3)*0.01
xhat = numpy.matrix([[0],[0],[0]])
P= numpy.eye(3)

kf = KalmanFilterLinear(A,B,H,xhat,P,Q,R)
lpf=lowpassfilter(0.025)

fax=0
fay=0
faz=0
fgx=0
fgy=0
fgz=0
faxk=0
fayk=0
fazk=0
faxf=0
fayf=0
fazf=0
#measuredfax=[]
#kalmanfx=[]
lines=''
lines=lines+('n|t|dt|fax| fay| faz| fgx| fgy| fgz| faxf| fayf| fazf| faxk| fayk| fazk\n')
lines=lines+('0| 0| 0|'+str(fax)+'|'+str(fay)+'|'+str(faz)+'|'+str(fgx)+'|'+str(fgy)+'|' + str(fgz)+ '|' +str(faxf)+'|' + str(fayf)+'|' + str(fazf)+'|' + str(faxk)+'|' + str(fayk)+'|' + str(fazk)+' \n')
inittime=time()
tottime=0
cycletime=0.03
for i in range (2000):
    tottime_old=tottime
    fax, fay, faz, fgx, fgy, fgz= IMU.readSensors()
    faxk,fayk,fazk = kf.filter(numpy.matrix([[0],[0],[0]]),numpy.matrix([[fax],[fay],[faz]]))
    tottime=time()-inittime
    steptime=tottime-tottime_old
    faxf,fayf,fazf=lpf.filter(fax,fay,faz,steptime)
    lines=lines +(str(i)+'|'+str(tottime)+'|'+str(steptime)+'|'+str(fax)+'|'+str(fay)+'|'+str(faz)+'|'+str(fgx)+'|'+str(fgy)+'|' + str(fgz)+ '|' +str(faxf)+'|' + str(fayf)+'|' + str(fazf)+'|' + str(faxk)+'|' + str(fayk)+'|' + str(fazk)+' \n')
    #sleep(0.001)
    #print str(cycletime-steptime)
    #sleep(cycletime-steptime)
    #measuredfax.append(fax)
    #kalmanfx.append(faxk)
#print str(tottime)
with open('sensor_data.txt', 'w+') as data_file:
    data_file.write(lines)
    data_file.flush()


#if False:
#    pylab.plot(range(1000),measuredfax,'b',range(1000),range(1000),kalmanfax,'g')
#    pylab.xlabel('Time')
#    pylab.ylabel('Voltage')
#    pylab.title('Voltage Measurement with Kalman Filter')
#    pylab.legend(('measured','true voltage','kalman'))
#    pylab.show()



