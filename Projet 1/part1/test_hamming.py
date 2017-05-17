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
-----END RSA PRIVATE KEY-----""", """-----BEGIN RSA PRIVATE KEY-----
MIIBOgIBAAJBAL4dQMCgpGczrb/ZgJzJ7LguUrqjaLFH1m3esbrrcLVWoto0Ly2k
S36BAqtsJGXCx5IRXTGSDTodZAPA+80vDrkCAwEAAQJASo+ggKvALrWG9FIybcuH
6qhIS+igu76n64lGfT+vgX6eRRKB3/gjWKk09m85Q+ZSM8XFG58RH7YrEHXnHtdq
MQIhAPDC9FZjplTdZyNtuYwuQIHr10/59fQl5hYj6JRmCGDtAiEAyiWp5ATijO/C
UWzYmD7X77bR/dNDAkr5CXaeeKBOR30CIDbja0rqqvf8BdB46m0/+irkdpDgHqeL
oFn508NJQ629AiB1Jfaa6inQu3HFdmrfcCv8A9sWWkRPI9vHHDMifORgkQIhANdE
9O38B4SKHEtMJueU8+SyNtKD7tTkwiwcKOFss6K5
-----END RSA PRIVATE KEY-----""", """-----BEGIN RSA PRIVATE KEY-----
MIICXQIBAAKBgQDAAQi4SHyTFNUd2hwqrNZ0PJ84T0l/LD2n4scbNzDQlhYlemSm
+MRkN/b/HgR3epyNjz2ekXYhfhZf+xpwJR/+8qFe/fbYalViEyRUWrp2UMRt4wMA
ucQQx+aoozkOGb0LmJoDTgBp9l6topifc6jDR8kH8Ee1YeSqO65QgAcJpQIDAQAB
AoGBALVvBLdnP9iYof5wgZdN9eSm+Gn0emYi/ywrHqy4DXe9q7XEn2IsxyBQxiUz
T1M72L3n8nlpyTBC/o+6L7RzUHQrtONmIqBwZJGrd9YCZ+EZHa5tFzjGERkUezeS
KMEoFkwgaXnwT6G6qVWdWHNT+PMdF9EJjISFo7Gn+jfSItxtAkEA9iFr39dIQ7E4
czlOZsdFLcN98NPUETRQkCw5aoGWT9SZZ9w2Jaw0wxpoOz+vvWCe1a2F8PxCebQr
YDr2IUKOSwJBAMez/kymEs6K2vzmoZekt/SVFtdxxA5ybe/TBZouZ0EZYGZdw6i1
fd/yPEHKuDoU52s0UGHcsUwaBvzV3ZlpEc8CQDfUqPWjjd7dCmMIssIZnZWd7Kl+
Q3KLnWK2xWdlccU2An5Os3GkOGuxR8d40NJyYlUyAVoCvsmAlv5DIaW1xTUCQB8q
pCFqOb0qRor5o3Z7KoptSidNhf+LNEUddd5eJ5ctUrInKAYIbSCqOWU7Mg0+fe9p
NrJPMwxhc326Et+CWlkCQQDkawZZ6v080JYK4NTi+3JLvB8TQc80qtQXdViIS1dA
ICgYQ9DwneRuYxHQgxTntueBTRZE2T9xO9MZTSmOyGFB
-----END RSA PRIVATE KEY-----""", """-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEAsAw7DvA+9TxNp8j8+sLJNLxSheBL502bMCvNrEZtSNHf6cfs
1EaH/5yocgbcjaNnc+Nr2cu+WSDzulB/fHXHwTPk/u8bxhYKAm82hOclBDWdThnJ
omagIBpa/sExos9h+MlyXb3+gT4z9//HYt+4XPWMeG3GFfkfVyZHMRDJHW0b/I0j
Kc9ODb44EOACpboZbNcQJGV6Aze9W6fulnG2FLt+l4hCTT377xVfYugxjJ/ild3z
ODI/b686F6oUgbYtzeuLWsRPSUUMoAMSjvaPDPqxhYxGllXn2uvr6PFtCfsNOI3d
Az0xRasyGUy+euGMtpF/DRpYwxAfTax/XRvA4wIDAQABAoIBAQCSQ0cZ7S5Rby2R
deIAsK6cGs5xHd3SKV8C0ZHKTKTlOEFRKOIxpvu8uboVKnA5WQZNeSgUxjq6MC9u
nwycKfqxIN1jlOK9W3grd5yTJLtTWPv9dF1aiOsGYP8y4u3LN4NNQIi9K2n0lOp2
Y9KS6g5xZSy0rXdCsDyCmnHRaQG+aJPh7UScWrjTThvGeQ+1TcZWmYKHZPzTM+b9
wfIxnosJiFUuVP/uEMU3gVa/l4umze5bO1NTk0WDYX95lLQoqs10Rh8lkV8LYKxG
nbBv4vILb65RctF7QGf+wJ5Bi/P/AuPAY+BQStegjG/W+nuju//EwZKD6K9uwmYi
saT2BkEpAoGBAOCuZWTnjqg0bbcAUQqULvuyQHFmTsccTA81CS3u9YMRRmtWMY+L
vKgk5BWIl8p2rEnBUonI3vlZ7xb7QMzvD3/uwLOES0F1rpIVlWJ9YJZXVNJ2zzis
LelpXgkRu+uY0ihUECNu1aqfDKojzO7J34nt0Q081NH6nmCZuja0KEtvAoGBAMiW
YZlhf4R2XSkeHTUE2ynR2lK9qIwwEfSaGPtEW1rs6UOAGtS5l/4cQwpsViIB63eT
Ic43E6CNDgZ7dq9pZPHj3vmw7E6sPbVgNADFD10aH5ketZfZ7ToUGfZVOe1lj7Je
CP+ejfUm3tkJdMwQwP+zeHE5PVgR7VoLfzBqRbfNAoGAcXFcnKAV9XPTWaz9Pjwn
pMoRo7AmYn41IRCEO/8FU1IrnhJ9H59MeBF4YC8BhSZ6QxsrU4pqmrf/8jiWNWMX
Dl88SOepH7oNlJD1Ri9Lz1z05Pc8Fb9Jxyp+YlHj8kbNBbO8Gkfh9i4sNNOyq3ae
OYQsI2Tth7/kq52y2eAI4F0CgYA3Ulpqrhw4UVjSTU7q34L+nrUjGtHQkDVzi8iW
DD1R74NKLZu4zdMgr3TB/C0pRfRGT1sEf+Y24pBas1SBfoTrvdgyb1xNOm3uhzDw
gWkCWYEbfv/AeMdXvFGIweqvEdK28/5xWa53TZgqrdP7sCc6nqn6ODo1/wPCUOds
V/MQhQKBgQCQM0wNqH/GElsI6L5Eem1FASHS7xZ1BL/1bOOELnKF1EDXAYXsYsIA
LrGiCq80tTHCM22ZgOSiyWRr5LBMyL/sMOWFxwhshEELNMW36GTmgW2ik79nrWmn
jJ5GmxZsQ3mH58VJV+s27ODSGyNRZIYZ83F2kTy/mucFlwYFtIaPYA==
-----END RSA PRIVATE KEY-----""", """-----BEGIN RSA PRIVATE KEY-----
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
-----END RSA PRIVATE KEY-----"""]

R_list = [10, 11, 12, 13, 14, 15, 16]

E = [0.05, 0.06, 0.07, 0.08, 0.09, 0.1, 0.11, 0.12, 0.13, 0.14, 0.15, 0.16, 0.17, 0.18, 0.19, 0.20, 0.21, 0.22, 0.23, 0.24, 0.25, 0.26, 0.27, 0.28, 0.29, 0.30]
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

A = 1000000

# ==
compt_key = 0
for key_RSA in keys:
	key = key = RSA.importKey(key_RSA)
	k = k_list[compt_key]
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