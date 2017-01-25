#0x08-python-more_classes


|                  File                                    |                     Description                     |
| :-----------------------------------------: |  :-----------------------------------------------:  |
|        0-rectangle.py                        | Writing an empty class defining a rectangle. |
|        1-rectangle.py                        | Updating 0-rectangle to include private instance attributes height and width and instantiating them.  |
|        2-rectangle.py               | Updating 1-rectangle to include an area and perimeter public instance methods. |
|        3-rectangle.py               | Updating 2-rectangle to being able to print out the # character with print and str. |
|        4-rectangle.py               | Updating 3-rectangle to be able to return the string using repr() and eval().  |
|        5-rectangle.py               | Updating 4-rectangle to be able to catch the del function and print out a statement after deleting the instance.  |
|        6-rectangle.py               | Updating 5-rectangle to include incrementing and decrementing number_of_instances with each new instantiation.  |
|        7-rectangle.py               | Updating 6-rectangle to print other characters besides #.  |
|        8-rectangle.py               | Updating 7-rectangle to include a static method and comparing the size of the rectangle.  |
|        9-rectangle.c                |  Updating 8-rectangle to include a class method that returns a new rectangle.  |

##Example:

####3-rectangle.py
```
waltonlee$ ./3-main.py
Area: 8 - Perimeter: 12
##
##
##
##
<3-rectangle.Rectangle object at 0x7f92a75a2eb8>
--
##########
##########
##########
<3-rectangle.Rectangle object at 0x7f92a75a2eb8>
waltonlee$
```
####7-print_last_digit.c
```
waltonlee$ cat 6-main.py
#!/usr/bin/python3
Rectangle = __import__('6-rectangle').Rectangle

my_rectangle_1 = Rectangle(2, 4)
my_rectangle_2 = Rectangle(2, 4)
print("{:d} instances of Rectangle".format(Rectangle.number_of_instances))
del my_rectangle_1
print("{:d} instances of Rectangle".format(Rectangle.number_of_instances))
del my_rectangle_2
print("{:d} instances of Rectangle".format(Rectangle.number_of_instances))

waltonlee$ ./6-main.py
2 instances of Rectangle
Bye rectangle...
1 instances of Rectangle
Bye rectangle...
0 instances of Rectangle
waltonlee$
```