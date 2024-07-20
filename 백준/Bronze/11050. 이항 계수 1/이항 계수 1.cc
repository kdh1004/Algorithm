#include<stdio.h>

int fact(int num){
    int result = 1;
    for(int i=1;i<=num;i++){
        result=result*i;
    }
    return result;
}
int main(){
    int N;
    int K;
    scanf("%d",&N);
    scanf("%d",&K);
    
    int A=fact(N);
    int B=fact(K);
    int C=fact(N-K);
    
    int result=A/(B*C);
    printf("%d\n",result);
}