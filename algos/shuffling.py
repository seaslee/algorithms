#===========================
#Fisher-Yates shuffle algo
#author seaslee
#date: 4/24,2012
#===========================
import random
a=[1,2,3,4,5]
len(a)
def fyshuffling(a):
    for i in range(len(a)-1,0,-1):
        j=random.randint(0,i)
        a[i],a[j]=a[j],a[i]

if __name__=='__main__':
    fyshuffling(a)
    print a

