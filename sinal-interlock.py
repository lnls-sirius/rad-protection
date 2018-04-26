#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import time
import smtplib
import Adafruit_BBIO.GPIO as GPIO
from epics import PV

def send(integralBuffer, name):

    smtp = smtplib.SMTP('smtp.gmail.com', 587)  # porta gmail TLS 587 outlook e a mesma hotmail = 465
    smtp.starttls()

    smtp.login('controle.supervisorio@gmail.com', 'Controle123')

    subject = 'Alerta Radiacao Interlock:' + '  ' + name 
    mail_de = 'controle.supervisorio@gmail.com'
    mail_para = 'fernando.bacchin@lnls.br' #adc remetente
    mail_msgm100 = 'Subject: %s\n\n%s' % (subject,'A dose integral de Radiacao atingiu 2uSv na sonda ' + name + ' e desarmou o sistema de interlock')

    if integralBuffer[0] < (maxintegral) and integralBuffer[-1] > (maxintegral) :
        smtp.sendmail(mail_de, mail_para, mail_msgm100 + '  ' + name)

integralThermo = 0.0
integralElse = 0.0
integralBerthold = 0.0
Thermo = 0.0
Else = 0.0
Berthold = 0.0
maxintegral = 2.0
integralBufferThermo = [0.0]*2
integralBufferElse = [0.0]*2
integralBufferBerthold = [0.0]*2

# setando o pino como saída para utilizar como trigger
GPIO.setup("P9_14", GPIO.OUT)
GPIO.output("P9_14", GPIO.HIGH)

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

        # Adc os valores das integrais no Buffer
        integralBufferThermo.append(Thermo)
        integralBufferElse.append(Else)
        integralBufferBerthold.append(Berthold)

        # Printando os valores para debug
        #print(Thermo)
        #print(Else)
        #print(Berthold)

        # lógica de controle trigger
        if Thermo >= maxintegral or Else >= maxintegral or Berthold >= maxintegral:
            GPIO.output("P9_14", GPIO.LOW)
            send(integralBufferThermo, 'Thermo')
            send(integralBufferElse, 'Else')
            send(integralBufferBerthold, 'Berthold')

        if Thermo < maxintegral and Else < maxintegral and Berthold < maxintegral:
            GPIO.output("P9_14", GPIO.HIGH)

        if len(integralBufferThermo) > 2:
            integralBufferThermo = integralBufferThermo[1:]

        if len(integralBufferElse) > 2:
            integralBufferElse = integralBufferElse[1:]

        if len(integralBufferBerthold) > 2:
            integralBufferBerthold = integralBufferBerthold[1:]
        

    except Exception as e:
        print(e)
        pass 



