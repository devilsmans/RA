import sys

def fillValues(w,v,maxWeight):
	n = len(w)
	a = [0]*(maxWeight+1)
	l = [-1]*(maxWeight+1)

	for i in range(1,len(a)):
		for j in range(0,n):
			if w[j] <= i and (v[j] + a[i - w[j]]) > a[i]:
				a[i] = v[j] + a[i - w[j]]
				l[i] = j	
	print a[len(a)-1]
	print a
	track(w,l)

def track(w,l):
	comb = [0]*len(w)
	postTracker = len(l)-1
	itemTracker = l[postTracker]
	while itemTracker !=-1 and postTracker > 0:
		comb[itemTracker] = comb[itemTracker]+1
		postTracker = postTracker - w[itemTracker]
	        itemTracker = l[postTracker]
	print comb
	


tdict = {}
print "Enter the dict value:"
kk = raw_input()
vv = input()
tdict[kk]=vv
print tdict

for i in tdict:
	zone=tdict[i]
	w = []
	v = []
	k = 1
	for j in ('large','x','2x','4x','8x','10x'):
		result = zone.get(j,0)
		w.append(result)
		if result == 0:
			v.append(0)
		else:
			v.append(k)
		k = k*2
maxWeight = input("Max Value:")
print w
print v
fillValues(w,v,maxWeight)
