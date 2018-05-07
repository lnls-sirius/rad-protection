import smtplib
import time
import sys
from epics import PV

def send(pvname, name):

    smtp = smtplib.SMTP('smtp.gmail.com', 587)  # porta gmail TLS 587 outlook e a mesma hotmail = 465
    smtp.starttls()

    smtp.login('controle.supervisorio@gmail.com', 'Controle123')

    subject = 'Alerta Radiacao LNLS via supervisório:' + '  ' + name
    mail_de = 'controle.supervisorio@gmail.com'
    mail_para = 'isabela.moraes@lnls.br' #adc remetente
    mail_msgm50 = 'Subject: %s\n\n%s' % (subject,'A dose integral de Radiacao atingiu 50% na sonda' + name)
    mail_msgm75 = 'Subject: %s\n\n%s' % (subject,'A dose integral de Radiacao atingiu 75% na sonda' + name)
    mail_msgm100 = 'Subject: %s\n\n%s' % (subject,'A dose integral de Radiacao atingiu 100% na sonda' + name)

    if pvname >= 2:
        smtp.sendmail(mail_de,mail_para, mail_msgm100 + '  ' + name)

    elif pvname >= 1.5:
        smtp.sendmail(mail_de, mail_para, mail_msgm75 + '  ' + name)

    elif pvname >= 1:
        smtp.sendmail(mail_de, mail_para, mail_msgm50 + '  ' + name)


pvthermo = PV('RAD:THERMO:DoseIntegral')
integralthermo = pvthermo.value
pvelse = PV('RAD:ELSE:DoseIntegral')
integralelse = pvelse.value
pvberthold = PV('RAD:Berthold:DoseIntegral').value
integralberthold = pvberthold.value

while(1):
	if integralthermo:








