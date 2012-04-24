#! /usr/bin/env python
import random
import time
#-----------------------------------
# Get a median number from the number list
#-----------------------------------

def median1(a):
    n=len(a)
    rank=[0]*n
    for i in range(1,n):
        for j in range(i):
            if a[j]<=a[i]:
                rank[i]+=1
            else:
                rank[j]+=1
    m=(n+1)/2-1
    for i,e in enumerate(rank):
        if e==m:
            return a[i]

def median2(a):
    m=(len(a)+1)/2-1
    return sorted(a)[m]

def partion(a,p,q):
    x=a[p]
    i=p
    for j in range(p+1,q+1):
        if a[j]<x:
            i+=1
            a[i],a[j]=a[j],a[i]
    a[i],a[p]=a[p],a[i]
    return i

def randomPartion(a,p,q):
    i=random.randint(p,q-1)
    a[p],a[i]=a[i],a[p]
    return partion(a,p,q)

def select(a,p,q,k):
    if p==q:
        return a[p]
    i=randomPartion(a,p,q)
    m=i-p+1
    #print 'p is %d,q is %d,i is %d, m is %d ,k is %d' %(p,q,i,m,k)
    if (k+1)==m:
        return a[i]
    elif (k+1)>m:
        return select(a,i+1,q,k-m)
    else:
        return select(a,p,i-1,k)

def median3(a):
    n=len(a)
    m=(n+1)/2-1
    return select(a,0,n-1,m)

def select2(a,p,q,k):
    for e in a:
        print e,
    print '\n=================\n'
    l=p
    u=q
    while l<u:
        i=l
        j=u
        x=a[k]
        while True:
            while a[i]<x:
                i+=1
            while x<a[j]:
                j-=1
            if i <= j:
                a[i],a[j]=a[j],a[i]
                i+=1
                j-=1
            if i>j:
                break
        if j<k:
            l=i
        if k<i:
            u=j
        for e in a:
            print e,
        print '\n'
        print l,u,i,j
    return a[k]

def median4(a):
    n=len(a)
    m=(n+1)/2-1
    return select2(a,0,n-1,m)

def main():
    while(True):
        s=raw_input('input:n m\n')
        ins=map(int,s.split())
        n=ins[0]
        m=ins[1]
        a=[0]*n
        for i in range(len(a)):
            a[i]=random.randint(0,n)
        s=time.clock()
        if m==1:
            result=median1(a)
        elif m==2:
            result=median2(a)
        elif m==3:
            result=median3(a)
        elif m==4:
            result=median4(a)
        t=(time.clock()-s)*1000
        rigres=median2(a)
        if result != rigres:
            print 'Mistake method!'
        print 'the number : %d ,the method is : %d ,the result is %d,the rigres : %d time is %d ' %(n,m,result,rigres,t)
    
if __name__=='__main__':
    main()
