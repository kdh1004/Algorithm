#include<stdio.h>

int main(){
    int t;
    scanf("%d",&t);
    
    for(int i;i<t;i++){
        int a,b;
        scanf("%d %d",&a,&b);
        printf("%d\n",a+b);
    }
}