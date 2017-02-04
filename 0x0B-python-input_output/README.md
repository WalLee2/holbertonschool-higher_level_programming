#0x0B-python-input_output

|                  File                                    |                     Description                     |
| :-----------------------------------------: |  :-----------------------------------------------:  |
|        0-read_file.py                      |  Reading a text file in UTF-8 and print to standard out.   |
|        1-number_of_lines.py                |  Returning the number of lines of a text file.   |
|        2-read_lines.py                     |  Reading "n" lines of a text file in UTF-8 format and printing it to standard out.   |
|        3-write_file.py                     |  Write a string to a text file in UTF-8 and returning the number of  characters.   |
|        4-append_write.py                   |  Appending a string at the end of a text file in UTF-8 format and return the number of characters.   |
|        5-to_json_string.py                 |  Return a JSON representation of a string object.   |
|        6-from_json_string.py               |  Return an object represented by a JSON string.   |
|        7-save_to_json_file.py              |  Writing an object to a text file using JSON representation.   |
|        8-load_from_json_file.py            | Create an object from a JSON file. |
|        9-add_item.py                       | Add all arguments to a Python list and save it to a file. |


##Example:

####4-append_write.py
```
waltonlee$ cat 4-main.py
#!/usr/bin/python3
append_write = __import__('4-append_write').append_write

nb_characters_added = append_write("file_append.txt", "Holberton School is so cool!\n")
print(nb_characters_added)
waltonlee$ cat file_append.txt
cat: file_append.txt: No such file or directory
waltonlee$ ./4-main.py
29
waltonlee$ cat file_append.txt
Holberton School is so cool!
waltonlee$ ./4-main.py
29
waltonlee$ cat file_append.txt
Holberton School is so cool!
Holberton School is so cool!
waltonlee$ 

```
####8-load_from_json_file.py
```
waltonlee$ cat my_fake.json
{"is_active": true, 12 }
waltonlee$ cat 8-main.py
#!/usr/bin/python3
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

filename = "my_list.json"
my_list = load_from_json_file(filename)
print(my_list)
print(type(my_list))

filename = "my_dict.json"
my_dict = load_from_json_file(filename)
print(my_dict)
print(type(my_dict))

try:
    filename = "my_set_doesnt_exist.json"
    my_set = load_from_json_file(filename)
    print(my_set)
    print(type(my_set))
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    filename = "my_fake.json"
    my_fake = load_from_json_file(filename)
    print(my_fake)
    print(type(my_fake))
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

waltonlee$ cat my_list.json ; echo ""
[1, 2, 3]
waltonlee$ cat my_dict.json ; echo ""
{"name": "John", "places": ["San Francisco", "Tokyo"], "id": 12, "info": {"average": 3.14, "age": 36}, "is_active": true}
<class 'dict'>
[FileNotFoundError] [Errno 2] No such file or directory: 'my_set_doesnt_exist.json'
[FileNotFoundError] [Errno 2] No such file or directory: 'my_fake.json']
waltonlee$ 
```
