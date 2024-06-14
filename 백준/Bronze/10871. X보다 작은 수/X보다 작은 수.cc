#include<stdio.h>

int main(){
    int n,d;
    int a[10000];
    scanf("%d %d",&n, &d);
    
    for(int i;i<n;i++){
        scanf("%d", &a[i]);
        if(a[i]<d){
            printf("%d ", a[i]);
        }
    }
}