#! /usr/bin/env python

#Euclid 
#gcd(a,0)=a
#gcd(a,b)=gcd(b,a mod b)
#gcd can be found in the module of fractions
def gcd(a,b):
    while b:
        a,b=b,a%b
    return a

def translate( a ):
    #stack
    s=[]
    b=[]
    for i in range(len(a)):
        if i==0:
            for j in range(a[i]):
                s.append('(')
                b.append(1)
            s.append(')')
            b.append(1)
        else:
            for j in range(a[i]-a[i-1]):
                s.append('(')
                b.append(1)
            s.append(')')
            b.append(1)
    c=[]
    for m,v in enumerate(s):
        count=0
        if v==')':
            for n in range(m-1,-1,-1):
                if s[n]=='(':
                    count+=1
                if s[n]=='(' and b[n]==1:
                    b[n]=0
                    break;
            c.append(count)

    for e in c:
        print e ,
    print '\n-----------'


def isconnect(a):
    m=max(a)
    s=0
    first=True
    for e in a:
        if e!=m:
            s+=e
        if e==m and first:
            first=False
        elif e==m and not first:
            s+=e
    if m>s:
        return False
    else:
        return True
def bwt(s):
    assert '\0' not in s, "s CAN NOT contains ('\0')"
    s+='\0'
    table=sorted(s[i:]+s[:i] for i in range(len(s)))
    r=[row[-1] for row in table]
    return ''.join(r)

def ibwt(r):
    table=['']*len(r)
    for i in range(len(r)):
        table=sorted(r[i]+table[i] for i in range(len(r)))
    s=[row for row in table if row.endswith('\0')][0]
    return s.rstrip('\0')

