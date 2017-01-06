#!/usr/bin/python3
import hidden_4
name = dir(hidden_4)
length = len(dir(hidden_4))
for i in range(0, length):
    if (name[i][:2] != "__"):
        print(name[i])
