#! /usr/bin/env python
from random import random
from time import clock
#---------------------------------
# author :seaslee
#problem :
#input:  array a of n elements which is float
#output: the max sum of the continous subarray of the array a
#following is four methods from "Programming Pearls"
#---------------------------------
a=[0]*10000000
n=0
def sprinkle():
    global a
    global n
    for i in range(n):
        a[i]=1-2*random()

#method 1 , running time is :O(n^3)
def maxsubarr1():
    global a
    global n
    submax=0
    for i in range(n):
        for j in range(i,n):
            subsum=0
            for k in range(i,j+1):
                subsum+=a[k]
        submax=max(submax,subsum)
    return submax

#method 2, running time is :O(n^2)
def maxsubarr2():
    global a
    global n
    submax=0
    for i in range(n):
        subsum=0
        for j in range(i,n):
            subsum+=a[j]
            submax=max(submax,subsum)
    return  submax

#method 3,running time is :O(nlgn)
#divide and conque.
def maxsub(l,u):
    global a
    if l>u:
        return 0
    if l==u:
        return max(a[l],0)
    m=(l+u)/2
    lmax=subsum=0
    for i in range(m,l-1,-1):
        subsum+=a[i]
        lmax=max(lmax,subsum)
    rmax=subsum=0
    for i in range(m+1,u+1):
        subsum+=a[i]
        rmax=max(rmax,subsum)
    return max(lmax+rmax,maxsub(l,m),maxsub(m+1,u))

def maxsubarr3():
    global n
    return maxsub(0,n-1)
#method 4,running time is :O(n)
def maxsubarr4():
    global a
    global n
    front=0
    submax=0
    for i in range(n):
        front+=a[i]
        front=max(front,0)
        submax=max(submax,front)
    return submax
        
if __name__=='__main__':
    global n
    #from timeit import Timer
    while True:
        s=raw_input("Input:")
        ins=map(int,s.split())
        algnum=ins[0]
        n=ins[1]
        sprinkle()
        start = clock()
        thisans = -1
        if algnum ==1:
            thisans=maxsubarr1()
            #t=Timer('maxsubarr1()','from __main__ import maxsubarr1 ')
        elif algnum==2:
            thisans=maxsubarr2()
            #t=Timer('maxsubarr2()','from __main__ import maxsubarr2')
        elif algnum==3:
            thisans=maxsubarr3()
            #t=Timer('maxsubarr3()','from __main__ import maxsubarr3')
        elif algnum==4:
            thisans=maxsubarr4()
            #t=Timer('maxsubarr4()','from __main__ import maxsubarr4')
        clicks = clock()-start;
        #clicks=t.timeit(10)/10
        print '%d\t%d\t%.2f\t%.2f\t' %(algnum, n,thisans,clicks)

