# Sirius Radiological Protection Software Supervisory 

## Alpha version – under development 

### Introduction

This page will contain documentation about the EPICS IOC for radiation protection equipments at Sirius building.

Three radiation monitoring systems (from different manufacturers) were bought for evaluation. [[CON:CON|Controls group]] is working on remote interfaces for these equipments. They will be tested during Sirius [https://wiki-sirius.lnls.br/mediawiki/index.php/Machine:Linac_parameters Linac] comissioning (scheduled to start in March 2018).

### Project description

The supervisory was developed with the purpose of performing the radiological area  monitoring in the Sirius facilities. The supervisor is easy to see and to interpret the data. The system compares the reading of different probes in different regions. Each device performs dose readings in uSv / h.

On the main frame of the supervisory we have an overview of all the PV's in two dynamic screens. The readings are performed by the following probes:

 >> [https://www.elsenuclear.com/en Else Nuclear] - Saturn II 5702 containing an ICP-T-PF gamma detector and a LUPIN 5401 BF3-NP neutron detector;
 >> [https://www.thermofisher.com/br/en/home.html ThermoFisher Scientific] - FHT 6020 containing a FHT 192-10 gamma detector and a FHT 762 neutron detector;
 >> [https://www.berthold.com/ Berthold Technologies] - LB 6420 Dose Meter For Measuring Pulsed Radiation.

The name of the PV consists of RAD, symbolizing the domain of the radiation protection department, followed by the name of the detector manufacturer and, finally, the variable addressed. Gamma radiation dose, neutron dose and total dose (sum of neutron dose  and gamma dose) and integrated dose in 4h are performed. Two lines were inserted into the graphs representing the limit for the integrated dose (2uSv) and the mean value for the background.

All PV names are listed below:

 >> RAD:ELSE:DoseIntegral
 >> RAD:THERMO:DoseIntegral
 >> RAD:Berthold:IntegralRate
 >> RAD:ELSE:Gamma
 >> RAD:ELSE:Neutron
 >> RAD:ELSE:TotalDoseRate
 >> RAD:THERMO:Gamma
 >> RAD:THERMO:Neutron
 >> RAD:THERMO:TotalDoseRate
 >> RAD:Berthold:Gamma
 >> RAD:Berthold:TotalNeutronRate
 >> RAD:Berthold:TotalDoseRate
 >> RAD:Berthold:HighEnergyNeutrons

Ps.: The Berthold probe, in addition to the cited PVs, there is a dose measurement due to fast neutrons displayed on the second screen (RAD:Berthold:HighEnergyNeutrons).

In the second frame on the main frame of the supervisory we see a graph containing lines with the values of the instantaneous dose measurements in uSv / h as a function of time. The first frame contains the readings of the PVs related to the integrated doses in 4h. The integrated dose is the dose that has been achieved within the last four hours, obtained by the trapezoidal method that makes use of the instantaneous measurement and time difference for the calculation.

There are interactive buttons and a legend relating the name of the PV, its value read instantly and the color of the line referring to that PV on the main frame. The buttons allow to open in a new frame the enlargement of each frame for better visualization, opening of a WEB page directed to the ‘Archiver EPICS’ and the access to a configuration menu. The new frames have a button to came back to main frame.

### Download

The software can be downloaded through [https://github.com/lnls-sirius/rad-protection GitHub] and only need to be downloaded and run with [https://github.com/ControlSystemStudio/cs-studio/wiki Control System Studio] is a graphical tool based on [http://www.eclipse.org/ Eclipse] which offers many features to monitor and to operate controls systems, being maintained continuously and improved by developers from many laboratories and teaching institutes. Between the projects contained in the [https://github.com/ControlSystemStudio CSS repository], one of the them allows the generation of local and customised distributions according to the needs of the respective laboratory. This project, called [https://github.com/ControlSystemStudio/org.csstudio.product org.csstudio.product], was, therefore, extended and modified to meet only our group's needs.

For more information see the [https://wiki-sirius.lnls.br/mediawiki/index.php/CON:Lnls-studio Control System Studio] page on the [https://wiki-sirius.lnls.br/ Wiki-Sirius]

Inquieries: aureo.carneiro@lnls.br
