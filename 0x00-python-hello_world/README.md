#0x00-python-hello_world

|                  File                       |                     Description                     |
| :-----------------------------------------: |  :-----------------------------------------------:  |
|        0-run                        |   Shell script that runs a Python script. |
|        1-isdigit.c                  |   Shell script that runs Python code. |
|        2-print.py                   |   Python script that prints exactly ```"Programming is like a building a multilingual puzzle```  |
|        3-print_number.py            |   Python script that prints out an integer and a string. |
|        4-print_float.py             |   Python script that prints a float stored in a variable called number. |
|        5-print_string.py            |   Python script that prints out a string a number of times  |
|        6-concat.py                  |   Python script that concatenates two variables that hold two different strings and makes one single variable that prints the string to standard out.  |
|        7-edges.py                   |   Python script that concatenate variables that store parts of the whole string.  |
|        8-concat_edges.py            |   Python script that changes the string that is to be printed.  |
|        9-easter_egg.py              |   Python Easter Egg with import this.  |
|        100-write.py                 |   Python script that prints exactly ```and that piece of art is useful - Dora Korpar, 2015-10-19``` followed by a new line.
|        101-compile                  |  Python script that creates a .pyc that is modified to a specific format when ran with od -t x1 main.pyc |
|        102-magic_calculation.py     |  Python script that breaks the file down into Python Byte code.  |
##Examples:

####2-print.py
```
waltonlee$ ./2-print.py
"Programming is like building a multilingual puzzle
waltonlee$ 
```
####6-concat.py
```
waltonlee$ ./6-concat.py
Welcome to Holberton School!
waltonlee$ wc -l 6-concat.py
5 6-concat.py
waltonlee$ 
```
####102-magic_calculation.py
```
When using the python3 terminal:
  2           0 LOAD_CONST               1 (98)
              3 LOAD_FAST                0 (a)
              6 LOAD_FAST                1 (b)
              9 BINARY_POWER
             10 BINARY_ADD
             11 RETURN_VALUE
```
