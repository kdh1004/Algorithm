#include<stdio.h>

int main(){
    int melody[8]={0,};
    int check=0;
    
    for(int i=0;i<8;i++){
        scanf("%d", &melody[i]);
    }
    if(melody[0]==1){
        for(int i=1;i<8;i++){
            if(melody[i]==i+1){
                check=1;
            }
        else{
            check=0;
            break;
        }
        }
    }
    else if(melody[0]==8){
        for(int i=1;i<8;i++){
            if(melody[i]==8-i){
                check=2;
            }
        else{
            check=0;
            break;
        }
        }
    }
    if (check == 1) printf("ascending");
    else if (check == 2) printf("descending");
    else printf("mixed");
    
    return 0;
}