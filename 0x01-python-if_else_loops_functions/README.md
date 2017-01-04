#0x01-python-if_else_loops_functions

|                  File                       |                     Description                     |
| :-----------------------------------------: |  :-----------------------------------------------:  |
|          0-positive_or_negative.py   |  Script that prints out a random number and also outputs: ```is negative```, ```is zero```, or ```is positive```. |
|        1-last_digit.py         |   Script that prints out the last number of a 4 digit number and also prints out a specific string depending on whether the number is positive, negative, or zero. |
|        2-print_alphabet.py        |   Script that prints the alphabet.  |
|       3-print_alphabt.py          |   Script that prints out the alphabet without the letters: ```q``` and ```e```. |
|        4-print_hexa.py          |   Script that prints all numbers from 0 to 98 in decimal and hexadecimal.  |
|        5-print_comb2.py         |   Script that prints numbers from 0 to 99 with a space and comma at the end except on the last number.  |
|        6-print_comb3.py         |   Script that prints all possible unique combinations of two digits.  |
|        7-islower.py             |   Function that checks for lowercase characters and prints out the character and if the character is in uppercase or lowercase.  |
|        8-uppercase.py               |   Function that prints a string in uppercase followed by a new line.  |
|        9-print_last_digit.py        |   Function that prints the last digit of a number.  |
|        10-add.py                  |    Function that adds two integers and returns the result.  |
|        11-pow.py        |   Function that takes the power of two numbers ```a``` and ```b```.  |
|        12-fizzbuzz.py       |   Function that prints FizzBuzz if evenly divisible by 3 and 5, prints Fizz if only divisible by 3, Buzz if only divisible by 5, otherwise the number will be printed if none of those apply.  |
|        100-print_tebahpla.py        |   Script that prints the alphabet in reverse order with alternating lower and uppercase characters starting with z as a lowercase and Y as an uppercase.  |
|        101-remove_char_at.py        |   Function that creates a copy of the string, removing the character at the position n.  |
|        102-magic_calculation.py        |   Python function that results in a very specific bytecode when dis.dis is ran.  |
##Example:

####6-print_comb3.py
```
waltonlee$ chmod u+x 6-print_comb3.py
waltonlee$ ./6-print_comb3.py
01, 02, 03, 04, 05, 06, 07, 08, 09, 12, 13, 14, 15, 16, 17, 18, 19, 23, 24, 25, 26, 27, 28, 29, 34, 35, 36, 37, 38, 39, 45, 46, 47, 48, 49, 56, 57, 58, 59, 67, 68, 69, 78, 79, 89
waltonlee$ 
```
####12-main.py
```
waltonlee$ chmod u+x 12-main.py
waltonlee$ chmod u+x 12-fizzbuzz.py
waltonlee$ ./12-main.py | cat -e
1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz 16 17 Fizz 19 Buzz Fizz 22 23 Fizz Buzz 26 Fizz 28 29 FizzBuzz 31 32 Fizz 34 Buzz Fizz 37 38 Fizz Buzz 41 Fizz 43 44 FizzBuzz 46 47 Fizz 49 Buzz Fizz 52 53 Fizz Buzz 56 Fizz 58 59 FizzBuzz 61 62 Fizz 64 Buzz Fizz 67 68 Fizz Buzz 71 Fizz 73 74 FizzBuzz 76 77 Fizz 79 Buzz Fizz 82 83 Fizz Buzz 86 Fizz 88 89 FizzBuzz 91 92 Fizz 94 Buzz Fizz 97 98 Fizz Buzz $
waltonlee$ 
```
####101-remove_char_at.py
```
waltonlee$ chmod u+x 101-remove_char_at.py
waltonlee$ chmod u+x 101-main.py
waltonlee$ cat 101-main.py
#!/usr/bin/env python3
remove_char_at = __import__('101-remove_char_at').remove_char_at

print(remove_char_at("Holberton School", 3))
print(remove_char_at("Chicago", 2))
print(remove_char_at("C is fun!", 0))
print(remove_char_at("School", 10))
print(remove_char_at("Python", -2))

waltonlee$ ./101-main.py
Holerton School
Chcago
 is fun!
School
Python
waltonlee$ 
```
