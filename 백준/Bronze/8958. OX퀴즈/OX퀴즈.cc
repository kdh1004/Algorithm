#include<stdio.h>
#include<string.h>

int main(){
    
    int t;
    char s[80];
    int score;
    int count;
    
    scanf("%d",&t);
    
    for(int i=0;i<t;i++){
        scanf("%s",s);
        
        score=0;
        count=1;
        
        for(int i=0;i<strlen(s);i++){
            if(s[i]=='O') score += count++;
            else if(s[i]=='X') count=1;
        }
        printf("%d \n",score);
    }
}