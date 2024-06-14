#include<stdio.h>

int main(){
    int a[30] = {0};
    for(int i;i<28;i++){
        int n;
        scanf("%d",&n);
        a[n-1]++;
    }
    for(int j;j<30;j++){
        if(a[j]==0){
            printf("%d\n",j+1);
        }
    }
}