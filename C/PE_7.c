// 10001st prime
//
// https://projecteuler.net/problem=7

#include <math.h>
#include <stdio.h>

int is_prime(int n) {
    int root = sqrt(n);

    for (int i = 2; i <= root; i++) {
        if (n % i == 0) {
            return 0;
        }
    }

    return 1;
}

int main() {
    int n = 1;
    int p_i = 0;

    while (p_i < 10001) {
        n++;
        if (is_prime(n)) {
            p_i++;
        }
    }

    printf("%d\n", n);

    return 0;
}
