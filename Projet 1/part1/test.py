#! /usr/bin/python
#from random import randint

i = 0
while i < 10000000:
	print i, "of 10000000                 \r",
	i += 1
print ""



"""def change_bit(N, l):
	tmp = N
	for pos in l :
		if pos == -1:
			continue
		old_bit = tmp & 2**pos
		if old_bit :
			tmp -= 2**pos
		else:
			tmp += 2**pos
	return tmp

i = 0
while i < 20:
	n = randint(2**7, 2**8)
	l = []
	while len(l) != 3:
		x = randint(0, 7)
		if x not in l:
			l.append(x)
	c = bin(change_bit(n, l))[2:]
	print "76543210"
	print bin(n)[2:]
	print "0"*(8-len(c))+c, l
	i += 1 

from time import time
L = [5, 1, 0, 2, 5, 3, 5, 0, 1, 0, 1, 5, 1, 5, 0, 0, 5, 5, 0, 2, 0, 0, 0, 5, 2, 0, 1, 0, 4, 5, 5, 5, 0, 4, 5, 5, 4, 4, 5, 5, 0, 5, 5, 3, 4, 5, 0, 0, 5, 4, 2, 5, 5, 4, 2, 0, 1, 0, 0, 5, 0, 0, 0, 5, 1, 0, 4, 4, 5, 4, 5, 4, 1, 0, 4, 4, 5, 0, 4, 0, 0, 0, 5, 1, 0, 5, 0, 1, 4, 0, 5, 4, 1, 3, 1, 0, 0, 5, 4, 5, 0, 0, 4, 5, 5, 5, 4, 4, 1, 5, 1, 1, 1, 4, 5, 0, 5, 0, 0, 0, 5, 0, 5, 5, 4, 1, 0, 5, 0, 5, 5, 0, 4, 5, 3, 1, 0, 5, 2, 0, 1, 4, 0, 1, 0, 0, 0, 1, 5, 5, 4, 4, 1, 0, 2, 4, 4, 3, 5, 0, 5, 4, 1, 5, 0, 0, 5, 1, 0, 5, 1, 5, 1, 5, 5, 0, 5, 4, 0, 1, 5, 0, 1, 4, 1, 5, 0, 0, 4, 4, 5, 4, 4, 0, 0, 5, 1, 4, 5, 0, 0, 1, 4, 3, 5, 4, 0, 1, 0, 0, 5, 5, 0, 1, 1, 2, 1, 0, 0, 1, 1, 0, 2, 5, 3, 0, 5, 0, 0, 1, 5, 0, 4, 3, 0, 0, 1, 5, 4, 1, 3, 0, 0, 0, 5, 4, 0, 1, 0, 0, 3, 2, 0, 5, 5, 0, 0, 5, 0, 0, 0, 4, 4]
i = 0
l = len(L)
pos = [-1, -1, -1]
t = time()
while i < (l+1)**3:
	i_0 = i % l
	i_1 = (i/l)%l
	i_2 = (i/l)/l
	if L[i_0] == 0 or L[i_0] == 5:
		i += 1
		continue
	if (L[i_1] == 0 or L[i_1] == 5):
		i += l
		continue
	if L[i_2] == 0 or L[i_2] == 5:
		i += l**2
		continue
	print L[i_0], L[i_1], L[i_2]
	i += 1
print time() - t
"""