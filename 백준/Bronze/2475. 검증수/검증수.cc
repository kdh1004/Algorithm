#include<stdio.h>

int main(){
    int a;
    int b=0;
    
    for(int i=0;i<5;i++){
        scanf("%d",&a);
        b += a*a;
    }
    
    b %= 10;
    
    printf("%d",b);
    return 0;
}