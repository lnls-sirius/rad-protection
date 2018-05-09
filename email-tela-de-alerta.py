import smtplib
import time
import sys
from epics import PV

def send(pvname, name): #se a dose ainda está maior que 2uSv, envio falando qual sonda alarmou

    smtp = smtplib.SMTP('smtp.gmail.com', 587)  # porta gmail TLS 587 outlook e a mesma hotmail = 465
    smtp.starttls()

    smtp.login('controle.supervisorio@gmail.com', 'Controle123')

    subject = 'Alerta Radiacao via supervisório:' + '  ' + name
    mail_de = 'controle.supervisorio@gmail.com'
    mail_para = 'fernando.bacchim@lnls.br' #adc remetente
    mail_msgm = 'Subject: %s\n\n%s' % (subject,'Tela do supervisório fechada após a sonda ' + name + ' atingir o limite da dose integral. \n Situação atual: ACIMA DO LIMITE')
    smtp.sendmail(mail_de,mail_para, mail_msgm)

def send2(): #se a leitura de todas as sondas é menor que 2uSv, apenas alerto que a tela foi fechada

    smtp = smtplib.SMTP('smtp.gmail.com', 587)  # porta gmail TLS 587 outlook e a mesma hotmail = 465
    smtp.starttls()

    smtp.login('controle.supervisorio@gmail.com', 'Controle123')

    subject = 'Alerta Radiacao via supervisório'
    mail_de = 'controle.supervisorio@gmail.com'
    mail_para = 'fernando.bacchim@lnls.br' #adc remetente
    mail_msgm = 'Subject: %s\n\n%s' % (subject,'Tela do supervisório fechada após sonda atingir o limite da dose integral.\n Situação atual: OKAY.')

    smtp.sendmail(mail_de,mail_para, mail_msgm)


pvthermo = PV('RAD:THERMO:DoseIntegral')
integralthermo = pvthermo.value
pvelse = PV('RAD:ELSE:DoseIntegral')
integralelse = pvelse.value
pvberthold = PV('RAD:Berthold:DoseIntegral').value
integralberthold = pvberthold.value

# while(1):
if integralthermo >= 2:
    send(integralthermo, 'THERMO')
if integralelse >= 2:
    send(integralelse, 'ELSE')
if integralberthold >= 2:
    send(integralberthold, 'Berthold')
else:
    send2()












