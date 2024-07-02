#include<stdio.h>
#include<string.h>

int main(){
    int c[26]={0,};
    char s[101];
    scanf("%s",s);
    for(int i=0;i<strlen(s);i++){
        if(c[s[i]-'a']==0){
            c[s[i]-'a']=i+1;
        }
    }
    for(int i=0;i<26;i++){
        if(c[i]==0) printf("-1 ");
        else printf("%d ",c[i]-1);
    }
    return 0;
}