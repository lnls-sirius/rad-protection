#!/usr/bin/python
# -*- coding: utf-8 -*-

import smtplib
import time
import sys
from epics import PV

# função para enviar email
def send(main, valormain, sonda1, valorsonda1, sonda2, valorsonda2, maxintegral):

    smtp = smtplib.SMTP('smtp.gmail.com', 587)  # porta gmail TLS 587 outlook e a mesma hotmail = 465
    smtp.starttls()

    smtp.login('controle.supervisorio@gmail.com', 'Controle123')

    subject = 'Alerta Radiação via Supervisório'
    mail_de = 'controle.supervisorio@gmail.com'
    mail_para = 'fernando.bacchim@lnls.br'
    mail_msgm1 = 'Subject: %s\n\n%s' % (subject,'ALERTA !!\nUma das sondas de Radiação atingiu o limite da Integral em 4 horas!')
    mail_msgm2 = '\n \nDiagnóstico dos dados: \n \n' + '{}:  {} uSv \n{}:  {} uSv \n{}:  {} uSv \n'.format(main, valormain, sonda1, valorsonda1, sonda2, valorsonda2)
    mail_msgm3 = '\n\nObservação: O email foi enviado pelo supervisório pois a sonda {} atingiu um limite com valor de {} uSv.'.format(main, valormain)
    mail_msgm4 = '\n\nProteção Radiológica - SIRIUS\nGrupo de Controle\nLNLS - CNPEM'
    mail_msgm = mail_msgm2 + mail_msgm3 + mail_msgm4
    mail_msgm50 = mail_msgm1 + '\nA sonda {} atingiu 50% do valor máximo permitido(1 uSv em 4h)'.format(main) + mail_msgm
    mail_msgm75 = mail_msgm1 + '\nA sonda {} atingiu 75% do valor máximo permitido(1.5 uSv em 4h)'.format(main) + mail_msgm
    mail_msgm100 = mail_msgm1 + '\nA sonda {} atingiu 100% do valor máximo permitido(2 uSv em 4h)'.format(main) + mail_msgm

    # lógica para envio do email
    if valormain[0] < (0.50*maxintegral) and valormain[-1] > (0.50*maxintegral):
        smtp.sendmail(mail_de,mail_para, mail_msgm50 + '  ' + main)

    elif valormain[0] < (0.75*maxintegral) and valormain[-1] > (0.75*maxintegral):
        smtp.sendmail(mail_de, mail_para, mail_msgm75 + '  ' + main)

    elif valormain[0] < (maxintegral) and valormain[-1] > (maxintegral) :
        smtp.sendmail(mail_de, mail_para, mail_msgm100 + '  ' + main)

    smtp.close()

integralBufferThermo = [0.0]*2
integralBufferElse = [0.0]*2
integralBufferBerthold = [0.0]*2
integralThermo = 0.0
integralBerthold = 0.0
integralElse = 0.0
maxintegral = 2

# criando os obj PV
integralThermo = PV('RAD:THERMO:DoseIntegral')
integralElse = PV('RAD:ELSE:DoseIntegral')
integralBerthold = PV('RAD:Berthold:DoseIntegral')

#name das PVs
probe_thermo = 'Thermo'
probe_else = 'Else'
probe_berthold = 'Berthold'

while (1):

    try:

        time.sleep(1)      

        # Armazenando os obj PV no Buffer e chamando a função
        integralBufferThermo.append(integralThermo.value)
        if len(integralBufferThermo) >= 3 and integralBufferThermo[-1] > 0.5*maxintegral:
            send(integralBufferThermo, probe_thermo, integralBufferElse[-1], probe_else, integralBufferBerthold, probe_berthold, maxintegral)

        integralBufferElse.append(integralElse.value)
        if len(integralBufferElse) >= 3 and integralBufferElse[-1] > 0.5*maxintegral:
            send(integralBufferElse , probe_else, integralBufferBerthold[-1], probe_berthold, integralBufferThermo[-1], probe_thermo, maxintegral)

        integralBufferBerthold.append(integralBerthold.value)
        if len(integralBufferBerthold) >= 3 and integralBufferBerthold[-1] > 0.5*maxintegral:
            send(integralBufferBerthold, probe_berthold, integralBufferThermo[-1], probe_thermo, integralBufferElse, probe_else, maxintegral)

        # esvaziando os Buffers
        if len(integralBufferThermo) > 2:
            integralBufferThermo = integralBufferThermo[1:]

        if len(integralBufferElse) > 2:
            integralBufferElse = integralBufferElse[1:]

        if len(integralBufferBerthold) > 2:
            integralBufferBerthold = integralBufferBerthold[1:]

    except Exception as e:
        print(e)
        pass

 
