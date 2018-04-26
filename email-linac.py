import smtplib
import time
import sys
from epics import PV

def send(integralBuffer, name):

    smtp = smtplib.SMTP('smtp.gmail.com', 587)  # porta gmail TLS 587 outlook e a mesma hotmail = 465
    smtp.starttls()

    smtp.login('controle.supervisorio@gmail.com', 'Controle123')

    subject = 'Alerta Radiacao LNLS:' + '  ' + name
    mail_de = 'controle.supervisorio@gmail.com'
    mail_para = 'aureo.carneiro@lnls.br' #adc remetente
    mail_msgm50 = 'Subject: %s\n\n%s' % (subject,'A dose integral de Radiacao atingiu 50%')
    mail_msgm75 = 'Subject: %s\n\n%s' % (subject,'A dose integral de Radiacao atingiu 75%')
    mail_msgm100 = 'Subject: %s\n\n%s' % (subject,'A dose integral de Radiacao atingiu 100%')

    if integralBuffer[0] < (0.50*maxintegral) and integralBuffer[-1] > (0.50*maxintegral):
        smtp.sendmail(mail_de,mail_para, mail_msgm50 + '  ' + name)

    elif integralBuffer[0] < (0.75*maxintegral) and integralBuffer[-1] > (0.75*maxintegral):
        smtp.sendmail(mail_de, mail_para, mail_msgm75 + '  ' + name)

    elif integralBuffer[0] < (maxintegral) and integralBuffer[-1] > (maxintegral) :
        smtp.sendmail(mail_de, mail_para, mail_msgm100 + '  ' + name)

integralBufferThermo = [0.0]*2
integralBufferElse = [0.0]*2
integralBufferBerthold = [0.0]*2
integralThermo = 0.0
integralBerthold = 0.0
integralElse = 0.0
maxintegral = 2

while (1):

    try: 

        time.sleep(1)      

        # sonda THERMO
        integralThermo = PV('RAD:THERMO:DoseIntegral')
        print(integralThermo.value)
        integralBufferThermo.append(integralThermo.value)
        if len(integralBufferThermo) >= 3:
            send(integralBufferThermo, 'Thermo')

        # sonda ELSE
        integralElse = PV('RAD:ELSE:DoseIntegral')
        print(integralElse.value)
        integralBufferElse.append(integralElse.value)
        if len(integralBufferElse) >= 3:
            send(integralBufferElse , 'ELSE')

        # sonda Berthold
        integralBerthold = PV('RAD:Berthold:DoseIntegral')
        print(integralBerthold.value)
        integralBufferBerthold.append(integralBerthold.value)
        if len(integralBufferBerthold) >= 3:
            send(integralBufferBerthold, 'Berthold')

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

 
