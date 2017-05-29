#! /usr/bin/python

def fact(n):
    x=1
    for i in xrange(2,n+1):
        x*=i
    return x

def combinaison(n,k):
    """Combinaison de n objets pris p a p."""
    return fact(n)/(fact(k)*fact(n-k))

eb = [0.24, 0.25]

for e in eb:
	print "-"*100
	for u in range(50):
		t = 2*u+1
		somme = 0
		s = u+1
		while s < t+1:
			t1 = combinaison((2*u)+1, s)
			t2 = e**s
			t3 = (1-e)**(t-s)
			somme += t1*t2*t3
			s += 1
		if (256+16)*somme < 2:
			break
	print e, t - 2