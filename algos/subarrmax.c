/*---------------------------------*/
/*author :seaslee*/
/*problem :*/
/*input:  array a of n elements which is float*/
/*output: the max sum of the continous subarray of the array a*/
/*following is four methods from "Programming Pearls"*/
/*---------------------------------*/

#include<stdio.h>
#include<time.h>
#include<math.h>
#include<stdlib.h>
#define MAX  10000003
float a[MAX];
int n;
double t[7][5];

float max(float a,float b){
    return a>b?a:b;
}
void sprinkle() /* Fill x[n] with reals uniform on [-1,1] */
{   int i;
    for (i = 0; i < n; i++)
        a[i] = 1 - 2*( (float) rand()/RAND_MAX);
}

float  maxsubarr1(){
    int i,j,k;
    float subsum,submax;
    submax=0;
    for(i=0;i<n;i++){
        for(j=i;j<n;j++){
            subsum=0;
            for(k=i;k<=j;k++){
                subsum+=a[k];
            }
            submax=max(submax,subsum);
        }
    }
    return submax;
}

float maxsubarr2(){
    int i,j;
    float subsum,submax;
    submax=0;
    for(i=0;i<n;i++){
        subsum=0;
        for(j=i;j<n;j++){ //bad luck ! i=j
            subsum+=a[j];
            submax=max(submax,subsum);
        }
    }
    return submax;
}

float maxsubarr3(int l,int u){
    if(l>u)
        return 0;
    if(l==u)
        return max(a[l],0);
    int m=(l+u)/2;
    float lmax,rmax,subsum;
    lmax=0;
    subsum=0;
    int i;
    for(i=m;i>=l;i--){ //bad luck ! i>=i
        subsum+=a[i];
        lmax=max(lmax,subsum);
    }
    rmax=0;
    subsum=0;
    for(i=m+1;i<=u;i++){
        subsum+=a[i];
        rmax=max(rmax,subsum);
    }
    return max(lmax+rmax,max(maxsubarr3(l,m),maxsubarr3(m+1,u)));
}

int maxsubarr4(){
    int i;
    float top,submax;
    top=0;
    submax=0;
    for(i=0;i<n;i++){
        top+=a[i];
        top=max(top,0);
        submax=max(submax,top);
    }
    return submax;
}

int main(){
    int algnum, start, clicks;
    float thisans;
    while (scanf("%d %d", &algnum, &n) != EOF) {
        sprinkle();
        start = clock();
        thisans = -1;
        switch (algnum) {
			case 1:  thisans = maxsubarr1();  break;
			case 2:  thisans = maxsubarr2();  break;
			case 3:  thisans = maxsubarr3(0,n-1);  break;
			case 4:  thisans = maxsubarr4();  break;
			default: break;
		}
        clicks = clock()-start;
        printf("%d\t%d\t%f\t%d\t%f\n", algnum, n, thisans,clicks, clicks / (float) CLOCKS_PER_SEC);
    }
    return 0; 
}
