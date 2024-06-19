#include<stdio.h>

int main(){
    int a;
    char b[101];
    
    scanf("%d",&a);
    scanf("%s",b);
    
    int sum=0;
    for(int i=0;i<a;i++){
        sum += b[i] - '0';
    }
    printf("%d",sum);
    return 0;
}