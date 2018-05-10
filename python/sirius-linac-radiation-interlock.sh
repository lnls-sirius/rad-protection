#!/bin/bash

export PATH=/root/base-3.15.5/bin/linux-arm:$PATH
export EPICS_BASE="/root/base-3.15.5"
export EPICS_HOST_ARCH="linux-arm"
export EPICS_CA_MAX_ARRAY_BYTES=1048576
export EPICS_CA_ADDR_LIST=10.0.4.57
#export EPICS_CA_AUTO_ADDR_LIST=NO

export PYEPICS_LIBCA=/root/base-3.15.5/lib/linux-arm/libca.so

/usr/bin/python /root/sirius-linac-radiation-interlock.py 2 &
