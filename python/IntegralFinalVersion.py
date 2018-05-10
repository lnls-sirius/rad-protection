#!/usr/bin/python
# -*- coding: utf-8 -*-

from epics import PV
import time
import sys
import datetime
from pcaspy import Driver, Alarm, Severity, SimpleServer
from Queue import Queue
import threading


class IntegralDriver(Driver):

    def __init__(self):

        Driver.__init__(self)

        self.queue = Queue()

        self.event = threading.Event()

        self.process = threading.Thread(target=self.processThread)
        self.scan = threading.Thread(target=self.scanThread)

        self.process.setDaemon(True)
        self.scan.setDaemon(True)

        self.process.start()
        self.scan.start()


    def scanThread(self):

        while (True):
            self.queue.put("UPDATE_PV")
            self.event.wait(1)

    def processThread(self):

        while (True):

            queue_item = self.queue.get(block=True)

            if (queue_item == "UPDATE_PV"):
                self.setParam("RAD:ELSE:IntegralGamma", else_integralgamma)
                self.setParam("RAD:ELSE:IntegralNeutron", else_integralneutron)
                self.setParam("RAD:ELSE:DoseIntegral", else_integral)
                self.setParam("RAD:THERMO:IntegralGamma", thermo_integralgamma)
                self.setParam("RAD:THERMO:IntegralNeutron", thermo_integralneutron)
                self.setParam("RAD:THERMO:DoseIntegral", thermo_integral)
                self.setParam("RAD:Berthold:IntegralGamma", berthold_integralgamma)
                self.setParam("RAD:Berthold:IntegralNeutron", berthold_integralneutron)
                self.setParam("RAD:Berthold:DoseIntegral", berthold_integral)
                self.updatePVs()

    def write(self, reason, value):

        return (False)


def time_sec(timeBuffer):
    deltatime = (timeBuffer[-1] - timeBuffer[-2]).total_seconds()
    return deltatime


def integral_transitoria(buffer, deltatimeBuffer):
    return (((buffer[-1] + buffer[-2]) * deltatimeBuffer[-1]) / (2 * 3600))


def integral_permanente(buffer, deltatimeBuffer, x):
    i = x
    integral = 0
    while (i < sample):
        integral += (((buffer[i] + buffer[i + 1]) * deltatimeBuffer[i]) / (2 * 3600))
        i += 1
    return integral


else_gamma = PV('RAD:ELSE:Gamma')
else_neutron = PV('RAD:ELSE:Neutron')
else_total = PV('RAD:ELSE:TotalDoseRate')
thermo_gamma = PV('RAD:THERMO:Gamma')
thermo_neutron = PV('RAD:THERMO:Neutron')
thermo_total = PV('RAD:THERMO:TotalDoseRate')
berthold_gamma = PV('RAD:Berthold:Gamma')
berthold_neutron = PV('RAD:Berthold:TotalNeutronRate')
berthold_total = PV('RAD:Berthold:TotalDoseRate')

sample = 14400
timeBuffer = [datetime.datetime.utcnow()] * sample
deltatimeBuffer = [0] * sample
else_gammaBuffer = [0.0] * sample
else_neutronBuffer = [0.0] * sample
else_dataBuffer = [0.0] * sample
thermo_gammaBuffer = [0.0] * sample
thermo_neutronBuffer = [0.0] * sample
thermo_dataBuffer = [0.0] * sample
berthold_gammaBuffer = [0.0] * sample
berthold_neutronBuffer = [0.0] * sample
berthold_dataBuffer = [0.0] * sample
else_integralgamma = 0.0
else_integralneutron = 0.0
else_integral = 0.0
thermo_integralgamma = 0.0
thermo_integralneutron = 0.0
thermo_integral = 0.0
berthold_integralgamma = 0.0
berthold_integralneutron = 0.0
berthold_integral = 0.0
deltatime = 0.0
j = 0
x = 0

