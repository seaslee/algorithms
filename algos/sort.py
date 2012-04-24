#! /usr/bin/env python
import random

'''This is a module of sort algorithms,
   Which is follow the "Introduction to Algorithms".
   The main is insert sort, bubble sort,merge sort,
   quick sort,count sort,radix sort,heap sort.
   The concrete introduction and analysis can refer to
   The book.
   '''
#--------------------------------------------
#insert sort , running time : O(n^2)
#[0..j] sorted, increase j to n
def insertSort(a):
    for j in range(1,len(a)):
        key=a[j]
        i=j-1
        while i>=0 and a[i]>key:
            a[i+1]=a[i]
            i-=1
        a[i+1]=key
#----------------------------------------------
#bubble sort,running time :O(n^2)
#[j..n] sorted,decrease j to 1
def bubbleSort(a):
    changed=True
    j=len(a)
    while j>1 and changed==True:
        changed=False
        for i in range(j-1):
            if a[i]>a[i+1]:
                changed=True
                a[i],a[i+1]=a[i+1],a[i]
        j-=1
#----------------------------------------------
def merge(a,p,q,r):
    t=[e for e in range(len(a))]
    k=p
    i=p
    j=q+1
    for e in range(p,q+1):
        print a[e],
    print '++++',
    for e in range(q+1,r+1):
        print a[e],
    while i<q+1 and j<r+1:
        if a[i]<a[j]:
            t[k]=a[i]
            i+=1
            k+=1
        else:
            t[k]=a[j]
            j+=1
            k+=1
    if i==q+1:
        for m in range(j,r+1):
            t[k]=a[m]
            k+=1
    elif j==r+1:
        for m in range(i,q+1):
            t[k]=a[m]
            k+=1
    for e in range(p,r+1):
        a[e]=t[e]
    print '-->>',
    for e in range(p,r+1):
        print a[e],
    print '\n'
#merge sort, running time : O(nlogn)
def mergeSort(a,p,r):
    if p<r:
        q=(p+r)/2       #to get the border
        mergeSort(a,p,q) #divide and solve recusively
        mergeSort(a,q+1,r)
        merge(a,p,q,r)#combine the solution
#---------------------------------------------------
#quick sort
#partion:a[p..i] less than x(pivot),a[i..j] bigger than x(pivot)
#        a[j..q] unknown .
def partion(a,p,q):
    x=a[p]
    i=p
    for j in range(p+1,q+1):
        if a[j]<=x:
            i+=1
            a[i],a[j]=a[j],a[i]
    a[i],a[p]=a[p],a[i]
    return i
# quick sort, worst-case runnig time : O(n^2)
def qSort(a,p,r):
    if p < r:
        q=partion(a,p,r)
        qSort(a,p,q-1)
        qSort(a,q+1,r)
#---------------------------------------------------
#counting sort,running time : O(n+k)
def countSort(a,k):
    b=[0]*len(a)
    c=[0]*(k+1)
    for j in range(len(a)):
        c[a[j]]+=1
    for j in range(1,k+1):
        c[j]=c[j]+c[j-1]
    for j in range(len(a)-1,-1,-1):
        b[c[a[j]]-1]=a[j]
        a[j]-=1
    for j in range(len(a)):
        a[j]=b[j]
#---------------------------------------
#radix sort,running time: O(d(n+k)) 
def countSortForRadix(a,d,k):
    b=[0]*len(a)
    c=[0]*(k+1)
    s=[0]*len(a)
    for j in range(len(a)):
        s[j]=a[j]
        for i in range(d):
            s[j]/=10
        s[j]%=10
    for j in range(len(a)):
        c[s[j]]+=1
    for j in range(1,k+1):
        c[j]+=c[j-1]
    for j in range(len(a)-1,-1,-1):
        b[c[s[j]]-1]=a[j]
        c[s[j]]-=1
    for j in range(len(a)):
        a[j]=b[j]

#running time : O(d(n+k))
def radixSort(a,d,k):
    for i in range(d):
        countSortForRadix(a,i,k)
#--------------------------------------
#heap sort ,running time :O(nlgn)
def maxHeapIfy(a,i,s):
    n=s
    l=2*i
    r=l+1
    if l<=n and a[l]>a[i]:
        largest=l
    else:
        largest=i
    if r<=n and a[r]>a[largest]:
        largest=r
    if largest != i:
        a[i],a[largest]=a[largest],a[i]
        maxHeapIfy(a,largest,n)
def buildMaxHeap(a):
    for j in range((len(a)-1)/2,0,-1):
        maxHeapIfy(a,j,len(a)-1)
def heapSort(a):
    buildMaxHeap(a)
    heapSize=len(a)-1
    for j in range(heapSize,1,-1):
        a[1],a[j]=a[j],a[1]
        heapSize-=1
        maxHeapIfy(a,1,heapSize)
#----------------------------------------
