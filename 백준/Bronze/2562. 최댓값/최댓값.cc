#include<stdio.h>

int main(){
    int input;
    int max=0;
    int b=0;
    
    for(int i=0;i<9;i++){
        scanf("%d",&input);
        if(input>max){
            max=input;
            b=i+1;
        }
    }
    printf("%d\n%d", max, b);
    return 0;
}