if (__name__ == '__main__'):
    PVs = {}
    PVs["RAD:ELSE:IntegralGamma"] = {"prec": 3, "type": "float", "unit": "uSv"}
    PVs["RAD:ELSE:IntegralNeutron"] = {"prec": 3, "type": "float", "unit": "uSv"}
    PVs["RAD:ELSE:DoseIntegral"] = {"prec": 3, "type": "float", "unit": "uSv"}
    PVs["RAD:THERMO:IntegralGamma"] = {"prec": 3, "type": "float", "unit": "uSv"}
    PVs["RAD:THERMO:IntegralNeutron"] = {"prec": 3, "type": "float", "unit": "uSv"}
    PVs["RAD:THERMO:DoseIntegral"] = {"prec": 3, "type": "float", "unit": "uSv"}
    PVs["RAD:Berthold:IntegralGamma"] = {"prec": 3, "type": "float", "unit": "uSv"}
    PVs["RAD:Berthold:IntegralNeutron"] = {"prec": 3, "type": "float", "unit": "uSv"}
    PVs["RAD:Berthold:DoseIntegral"] = {"prec": 3, "type": "float", "unit": "uSv"}

    CAserver = SimpleServer()
    CAserver.createPV("", PVs)
    driver = IntegralDriver()

    while (1):
        try:
            time.sleep(1)

            else_gammaBuffer.append(else_gamma.value)
            else_neutronBuffer.append(else_neutron.value)
            else_dataBuffer.append(else_total.value)
            thermo_gammaBuffer.append(thermo_gamma.value)
            thermo_neutronBuffer.append(thermo_neutron.value)
            thermo_dataBuffer.append(thermo_total.value)
            berthold_gammaBuffer.append(berthold_gamma.value)
            berthold_neutronBuffer.append(berthold_neutron.value)
            berthold_dataBuffer.append(berthold_total.value)

            timeBuffer.append(datetime.datetime.utcnow())
            deltatime = time_sec(timeBuffer)
            deltatimeBuffer.append(deltatime)

            else_integralgamma += integral_transitoria(else_gammaBuffer, deltatimeBuffer)
            else_integralneutron += integral_transitoria(else_neutronBuffer, deltatimeBuffer)
            else_integral += integral_transitoria(else_dataBuffer, deltatimeBuffer)
            thermo_integralgamma += integral_transitoria(thermo_gammaBuffer, deltatimeBuffer)
            thermo_integralneutron += integral_transitoria(thermo_neutronBuffer, deltatimeBuffer)
            thermo_integral += integral_transitoria(thermo_dataBuffer, deltatimeBuffer)
            berthold_integralgamma += integral_transitoria(berthold_gammaBuffer, deltatimeBuffer)
            berthold_integralneutron += integral_transitoria(berthold_neutronBuffer, deltatimeBuffer)
            berthold_integral += integral_transitoria(berthold_dataBuffer, deltatimeBuffer)

            #print ('TimeStamp:                {}'.format(timeBuffer[-1]))
            #print ('Deltatime:                {}'.format(deltatimeBuffer[-1]))
            #print ('Else Integral antes:      {}'.format(else_integral))
            #print ('Thermo Integral antes:    {}'.format(thermo_integral))
            #print ('Berthold Integral antes:  {}'.format(berthold_integral))
            #print ('\n')

            x = 0
            j = 0

            while (j <= sample):
                if (timeBuffer[-1] - timeBuffer[j]).total_seconds() >= float(sample):
                    x += 1
                else:
                    pass
                j += 1

            if x >= 1:
                else_integralgamma = integral_permanente(else_gammaBuffer, deltatimeBuffer, x)
                else_integralneutron = integral_permanente(else_neutronBuffer, deltatimeBuffer, x)
                else_integral = integral_permanente(else_dataBuffer, deltatimeBuffer, x)
                thermo_integralgamma = integral_permanente(thermo_gammaBuffer, deltatimeBuffer, x)
                thermo_integralneutron = integral_permanente(thermo_neutronBuffer, deltatimeBuffer, x)
                thermo_integral = integral_permanente(thermo_dataBuffer, deltatimeBuffer, x)
                berthold_integralgamma = integral_permanente(berthold_gammaBuffer, deltatimeBuffer, x)
                berthold_integralneutron = integral_permanente(berthold_neutronBuffer, deltatimeBuffer, x)
                berthold_integral = integral_permanente(berthold_dataBuffer, deltatimeBuffer, x)

            #print('Else Integral Depois:     {}   it = {}'.format(else_integral, x))
            #print('Thermo Integral Depois:   {}   it = {}'.format(thermo_integral, x))
            #print('Berthold Integral Depois: {}   it = {}'.format(berthold_integral, x))
            #print('==================================================\n')

            if len(else_gammaBuffer) > sample:
                else_gammaBuffer = else_gammaBuffer[1:]
            if len(else_neutronBuffer) > sample:
                else_neutronBuffer = else_neutronBuffer[1:]
            if len(else_dataBuffer) > sample:
                else_dataBuffer = else_dataBuffer[1:]
            if len(thermo_gammaBuffer) > sample:
                thermo_gammaBuffer = thermo_gammaBuffer[1:]
            if len(thermo_neutronBuffer) > sample:
                thermo_neutronBuffer = thermo_neutronBuffer[1:]
            if len(thermo_dataBuffer) > sample:
                thermo_dataBuffer = thermo_dataBuffer[1:]
            if len(berthold_gammaBuffer) > sample:
                berthold_gammaBuffer = berthold_gammaBuffer[1:]
            if len(berthold_neutronBuffer) > sample:
                berthold_neutronBuffer = berthold_neutronBuffer[1:]
            if len(berthold_dataBuffer) > sample:
                berthold_dataBuffer = berthold_dataBuffer[1:]
            if len(timeBuffer) > sample:
                timeBuffer = timeBuffer[1:]
            if len(deltatimeBuffer) > sample:
                deltatimeBuffer = deltatimeBuffer[1:]

            CAserver.process(0.1)

        except Exception as e:
            print(e)
            pass
