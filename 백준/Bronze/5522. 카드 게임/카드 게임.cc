#include<stdio.h>

int main(){
    int a, i, sum = 0;
    for(i=0;i<5;i++){
        scanf("%d", &a);
        sum += a;
    }
    printf("%d", sum);
    return 0;
}