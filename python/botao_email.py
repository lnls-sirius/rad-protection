#!/usr/bin/python
# -*- coding: utf-8 -*-

import smtplib
import time
import sys
from epics import PV

# definindo a funcao para enviar o email
def send(thermo, valorthermo, el, valorel, berthold, valorberthold):

    smtp = smtplib.SMTP('smtp.gmail.com', 587)  # porta gmail TLS 587 outlook e a mesma hotmail = 465
    smtp.starttls()

    smtp.login('controle.supervisorio@gmail.com', 'Controle123')

    subject = 'Alerta Radiação via Supervisório'
    mail_de = 'controle.supervisorio@gmail.com'
    mail_para = 'fernando.bacchim@lnls.br'
    mail_msgm1 = 'Subject: %s\n\n%s' % (subject,'ALERTA !!\nUma das sondas de Radiação atingiu o limite da Integral em 4 horas!')
    mail_msgm2 = '\n \nDiagnóstico dos dados: \n \n' + '{}:  {} uSv \n{}:  {} uSv \n{}:  {} uSv \n'.format(thermo, valorthermo, el, valorel, berthold, valorberthold)
    mail_msgm3 = '\n\nObservação: O email foi enviado pelo supervisório pois alguém apertou o botão para restaurar o sistema'
    mail_msgm4 = '\n\nProteção Radiológica - SIRIUS\nGrupo de Controle\nLNLS - CNPEM'
    mail_msgm = mail_msgm1 + mail_msgm2 + mail_msgm3 + mail_msgm4
    smtp.sendmail(mail_de,mail_para, mail_msgm)

    smtp.close()

# obj PV
thermo = PV('RAD:THERMO:DoseIntegral')
Else = PV('RAD:ELSE:DoseIntegral')
berthold = PV('RAD:Berthold:DoseIntegral')

# Pegando o valor do obj PV
pvthermo = thermo.value
pvelse = Else.value
pvberthold = berthold.value

# nome das PVs
namethermo = 'Thermo'
nameelse = 'Else'
nameberthold = 'Berthold'

# chama a função enviar email
send(namethermo, pvthermo, nameelse, pvelse, nameberthold, pvberthold)

# delay
time.sleep(1)

# mata o programa
exit()



