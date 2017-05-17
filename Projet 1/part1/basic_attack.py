#! /usr/bin/python
from random import random, randint
import Crypto.PublicKey.RSA as RSA
import Crypto.Util.number as number
from time import time
HAMMING = [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 4, 1, 2, 2, 3, 2, 3, 3, 4, 2, 3, 3, 4, 3, 4, 4, 5, 1, 2, 2, 3, 2, 3, 3, 4, 2, 3, 3, 4, 3, 4, 4, 5, 2, 3, 3, 4, 3, 4, 4, 5, 3, 4, 4, 5, 4, 5, 5, 6, 1, 2, 2, 3, 2, 3, 3, 4, 2, 3, 3, 4, 3, 4, 4, 5, 2, 3, 3, 4, 3, 4, 4, 5, 3, 4, 4, 5, 4, 5, 5, 6, 2, 3, 3, 4, 3, 4, 4, 5, 3, 4, 4, 5, 4, 5, 5, 6, 3, 4, 4, 5, 4, 5, 5, 6, 4, 5, 5, 6, 5, 6, 6, 7, 1, 2, 2, 3, 2, 3, 3, 4, 2, 3, 3, 4, 3, 4, 4, 5, 2, 3, 3, 4, 3, 4, 4, 5, 3, 4, 4, 5, 4, 5, 5, 6, 2, 3, 3, 4, 3, 4, 4, 5, 3, 4, 4, 5, 4, 5, 5, 6, 3, 4, 4, 5, 4, 5, 5, 6, 4, 5, 5, 6, 5, 6, 6, 7, 2, 3, 3, 4, 3, 4, 4, 5, 3, 4, 4, 5, 4, 5, 5, 6, 3, 4, 4, 5, 4, 5, 5, 6, 4, 5, 5, 6, 5, 6, 6, 7, 3, 4, 4, 5, 4, 5, 5, 6, 4, 5, 5, 6, 5, 6, 6, 7, 4, 5, 5, 6, 5, 6, 6, 7, 5, 6, 6, 7, 6, 7, 7, 8]
k = 256
key = RSA.generate(1024)
txt = """-----BEGIN RSA PRIVATE KEY-----
MIGrAgEAAiEAwI4/FTS6LXcAIaOLhjnHBcadAMZ3vNX35LACPliSyYMCAwEAAQIh
AJv1WoC5gSX74X5dcU+ZEmliUeyy/ErzhYRnvb6HNrapAhEA5eLMWHodVcDGYydt
LzqwbwIRANZt3URtflIcmlULDbZRmi0CEE12820NGT2ATFm1O3Gi0TkCEQClapmA
GSuSsogIRP+t/yN9AhALZOxCmVTANv/VKIsSD9m0
-----END RSA PRIVATE KEY-----"""
key = RSA.importKey(txt)
d = key.d
n = key.n
e = key.e
R = 10
y = (key.p -1 )*(key.q - 1)
eb = 0.05
t = 3
gama = 103

def gen_RSA_key(N):
	p = (N)
def change_bit(N, l):
	tmp = N
	for pos in l :
		if pos == -1:
			continue
		tmp ^= 2**pos
	return tmp


def squareAndMultiply(base,exponent,modulus):
	a = 1
	b = base
	while exponent != 0:
		if  exponent & 1:
			a = a * b % modulus
		b = b**2 % modulus
		exponent >>= 1
	return a

def ham_2(a):
	h = 0
	while a != 0:
		p = a & 0xff
		h += HAMMING[p]
		a >>= 8
	return h

def genV(key, rand):
	v = key.d + (rand * y)
	#v = d
	l = len(bin(v)) - 2
	i = 0
	while i < l:
		if random() < eb:
			v ^= 2**i
		i += 1
	return v

