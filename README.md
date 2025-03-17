# adif2callhistory

[![PyPI](https://img.shields.io/pypi/v/adif2callhistory)](https://pypi.org/project/adif2callhistory/)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Python: 3.10+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Made With:PyQt6](https://img.shields.io/badge/Made%20with-PyQt6-blue)](https://pypi.org/project/PyQt6/)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/adif2callhistory)](https://pypi.org/project/adif2callhistory/)

This package allows you to load an arbitrary ADIF file and map the ADIF tags to N1MM or Not1MM call history file fields.
After selecting the fields you wished to export, simply save the file under the name you give it.

![main screen](https://github.com/mbridak/adif2callhistory/blob/main/pic/adif2callhistory_initial.png?raw=true)

## Installation

This Python package is hosted on PyPi. It can be installed with pipx, `pipx install adif2callhistory` or you can use uv.

## Selecting/loading an ADIF file

Click `File -> Load ADIF` I file picker will appear allowing you to select the file. If the file is parsed correctly the drop downs next to the call history field names will populate with the unique ADIF tags found.

One thing that will prevent an ADIF file from parsing is if the ADIF header does not start with a comment line.

So if your ADIF file looks like:

```text
<ADIF_VER:5>2.2.0
<EOH>
<QSO_DATE:8:d>20220625
<TIME_ON:4>1806
```

Just add a line to the top like:

```text
Some Text Here
<ADIF_VER:5>2.2.0
<EOH>
<QSO_DATE:8:d>20220625
<TIME_ON:4>1806
```

and retry it.

## Mapping the fields to tags and saving the file

After the ADIF file is loaded and the drop downs are populated with tags, go down the list of fields, place a checkmark to the left of the desired field and select which tag to map to it.

Here's an example of fields selected and mapped to a Field Day ADIF file:

![mapped fields](https://github.com/mbridak/adif2callhistory/blob/main/pic/adif2callhistory_select_fields.png?raw=true)

After selecting and mapping the fields select `File -> Save Call History` and choose a filename and location to save your file.

You will end up with something like:

```text
!!Order!!,Call,Name,Loc1,Sect,State,Exch1
K6PV,,,LAX,CA,1D
K7SS,DANIEL A ESKENAZI,CN87tn,WWA,WA,1D
K6AA,UNITED RADIO AMATEUR CLUB INC,DM03ur,LAX,CA,3A
K0EU,RANDALL K MARTIN,DM79lp,CO,CO,1B
W3AO,NATIONAL PRESS RADIO CLUB,FM18pv,MDC,MD,1E
W6ZE,ORANGE COUNTY AMATEUR RADIO CLUB INC,DM13cs,ORG,CA,6A
...
```

## Recent Changes

- [25-3-17] Define newline in file open command incase windows user happens to run it.
- [25-3-15] Bumped pyadif-file requirement to 1.3.1
- [25-3-10] Initial push.

## Copyright

PyADIF-File © 2023-2024 by Andreas Schawo is licensed under [CC BY-SA 4.0](http://creativecommons.org/licenses/by-sa/4.0/)

PyADIF-File uses

xmlschema Copyright (c), 2016-2022, SISSA (Scuola Internazionale Superiore di Studi Avanzati)

xmltodict Copyright (c), 2012 Martin Blech and individual contributors