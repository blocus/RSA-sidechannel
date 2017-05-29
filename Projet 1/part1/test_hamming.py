#! /usr/bin/python
from random import random, randint
import math
import Crypto.PublicKey.RSA as RSA
HAMMING = [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 4, 1, 2, 2, 3, 2, 3, 3, 4, 2, 3, 3, 4, 3, 4, 4, 5, 1, 2, 2, 3, 2, 3, 3, 4, 2, 3, 3, 4, 3, 4, 4, 5, 2, 3, 3, 4, 3, 4, 4, 5, 3, 4, 4, 5, 4, 5, 5, 6, 1, 2, 2, 3, 2, 3, 3, 4, 2, 3, 3, 4, 3, 4, 4, 5, 2, 3, 3, 4, 3, 4, 4, 5, 3, 4, 4, 5, 4, 5, 5, 6, 2, 3, 3, 4, 3, 4, 4, 5, 3, 4, 4, 5, 4, 5, 5, 6, 3, 4, 4, 5, 4, 5, 5, 6, 4, 5, 5, 6, 5, 6, 6, 7, 1, 2, 2, 3, 2, 3, 3, 4, 2, 3, 3, 4, 3, 4, 4, 5, 2, 3, 3, 4, 3, 4, 4, 5, 3, 4, 4, 5, 4, 5, 5, 6, 2, 3, 3, 4, 3, 4, 4, 5, 3, 4, 4, 5, 4, 5, 5, 6, 3, 4, 4, 5, 4, 5, 5, 6, 4, 5, 5, 6, 5, 6, 6, 7, 2, 3, 3, 4, 3, 4, 4, 5, 3, 4, 4, 5, 4, 5, 5, 6, 3, 4, 4, 5, 4, 5, 5, 6, 4, 5, 5, 6, 5, 6, 6, 7, 3, 4, 4, 5, 4, 5, 5, 6, 4, 5, 5, 6, 5, 6, 6, 7, 4, 5, 5, 6, 5, 6, 6, 7, 5, 6, 6, 7, 6, 7, 7, 8]
k_list = [256, 512, 1024, 2048, 4096]
keys = ["""-----BEGIN RSA PRIVATE KEY-----
MIGrAgEAAiEAwI4/FTS6LXcAIaOLhjnHBcadAMZ3vNX35LACPliSyYMCAwEAAQIh
AJv1WoC5gSX74X5dcU+ZEmliUeyy/ErzhYRnvb6HNrapAhEA5eLMWHodVcDGYydt
LzqwbwIRANZt3URtflIcmlULDbZRmi0CEE12820NGT2ATFm1O3Gi0TkCEQClapmA
GSuSsogIRP+t/yN9AhALZOxCmVTANv/VKIsSD9m0
-----END RSA PRIVATE KEY-----"""]

R_list = [16]

E = [0.5]#, 0.06, 0.07, 0.08, 0.09, 0.1, 0.11, 0.12, 0.13, 0.14, 0.15, 0.16, 0.17, 0.18, 0.19, 0.20, 0.21, 0.22, 0.23, 0.24, 0.25, 0.26, 0.27, 0.28, 0.29, 0.30]
f = open("test_hamming_1024.txt", "w")

def ham_2(a):
	h = 0
	while a != 0:
		p = a & 0xff
		h += HAMMING[p]
		a >>= 8
	return h

def genV(key, rand, eb):
	v = key.d + (rand * ((key.p - 1)*(key.q - 1)))
	l = len(bin(v)) - 2
	i = 0
	while i < l:
		if random() < eb:
			v ^= 2**i
		i += 1
	return v

A = 100000

# ==
compt_key = 0
for key_RSA in keys:
	key = RSA.importKey(key_RSA)
	k = k_list[compt_key]
	print len(bin(key.n))-2
	for R in R_list:
		for eb in E:
			print "*"*50," r_j = r_m ", "*"*50
			f.write("*"*50+" r_j = r_m "+ "*"*50+"\n")
			print "-"*50+" eb = "+str(eb)+" "+ "-"*50
			f.write("-"*50+" eb = "+str(eb)+" "+ "-"*50+"\n")
			print "k = "+str(k)
			f.write("k = "+str(k)+"\n")
			print "R ="+str(R)
			f.write("R ="+str(R)+"\n")

			i = 0
			ecart = 0.0
			moy = 0.0
			while i < A:
				print i, "of", A, "                 ",moy/(i+1), math.sqrt((ecart/(i+1)) - (moy/(i+1))**2),"                 \r",
				rand = randint(0, 2**R)
				v1 = genV(key, rand, eb)
				v2 = genV(key, rand, eb)
				h = ham_2(v1 ^ v2)
				moy += h
				ecart += h**2
				i += 1
			print ""
			print "moyenne =", moy / A
			f.write("moyenne =" +str(moy / A)+"\n")
			print "ecart type =", math.sqrt((ecart/(A)) - (moy/(A))**2)
			f.write("ecart type ="+ str(math.sqrt((ecart/(A)) - (moy/(A))**2))+"\n")



		# !=
		for eb in E:
			print "*"*50," r_j != r_m ", "*"*50
			f.write("*"*50+" r_j != r_m "+ "*"*50+"\n")
			print "-"*50+" eb == "+str(eb)+" "+ "-"*50
			f.write("-"*50+" eb == "+str(eb)+" "+ "-"*50+"\n")
			print "k = "+str(k)
			f.write("k = "+str(k)+"\n")
			print "R ="+str(R)
			f.write("R ="+str(R)+"\n")

			i = 0
			ecart = 0.0
			moy = 0.0
			while i < A:
				print i, "of", A, "                 ",moy/(i+1), math.sqrt((ecart/(i+1)) - (moy/(i+1))**2),"                 \r",
				rand_1 = randint(0, 2**R)
				rand_2 = randint(0, 2**R)
				while rand_1 == rand_2:
					rand_2 = randint(0, 2**R)
				v1 = genV(key, rand_1, eb)
				v2 = genV(key, rand_2, eb)
				h = ham_2(v1 ^ v2)
				moy += h
				ecart += h**2
				i += 1
			print ""
			print "moyenne =", moy / A
			f.write("moyenne =" +str(moy / A)+"\n")
			print "ecart type =", math.sqrt((ecart/(A)) - (moy/(A))**2)
			f.write("ecart type ="+ str(math.sqrt((ecart/(A)) - (moy/(A))**2))+"\n")
	compt_key += 1
f.close()