# cap-calculator
CLI program written in Python to calculate Cumulative Average Point (CAP) of a student of National University of Singapore (NUS)

## Usage
```
cap.py [-h] [-f [FILE]]

optional arguments:
    -h, --help            show this help message and exit
    -f [FILE], --file [FILE]
                          read grades from FILE
```
When run without options, the user will be asked to enter the results, in the form of grades,MCs; if omitted, the MCs will be assumed to be 4. ```Ctrl+C``` can be used to terminate input and proceed to calculate and display CAP. When ```-f``` or ```--file``` is used alongwith a filepath to a CSV or a filename, the program will attempt to read from the file. If the option is used without any filepath or filename, the programs searches the user's working directory for CSVs and allows the user to choose which CSV to read from, if any. Following is an example of user input/CSV file:
### From CSV
For each module, type its grade and MCs in the same line, separated by a comma; if omitted, the MCs will be assumed to be 4. Any number of blank lines can be left between modules. Following is an example of a CSV file that can be used as input:
```
B+,6
B+,
B
A-
B-,2
B,2

A,6
B
B+
B
```
