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
dic = {}
R = 16
nb_test = 100000
U = [2, 2, 2, 3, 3, 3, 4]
E = [0.08, 0.09, 0.1, 0.06, 0.07, 0.04, 0.05]
#print "compteur           u  eb   esp   sig seuil"
for compteur in range(len(U)):
	u = U[compteur]
	eb = E[compteur]
	somme = 0.0
	somme_carre = 0.0
	i = 0
	seuil = [0, 0]
	while i < nb_test:
		while 1:
			if u == 2:
				uplet = (randint(0, 2**R), randint(0, 2**R), 0, 0)
				s = uplet[0] + uplet[1]
			elif u == 3:
				uplet = (randint(0, 2**R), randint(0, 2**R), randint(0, 2**R), 0)
				s = uplet[0] + uplet[1] + uplet[2]
			elif u == 4:
				uplet = (randint(0, 2**R), randint(0, 2**R), randint(0, 2**R), randint(0, 2**R))
				s = uplet[0] + uplet[1] + uplet[2] + uplet[3]
			if s in dic:
				old = dic.pop(s)
				couple_uplet = [old, uplet]
				break
			dic[s] = uplet
		v_tild = 0
		sign = 0
		for up in couple_uplet:
			for v in up:
				if v == 0:
					continue
				v_i = d + (y * v)
				l = len(bin(v_i)) - 2
				com_i = 0
				while com_i < l:
					if random() < eb:
						v_i ^= 2**com_i
					com_i += 1
				v_tild += ((-1)**sign) * v_i
			sign += 1
		v_tild = naf.NAF(v_tild)
		ham_v_tild = v_tild.hamming()
		somme += ham_v_tild
		somme_carre += ham_v_tild**2
		if ham_v_tild < 65.9:
			seuil[0] += 1
		if ham_v_tild < 63.6:
			seuil[1] += 1
		
		print "("+str(i)+"/"+str(nb_test)+")    "+str(u)+" %.2f" %eb +" %.2f" %(somme / (i+1)) +" %.2f " %(sqrt((somme_carre / (i+1)) - (somme / (i+1))**2))+str(seuil) +"                       \r",
		i += 1
	print "("+str(nb_test)+"/"+str(nb_test)+")    "+str(u)+" %.2f" %eb +" %.2f" %(somme / (nb_test+1)) +" %.2f " %(sqrt((somme_carre / (nb_test+1)) - (somme / (nb_test+1))**2))+str(seuil)
















