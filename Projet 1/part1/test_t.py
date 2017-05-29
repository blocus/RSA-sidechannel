#! /usr/bin/python
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

print getT(1024, 16, 0.05)
print getT(1024, 16, 0.1)
print getT(1024, 16, 0.15)
print getT(1024, 16, 0.2)
print getT(1024, 16, 0.25)
print getT(1024, 16, 0.3)