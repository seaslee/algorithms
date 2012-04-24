#include<stdio.h>
#include<stdlib.h>
/*-------------------------------------------------
 *author seaslee
 *Problem :  decide if a circle in a link list
 *spend time : about 4 hours
 *learn : 1)how to implement link list in C 
          2)Know a good algorithm 
          3)more about pointer in C
 *-------------------------------------------------
 */
struct node{
    int data;
    struct node  * next;
};
/*
 * walk through the list p to see that :
 * I walk the same pointer twice .
 * yes,has circle; no ,no circle
 */
int judgeHasCircle(struct node * p){
    struct node * st=NULL;
    struct node * current=p;
    do{
        struct node *n=malloc(sizeof(struct node));
        struct node *tmp=current;
        n->data=(int)current;
        n->next=st;
        struct node * stn=st;
        while(stn){
            int addr=stn->data;//Error first,waste 30min
            if(addr==n->data)
                return 1;
            else
                stn=stn->next;
        }
        st=n;
        current=tmp->next;
    }while(current);
    return 0;
}
/*
 * two pointer to walk through the p to see:
 * if two pointer can meet
 * yes ,has circle;no ,no circle
 */
int judgeHasCircle1(struct node * p){
    struct node * fastptr=p;
    struct node * slowptr=p;
    while((slowptr->next)&&(fastptr->next)&&(fastptr->next->next)){
        slowptr=slowptr->next;
        fastptr=fastptr->next->next;
        if(fastptr==slowptr)
            return 1;
    }
    return 0;
}

int main(){
    struct node * list=NULL;
    int i;
    for(i=0;i<10;i++){
        struct node *n=malloc(sizeof(struct node));
        n->data=i;
        n->next=list;
        list=n;
    }
    struct node * current=list;
    int j=0;
    struct node * back;
    struct node * pre;
    while(current){
        if(j==4)
            back=current;
        pre=current;
        current=current->next;
        j++;
    }
    pre->next=back;
    int b=judgeHasCircle(list);
    if(b)
        printf("HAS CIRCLE!\n");
    else
        printf("NO CIRCLE!\n");
    int c=judgeHasCircle1(list);
    if(c)
        printf("HAS CIRCLE!\n");
    else
        printf("NO CIRCLE!\n");

    return 0;
}

