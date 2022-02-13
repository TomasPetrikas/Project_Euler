// Largest prime factor
//
// https://projecteuler.net/problem=3

#include <stdio.h>

int main() {
    long int n = 600851475143;

    int i = 2;
    int largest = 0;
    while (i * i <= n) {
        if (n % i != 0) {
            i++;
        }
        else {
            n /= i;
            largest = i;
        }
    }
    if (n > largest) largest = n;

    printf("%d\n", largest);

    return 0;
}
