# Mach1py

Python file parser for biomomentum Mach-1 data files

## Overview

Mach1py is a file parser for data files generated using the Mach-1 Motion software for controlling Biomomentum Mach-1 mechanical testers.  File information is read into a dictionary and file data is read into a pandas dataframe.

## Installation

Download or clone the repository to your local machine.  In terminal, navigate to the repository location on your local machine and run local install using pip:

```
pip install .
```
or 
```
python -m pip install .
```

## Example script

``` python

from mach1py import mach1file

#load data from file
df = mach1file("/path/to/file.txt")

#check action type
print(df.info["Action"])

#check run date
print(df.info["Date"])

#check move velocity
print(df.info["Velocity, mm/s"])

#print file data
print(df.data)

#save file data to csv
df.data.to_csv("/output/path.csv")

```

## Mach1file object

**Arguments**
|      Name      |      Data Type      |     Description     |
|------|-----------|-------------|
|file_path | str | Location of Mach-1 text file to load | 

**Attributes**

|      Name      |      Data Type      |     Description     |
|------|-----------|-------------|
| info | dict | Dictionary of name/value pairs with all data in the info and function information blocks. |
| data | pandas.DataFrame | Numerical data from Data file section |