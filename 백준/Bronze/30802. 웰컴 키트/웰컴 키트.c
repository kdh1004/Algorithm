#include <stdio.h>

int main() {
    int N;
    int size[6];
    int T, P;

    scanf("%d", &N);
    for (int i = 0; i < 6; i++) {
        scanf("%d", &size[i]);
    }
    scanf("%d %d", &T, &P);

    int min = 0;
    for (int i = 0; i < 6; i++) {
        if (size[i] % T == 0)
            min += size[i] / T;
        else
            min += size[i] / T + 1;
    }

    printf("%d\n", min);
    printf("%d %d\n", N / P, N % P);

    return 0;
}