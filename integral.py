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
                self.setParam("RAD:ELSE:IntGamma", else_integralgamma)
                self.setParam("RAD:ELSE:IntNeutron", else_integralneutron)
                self.setParam("RAD:ELSE:Int", else_integral)
                self.setParam("RAD:THERMO:IntGamma", thermo_integralgamma)
                self.setParam("RAD:THERMO:IntNeutron", thermo_integralneutron)
                self.setParam("RAD:THERMO:Int", thermo_integral)
                self.setParam("RAD:Berthold:IntGamma", berthold_integralgamma)
                self.setParam("RAD:Berthold:IntNeutron", berthold_integralneutron)
                self.setParam("RAD:Berthold:Int", berthold_integral)
                self.updatePVs()

    def write(self, reason, value):

        return (False)


def time_sec(timeBuffer):
    deltatime = (timeBuffer[-1] - timeBuffer[-2]).total_seconds()
    return deltatime


def integral_transitoria(buffer, deltatimeBuffer):
    return (((buffer[-1] + buffer[-2]) * deltatimeBuffer[-1]) / (2 * 3600))


def integral_permanente(buffer, deltatimeBuffer, j):
    return ((((buffer[-1] + buffer[-2]) * deltatimeBuffer[-1]) - ((buffer[j] + buffer[j + 1]) * deltatimeBuffer[j])) / (
            2 * 3600))


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

if (__name__ == '__main__'):
    PVs = {}
    PVs["RAD:ELSE:IntGamma"] = {"prec": 3, "type": "float", "unit": "uSv"}
    PVs["RAD:ELSE:IntNeutron"] = {"prec": 3, "type": "float", "unit": "uSv"}
    PVs["RAD:ELSE:Int"] = {"prec": 3, "type": "float", "unit": "uSv"}
    PVs["RAD:THERMO:IntGamma"] = {"prec": 3, "type": "float", "unit": "uSv"}
    PVs["RAD:THERMO:IntNeutron"] = {"prec": 3, "type": "float", "unit": "uSv"}
    PVs["RAD:THERMO:Int"] = {"prec": 3, "type": "float", "unit": "uSv"}
    PVs["RAD:Berthold:IntGamma"] = {"prec": 3, "type": "float", "unit": "uSv"}
    PVs["RAD:Berthold:IntNeutron"] = {"prec": 3, "type": "float", "unit": "uSv"}
    PVs["RAD:Berthold:Int"] = {"prec": 3, "type": "float", "unit": "uSv"}

    CAserver = SimpleServer()
    CAserver.createPV("", PVs)
    driver = IntegralDriver()

    while (1):

        try:

            time.sleep(1)

            # armazenando as PVs no Buffer
            else_gammaBuffer.append(else_gamma.value)
            else_neutronBuffer.append(else_neutron.value)
            else_dataBuffer.append(else_total.value)
            thermo_gammaBuffer.append(thermo_gamma.value)
            thermo_neutronBuffer.append(thermo_neutron.value)
            thermo_dataBuffer.append(thermo_total.value)
            berthold_gammaBuffer.append(berthold_gamma.value)
            berthold_neutronBuffer.append(berthold_neutron.value)
            berthold_dataBuffer.append(berthold_total.value)

            # armazenando o timestamp
            timeBuffer.append(datetime.datetime.utcnow())
            if timeBuffer[-1] != 0 and timeBuffer[-2] != 0:
                deltatime = time_sec(timeBuffer)
                deltatimeBuffer.append(deltatime)

            # cauculando a integral
            if (timeBuffer[-1] - timeBuffer[j]).total_seconds() < sample:

                else_integralgamma += integral_transitoria(else_gammaBuffer, deltatimeBuffer)
                else_integralneutron += integral_transitoria(else_neutronBuffer, deltatimeBuffer)
                else_integral += integral_transitoria(else_dataBuffer, deltatimeBuffer)
                thermo_integralgamma += integral_transitoria(thermo_gammaBuffer, deltatimeBuffer)
                thermo_integralneutron += integral_transitoria(thermo_neutronBuffer, deltatimeBuffer)
                thermo_integral += integral_transitoria(thermo_dataBuffer, deltatimeBuffer)
                berthold_integralgamma += integral_transitoria(berthold_gammaBuffer, deltatimeBuffer)
                berthold_integralneutron += integral_transitoria(berthold_neutronBuffer, deltatimeBuffer)
                berthold_integral += integral_transitoria(berthold_dataBuffer, deltatimeBuffer)

            else:

                while (j <= sample):
                    else_integralgamma += integral_permanente(else_gammaBuffer, deltatimeBuffer, j)
                    else_integralneutron += integral_permanente(else_neutronBuffer, deltatimeBuffer, j)
                    else_integral += integral_permanente(else_dataBuffer, deltatimeBuffer, j)
                    thermo_integralgamma += integral_permanente(thermo_gammaBuffer, deltatimeBuffer, j)
                    thermo_integralneutron += integral_permanente(thermo_neutronBuffer, deltatimeBuffer, j)
                    thermo_integral += integral_permanente(thermo_dataBuffer, deltatimeBuffer, j)
                    berthold_integralgamma += integral_permanente(berthold_gammaBuffer, deltatimeBuffer, j)
                    berthold_integralneutron += integral_permanente(berthold_neutronBuffer, deltatimeBuffer, j)
                    berthold_integral += integral_permanente(berthold_dataBuffer, deltatimeBuffer, j)

                    j += 1
            j = 0

            # imprimindo para debug
            print("ELSE:     {} ".format(else_integral))
            print("THERMO:   {} ".format(thermo_integral))
            print("Berthold: {} ".format(berthold_integral))
            print("=========================== \n")

            # elimando elementos do Buffer circular
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
