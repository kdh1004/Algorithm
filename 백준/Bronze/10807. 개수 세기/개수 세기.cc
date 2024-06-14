#include<stdio.h>
int main(){
    int n,v,i;
    int arr[101];
    
    scanf("%d",&n);
    
    for(i=0;i<n;i++){
        scanf("%d",&arr[i]);
    }
    scanf("%d",&v);
    
    int res=0;
    for(i=0;i<n;i++){
        if(arr[i]==v)
            res++;
    }
    printf("%d",res);
}