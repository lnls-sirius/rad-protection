#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import time
import Adafruit_BBIO.GPIO as GPIO
from epics import PV

integralThermo = 0.0
integralElse = 0.0
integralBerthold = 0.0
Thermo = 0.0
Else = 0.0
Berthold = 0.0
maxintegral = 2.0

# setando o pino como saída para utilizar como trigger
GPIO.setup("P8_10", GPIO.OUT)
GPIO.output("P8_10", GPIO.HIGH)

while (1):

    try:

        time.sleep(1)

        # Pegando as PVs
        integralThermo = PV('RAD:THERMO:DoseIntegral')
        integralElse = PV('RAD:ELSE:DoseIntegral')
        integralBerthold = PV('RAD:Berthold:DoseIntegral')
        
        # Setando os valores das PVs
        Thermo = integralThermo.value
        Else = integralElse.value
        Berthold = integralBerthold.value

        # Printando os valores para debug
        #print(Thermo)
        #print(Else)
        #print(Berthold)

        # lógica de controle trigger
        if Thermo >= maxintegral or Else >= maxintegral or Berthold >= maxintegral:
            GPIO.output("P8_10", GPIO.LOW)

        if Themo < maxintegral and Else < maxintegral and Berthold < maxintegral:
            GPIO.output("P8_10", GPIO.HIGH)
        

    except Exception as e:
        print(e)
        pass 



