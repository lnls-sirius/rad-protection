#!/bin/bash

export PATH=/root/base-3.15.5/bin/linux-arm:$PATH
export EPICS_BASE="/root/base-3.15.5"
export EPICS_HOST_ARCH="linux-arm"
export EPICS_CA_MAX_ARRAY_BYTES=1048576

export PYEPICS_LIBCA=/root/base-3.15.5/lib/linux-arm/libca.so

EPICS_CAS_SERVER_PORT=5199 /usr/bin/python /root/rad-integral/IntegralFinalVersion.py &