C = []
J = 0
s = 0
finish = 0
roun = 0
time_start = time()
while finish == 0:
	print '-'*10, roun, '-'*10
	roun += 1
	stop = 0
	while stop == 0:
		print J+1, "keys in", len(C), "classes                      \r",
		V = genV(key, randint(0, 2**R))
		if J == 0:
			s = 1
			C.append([V])
		else :
			m = 0
			found = 0
			while ((m < s) and (found == 0)):
				tmp = 1
				for v_condidat in C[m]:
					h = ham_2(V ^ v_condidat)
					if h > gama:
						tmp = 0
						break
				if tmp == 1:
					C[m].append(V)
					found = 1
					if len(C[m]) == t:
						w = m
						stop = 1
				m += 1
			if found == 0:
				s += 1
				C.append([V])
		J += 1
	print ""
	M = C[w]
	C.remove(M)
	s -=1
	J -= t
	l = len(bin(max(M)))-2
	i = 0
	print "majority decision"
	num_corr_1 = []
	V_tild = 0
	while i < l:
		b0 = 0
		b1 = 0
		for j in range(t):
			if M[j] & 1:
				b1 += 1
			else:
				b0 += 1
			M[j] >>= 1
		if b1 > b0:
			V_tild += 2**i
		num_corr_1.append(b1)
		i += 1

	print "Verifing ..."
	message = randint(2, 2**10)
	cipher = squareAndMultiply(message, e, n)
	message_verif = squareAndMultiply(cipher, V_tild, n)
	nb_possibilite = 0
	for bla in num_corr_1:
		if (bla == t) or (bla == 0):
			continue
		nb_possibilite += 1
	print "*****", nb_possibilite, "*****"
	stop = 0
	print hex(V_tild)
	if message == message_verif:
		print "Found :)"
		finish = 1
		print time() - time_start
		exit()

	print "Brute force avec 1 bit"

	i = 0
	l = len(num_corr_1)
	stop = 0
	while i < l and stop == 0:
		print i, "/",(l - 1), "			\r",
		if num_corr_1[i] == 0 or num_corr_1[i] == t:
			i += 1
			continue
		pos = [i, -1, -1]
		V_test = change_bit(V_tild, pos)
		message_verif = squareAndMultiply(cipher, V_test, n)
		if message == message_verif:
			stop = 1
		i += 1
	print ""
	if stop == 1:
		print "Found :)"
	print "Brute force avec 2 bits"
	i = 0
	while i < l and stop == 0:
		if num_corr_1[i] == 0 or num_corr_1[i] == t:
			i += 1
			continue
		j = 0
		while j < l and stop == 0:
			print (i*l+j)+1, "/", l**2, "			\r",
			if num_corr_1[j] == 0 or num_corr_1[j] == t:
				j += 1
				continue
			if i == j:
				j += 1
				continue
			pos = [i, j, -1]
			V_test = change_bit(V_tild, pos)
			message_verif = squareAndMultiply(cipher, V_test, n)
			if message == message_verif:
				stop = 1
			j += 1

		i += 1
	print ""
	if stop == 1:
		print "Found :)"

	print "Brute force avec 3 bits"
	i = 0
	while i < l and stop == 0:
		if num_corr_1[i] == 0 or num_corr_1[i] == t:
			i += 1
			continue
		j = 0
		while j < l and stop == 0:
			if num_corr_1[j] == 0 or num_corr_1[j] == t:
				j += 1
				continue
			if i == j:
				j += 1
				continue
			k = 0
			while k < l and stop == 0:
				print (i*(l**2)+j*l+k), "/", l**3, "			\r",
				if num_corr_1[k] == 0 or num_corr_1[k] == t:
					k += 1
					continue
				if i == k or j == k:
					k += 1
					continue
				V_test = change_bit(V_tild, pos)
				message_verif = squareAndMultiply(cipher, V_test, n)
				if message == message_verif:
					stop = 1
				k += 1
			j += 1
		i += 1
	#print ""
	if stop == 0:
		print "Not found :'("
	else: 
		print "Found :)"
		finish = 1
		print V_test

Temps = time() - time_start
print "j     :", J
print "Temps :", Temps
print "#C    :", len(C)

