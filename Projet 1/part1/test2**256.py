#! /usr/bin/python
from time import time

i = 0
t = time()
while i < 2**256:
	i += 1
	print len(bin(i))-2, "                           \r",
print ""
print time() - t