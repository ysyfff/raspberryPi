#!/usr/bin/python
#-*- coding: utf-8 -*-
import time
import RPi.GPIO as GPIO
import os

GPIO.setmode(GPIO.BCM) #使用BCM编码方式
#定义引脚
GPIO_1 = 1
GPIO_2 = 2
GPIO_3 = 4
GPIO_4 = 4
GPIO_14 = 14
GPIO_16 = 16
GPIO_21 = 21
GPIO_22 = 22
GPIO_23 = 23
GPIO_24 = 24

led = 21   
#设置引脚为输入和输出  
GPIO.setwarnings(False)   
#设置23针脚为输入，接到红外避障传感器模块的out引脚  
#GPIO.setup(GPIO_23,GPIO.IN)   
GPIO.setup(GPIO_14,GPIO.OUT)
#GPIO.setup(GPIO_24,GPIO.IN)

  
def warn():   #亮灯来作为有障碍物时发出的警告  
#    GPIO.output(led,GPIO.HIGH)  
#    time.sleep(0.5)
#    GPIO.output(led, GPIO.LOW)
     time.sleep(0.5)
     print "warn"
          
while True:  
    print "low"
    GPIO.output(GPIO_14, GPIO.LOW) #当有障碍物时，传感器输出低电平，所以检测低电平  
    time.sleep(15)
    print "high"
    GPIO.output(GPIO_14, GPIO.HIGH) #当有障碍物时，传感器输出低电平，所以检测低电平  
    time.sleep(15)

GPIO.cleanup()
