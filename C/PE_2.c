// Even Fibonacci numbers
//
// https://projecteuler.net/problem=2

#include <stdio.h>

int main() {
    int sum = 0;
    int a = 0;
    int b = 1;

    while (1) {
        b += a;
        a = b - a;

        if (b > 4000000) break;

        if (b % 2 == 0) sum += b;
    }

    printf("%d\n", sum);

    return 0;
}
