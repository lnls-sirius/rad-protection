#!/usr/bin/python
# -*- coding: utf-8 -*-

# sirius-linac-radiation-interlock.py

# Simple script which provides a signal related to the radiation meters to Sirius Linac interlock
# system.

# Python modules required: Adafruit-BBIO and pyepics.
# Tested with Python 2.7.13, Adafruit-BBIO 1.0.10 and pyepics 3.3.1.

# Necessary modules

from epics import PV
import Adafruit_BBIO.GPIO as GPIO
import sys
import time

# Configuration of the BeagleBone Black pin used to open or close the relay contact

GPIO.setup("P9_14", GPIO.OUT)
GPIO.output("P9_14", GPIO.HIGH)

# These are the EPICS PVs that should be observed by this program

PV1 = PV("RAD:Berthold:Int")
PV2 = PV("RAD:ELSE:DoseIntegral")
PV3 = PV("RAD:THERMO:DoseIntegral")

# The radiation dose limit (in uSv) is an argument of the program

dose_limit = float(sys.argv[1])

# Loop

while (True):

    try:

        # If any of the three radiation measurements exceeded the limit, the program opens the
        # relay contact. If this is not the case, the relay contact is kept closed.

        if ((PV1.value >= dose_limit) or (PV2.value >= dose_limit) or (PV3.value >= dose_limit)):
            GPIO.output("P9_14", GPIO.LOW)
        else:
            GPIO.output("P9_14", GPIO.HIGH)

        time.sleep(0.5)

    except (Exception):

        pass
