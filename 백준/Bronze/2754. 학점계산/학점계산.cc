#include<stdio.h>

int main(){
    char score[3];
    scanf("%s",&score);
    float sum = 0.0;
    if(score[0]=='A'){
        sum = 4;
    }
    else if(score[0]=='B'){
        sum = 3;
    }
    else if(score[0]=='C'){
        sum = 2;
    }
    else if(score[0]=='D'){
        sum = 1;
    }
    else{
        sum = 0;
    }
    if(score[1]=='+'){
        sum += 0.3;
    }
    if(score[1]=='-'){
        sum -= 0.3;
    }
    else{
        sum += 0;
    }
    printf("%.1lf",sum);
}