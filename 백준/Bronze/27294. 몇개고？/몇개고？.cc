#include <stdio.h>

int main() {
    int t=0, s=0;
    scanf("%d %d", &t, &s);
    if(12<=t && t<=16)
    {
        if(s==1)
            printf("280");
        else
            printf("320");
    }
    else
        printf("280");
    return 0;
}