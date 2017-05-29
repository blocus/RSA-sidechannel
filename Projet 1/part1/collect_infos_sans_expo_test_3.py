#! /usr/bin/python
from random import random, randint, choice
import Crypto.PublicKey.RSA as RSA
import Crypto.Util.number as number
from math import sqrt
from time import time
HAMMING = [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 4, 1, 2, 2, 3, 2, 3, 3, 4, 2, 3, 3, 4, 3, 4, 4, 5, 1, 2, 2, 3, 2, 3, 3, 4, 2, 3, 3, 4, 3, 4, 4, 5, 2, 3, 3, 4, 3, 4, 4, 5, 3, 4, 4, 5, 4, 5, 5, 6, 1, 2, 2, 3, 2, 3, 3, 4, 2, 3, 3, 4, 3, 4, 4, 5, 2, 3, 3, 4, 3, 4, 4, 5, 3, 4, 4, 5, 4, 5, 5, 6, 2, 3, 3, 4, 3, 4, 4, 5, 3, 4, 4, 5, 4, 5, 5, 6, 3, 4, 4, 5, 4, 5, 5, 6, 4, 5, 5, 6, 5, 6, 6, 7, 1, 2, 2, 3, 2, 3, 3, 4, 2, 3, 3, 4, 3, 4, 4, 5, 2, 3, 3, 4, 3, 4, 4, 5, 3, 4, 4, 5, 4, 5, 5, 6, 2, 3, 3, 4, 3, 4, 4, 5, 3, 4, 4, 5, 4, 5, 5, 6, 3, 4, 4, 5, 4, 5, 5, 6, 4, 5, 5, 6, 5, 6, 6, 7, 2, 3, 3, 4, 3, 4, 4, 5, 3, 4, 4, 5, 4, 5, 5, 6, 3, 4, 4, 5, 4, 5, 5, 6, 4, 5, 5, 6, 5, 6, 6, 7, 3, 4, 4, 5, 4, 5, 5, 6, 4, 5, 5, 6, 5, 6, 6, 7, 4, 5, 5, 6, 5, 6, 6, 7, 5, 6, 6, 7, 6, 7, 7, 8]
k_list = [256]
R_list = [10]
E_list = [0.1]#, 0.16, 0.17, 0.18, 0.19, 0.20, 0.21, 0.22, 0.23, 0.24, 0.25, 0.26, 0.27, 0.28, 0.29, 0.30]

def fact(n):
    x=1
    for i in xrange(2,n+1):
        x*=i
    return x

def combinaison(n,k):
    """Combinaison de n objets pris p a p."""
    return fact(n)/(fact(k)*fact(n-k))

def getT(k, R, eb):
	for u in range(50):
		t = 2*u+1
		somme = 0
		s = u+1
		while s < t+1:
			t1 = combinaison((2*u)+1, s)
			t2 = eb**s
			t3 = (1-eb)**(t-s)
			somme += t1*t2*t3
			s += 1
		if (k+R)*somme < 2:
			break
	t = t - 2
	if t < 2:
		t = 3
	return t

def change_bit(N, l):
	tmp = N
	for pos in l :
		if pos == -1:
			continue
		tmp ^= 2**pos
	return tmp


def genRSAkey(N):
	p = number.getPrime(N/2)
	q = number.getPrime(N/2)
	n = p*q
	e = 0x10001
	y = (p-1)*(q-1)
	d = number.inverse(e, y)
	return [n, y, e, d]

def ham(a):
	h = 0
	while a != 0:
		p = a & 0xff
		h += HAMMING[p]
		a >>= 8
	return h

def squareAndMultiply(base,exponent,modulus):
	a = 1
	b = base
	while exponent != 0:
		if  exponent & 1:
			a = a * b % modulus
		b = b**2 % modulus
		exponent >>= 1
	return a

def genV(d, y, rand, eb):
	v = d + (rand * y)
	#v = d
	l = len(bin(v)) - 2
	i = 0
	while i < l:
		if random() < eb:
			v ^= 2**i
		i += 1
	return v

def getGama(k, R):
	return (0.5*(k+R)) - 4*(sqrt((k+R)*0.25))

