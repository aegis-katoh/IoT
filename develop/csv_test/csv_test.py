# This program is written in Python3

from csv import writer
from os import path
from datetime import datetime

t1 = datetime.now()
f1 = open("huge.csv", "a")
t2 = datetime.now()
writer1 = writer(f1)
t3 = datetime.now()
f1.close()
t4 = datetime.now()

t5 = datetime.now()
f2 = open("test.csv", "a")
t6 = datetime.now()
writer2 = writer(f2)
t7 = datetime.now()
f2.close()
t8 = datetime.now()

print("open huge.csv", t2 - t1)
print("writer", t3 - t2)
print("close f1", t4 - t3)
print("open test.csv", t6 - t5)
print("writer", t7 - t6)
print("close f2", t8 - t7)
