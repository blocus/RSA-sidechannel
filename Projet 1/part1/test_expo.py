#! /usr/bin/python
from random import random, randint
from time import time
import Crypto.PublicKey.RSA as RSA

def squareAndMultiply(base,exponent,modulus):
	a = 1
	b = base
	while exponent != 0:
		if  exponent & 1:
			a = a * b % modulus
		b = b**2 % modulus
		exponent >>= 1
	return a

key = """-----BEGIN RSA PRIVATE KEY-----
MIGrAgEAAiEAwI4/FTS6LXcAIaOLhjnHBcadAMZ3vNX35LACPliSyYMCAwEAAQIh
AJv1WoC5gSX74X5dcU+ZEmliUeyy/ErzhYRnvb6HNrapAhEA5eLMWHodVcDGYydt
LzqwbwIRANZt3URtflIcmlULDbZRmi0CEE12820NGT2ATFm1O3Gi0TkCEQClapmA
GSuSsogIRP+t/yN9AhALZOxCmVTANv/VKIsSD9m0
-----END RSA PRIVATE KEY-----"""

key = RSA.importKey(key)

i = 0
t = time()
x = 0
while i < 2000000:
	r1 = randint(0, 2**10)
	r2 = randint(0, 2**10)
	if r1 == r2:
		x += 1
	#squareAndMultiply(message, key.d, key.n)
	i+= 1

print (time() - t)/ 2000000, time() - t, x