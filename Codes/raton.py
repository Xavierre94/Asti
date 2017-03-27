#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 23:16:26 2016

@author: sheldom


mouse = file('/dev/input/mouse0')  
while True:  
    status, dx, dy = tuple(ord(c) for c in mouse.read(3))

    def to_signed(n):
        return n-((0x80 &amp; n) &lt;&lt; 1)

    dx = to_signed(dx)
    dy = to_signed(dy)
    print "%#02x %d %d" % (status, dx, dy)
    
    """
    
import struct
#import numpy as np
import time
import csv


file = open( "/dev/input/mouse0", "rb" );
X=0.0
Y=0.0
calibre=0.0
def getMouseEvent():
  buf = file.read(3);
 # button = ord( buf[0] );
 # bLeft = button & 0x1;
 # bMiddle = ( button & 0x4 ) > 0;
 # bRight = ( button & 0x2 ) > 0;
  x,y = struct.unpack( "bb", buf[1:] );
  return int(x), int(y)
  # return stuffs
  
def int_aprox_trap(xMin,xMax,numDiv): 

  deltaX=(xMax -xMin)/float(numDiv) 

  inte=(xMin + xMax)/2.0 
  k=1 
  while k < numDiv: 

    inte += xMin + k*deltaX 

    k += 1 

  return inte * deltaX
calibre=0.27
print (calibre)
i=0
lista = []
final=time.time()
while( i<2000 ):
  i=i+1
  buf = file.read(3);
  dx,dy=struct.unpack( "bb", buf[1:] );
  transcurrido=time.time()-final 
  final=time.time()
  if transcurrido < 0.6:
	X=X+(dx*transcurrido)
	Y=Y+(dy*transcurrido)
  print X*calibre
#print ("y: %f\n" % (Y*calibre) )
  #lista.extend([[i,X,Y]])
  #time.sleep(0.001)
  #print(i)
  
file.close();
print(lista)

#f = open('datos.csv','w')
#f.write('i,Dx,Dy\n')
with open("output.csv", "wb") as f:
      writer = csv.writer(f)
      writer.writerows(lista)




f.close();
