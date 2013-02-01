#!/usr/bin/env python

from datetime import datetime

now = str(datetime.now())
#print now



with open("output.txt", "a") as myfile:
    myfile.write(now + " appended text \n")



