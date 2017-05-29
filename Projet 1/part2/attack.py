#! /usr/bin/python
import naf
import Crypto.PublicKey.RSA as RSA
from random import randint, random
from math import sqrt
txt = """-----BEGIN RSA PRIVATE KEY-----
MIGrAgEAAiEAwI4/FTS6LXcAIaOLhjnHBcadAMZ3vNX35LACPliSyYMCAwEAAQIh
AJv1WoC5gSX74X5dcU+ZEmliUeyy/ErzhYRnvb6HNrapAhEA5eLMWHodVcDGYydt
LzqwbwIRANZt3URtflIcmlULDbZRmi0CEE12820NGT2ATFm1O3Gi0TkCEQClapmA
GSuSsogIRP+t/yN9AhALZOxCmVTANv/VKIsSD9m0
-----END RSA PRIVATE KEY-----"""
key = RSA.importKey(txt)
d = key.d
y = (key.p - 1)*(key.q - 1)
R = 16
N = [116, 116, 116, 30, 30, 30, 20]
U = [2, 2, 2, 3, 3, 3, 4]
E = [0.08, 0.09, 0.1, 0.06, 0.07, 0.04, 0.05]
for compteur in range(len(U)):
	u = U[compteur]
	eb = E[compteur]
	n = N[compteur]
	list_traces = []
	list_random = []
	i = 0
	while i < n:
		r = randint(0, 2**R)
		list_random.append(r)
		list_traces.append(d+(r*y))
		i += 1 
	list_uplet = []
	if u == 2:
		for i in range(n-1):
			for j in range(i+1, n):
				list_uplet.append((i, j))
	if u == 3:
		for i in range(n-2):
			for j in range(i+1, n-1):
				for k in range(j+1, n):
					list_uplet.append((i, j, k))
	if u == 4:
		for i in range(n-3):
			for j in range(i+1, n-2):
				for k in range(j+1, n-1):
					for l in range(k+1, n):
						list_uplet.append((i, j, k, l))
	for i in list_uplet:
		for j in list_uplet:
			if i == j:
				continue
			s = 0
			for k in i:
				v_i = d + (y * list_random[k])
				l = len(bin(v_i)) - 2
				com_i = 0
				while com_i < l:
					if random() < eb:
						v_i ^= 2**com_i
					com_i += 1
				s += v_i 
			for k in j:
				v_i = d + (y * list_random[k])
				l = len(bin(v_i)) - 2
				com_i = 0
				while com_i < l:
					if random() < eb:
						v_i ^= 2**com_i
					com_i += 1
				s -= v_i 
			n = naf.NAF(s)
			if n.hamming() < 65:
				print i, j, list_random[i[0]], list_random[i[1]], list_random[j[0]], list_random[j[1]]


	









