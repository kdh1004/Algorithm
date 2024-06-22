#include<stdio.h>

int main(){
    int a[9] = {0};
    int max=0;
    int b=0;
    
    for(int i=0;i<9;i++){
        scanf("%d",&a[i]);
        if(a[i]>max){
            max=a[i];
            b=i+1;
        }
    }
    printf("%d\n%d", max, b);
    return 0;
}