log = open("collect_infos_sans_expo_test_3.txt", "w")
compteur_cat = 0
for k in k_list:
	for R in R_list:
		for eb in E_list:
			gama = getGama(k, R)
			t = getT(k, R, eb)
			print "Categorie", compteur_cat, "/", len(k_list)*len(R_list)*len(E_list)
			for essai in range(20):
				key = genRSAkey(k)
				# "key generated"
				n = key[0]
				y = key[1]
				e = key[2]
				d = key[3]
				# d
				finish = 0
				tour = 0
				time_start = time()
				classes = []
				rand_v_i = []
				nb_v = 0
				nb_expo = 0
				while finish == 0:
					tour += 1
					# tour
					stop = 0
					# "searching for "+str(t)+"-Birthday"
					while stop == 0:
						rand = randint(0, 2**R)
						V = genV(d, y, rand, eb)
						if nb_v == 0:
							classes.append([V])
							rand_v_i.append([rand])
						else:
							m = 0
							found = 0
							while ((m < len(classes)) and (found == 0)):
								var_test = 1
								if len(classes[m]) <= 3:
									for v_condidat in classes[m]:
										h = ham(V ^ v_condidat)
										if h > gama:
											var_test = 0
											break
									if var_test == 1:
										classes[m].append(V)
										rand_v_i[m].append(rand)
										found = 1
										if len(classes[m]) == t:
											w = m
											stop = 1
								else:
									test_classes = []
									while len(test_classes) < 3:
										tmp = choice(classes[m])
										if tmp not in test_classes:
											test_classes.append(tmp)
									for v_condidat in test_classes:
										h = ham(V ^ v_condidat)
										if h > gama:
											var_test = 0
											break
									if var_test == 1:
										classes[m].append(V)
										rand_v_i[m].append(rand)
										found = 1
										if len(classes[m]) == t:
											w = m
											stop = 1
								m += 1
							if found == 0:
								classes.append([V])
								rand_v_i.append([rand])
						nb_v += 1
					print "majority decision"
					winner_class = classes[w]
					#classes.remove(winner_class)
					len_win_class = len(bin(max(winner_class)))-2
					num_corr_1 = []
					random_class = rand_v_i[w]
					d_test = []
					for i in random_class:
						if (d+(i*y)) not in d_test:
							d_test.append(d+(i*y))
					V_tild = 0
					i = 0
					while i < len_win_class:
						b0 = 0
						b1 = 0
						for j in range(t):
							if winner_class[j] & 1:
								b1 += 1
							else:
								b0 += 1
							winner_class[j] >>= 1
						if b1 > b0:
							V_tild += 2**i
						num_corr_1.append(b1)
						i += 1
					# "Verifing ..."
					stop = 0
					nb_expo += 1
					if V_tild in d_test:
						# "Found :)"
						finish = 1
						break
					# "Brute force avec 1 bit"

					i = 0
					l = len(num_corr_1)

					while i < l and stop == 0:
						if num_corr_1[i] == 0 or num_corr_1[i] == t:
							i += 1
							continue
						pos = [i, -1, -1]
						V_test = change_bit(V_tild, pos)
						nb_expo += 1
						if V_test in d_test:
							stop = 1
						i += 1
					if stop == 1:
						break
					# "Brute force avec 2 bits"
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
							pos = [i, j, -1]
							V_test = change_bit(V_tild, pos)
							nb_expo += 1
							if V_test in d_test:
								stop = 1
							j += 1

						i += 1
					if stop == 1:
						break
					# "Brute force avec 3 bits"
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
							k_compteur = 0
							while k_compteur < l and stop == 0:
								if num_corr_1[k_compteur] == 0 or num_corr_1[k_compteur] == t:
									k_compteur += 1
									continue
								if i == k_compteur or j == k_compteur:
									k_compteur += 1
									continue
								pos = [i, j, k_compteur]
								V_test = change_bit(V_tild, pos)
								nb_expo += 1
								if V_test in d_test:
									stop = 1
								k_compteur += 1
							j += 1
						i += 1
					if stop == 1:
						break
				calc_time = time() - time_start
				r_val = set()
				true_class = 0
				for ran in rand_v_i:
					test_val = ran[0]
					test_true = 1
					for r in ran:
						r_val.add(r)
						if test_val != r:
							test_true = 0
					true_class += test_true
				ch = "("+str(essai)+ " / 20)\t"+str(k)+"\t"+str(R)+"\t"+str(eb)+"\t"+str(t)+"\t"+str(calc_time)+"\t"+str(tour)+"\t"+str(nb_v)+"\t"+str(len(rand_v_i))+"\t"+str(true_class)+"\t"+str(len(r_val))+"\t"+str(nb_expo)
				print ch
				log.write(ch+"\n")
			compteur_cat += 1
