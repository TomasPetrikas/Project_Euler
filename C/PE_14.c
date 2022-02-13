// Longest Collatz sequence
//
// https://projecteuler.net/problem=14

// OEIS sequence:
// http://oeis.org/A006877

#include <stdio.h>

long int collatz(long int n) {
    if (n % 2 == 0) {
        return n / 2;
    }
    else {
        return 3 * n + 1;
    }
}

int main() {
    int max_chain = 0;
    long int max_number = 0;
    int chain = 0;

    for (int i = 2; i < 1000000; i++) {
        // if (i % 100000 == 0) printf("%d\n", i);

        long int n = i;
        chain = 1;
        while (n != 1) {
            n = collatz(n);
            chain++;
            if (chain > max_chain) {
                max_chain = chain;
                max_number = i;
            }
        }
    }

    printf("%ld with a chain of length %d\n", max_number, max_chain);
    printf("%ld\n", max_number);

    return 0;
}
