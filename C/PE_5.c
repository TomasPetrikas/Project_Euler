// Smallest multiple
//
// https://projecteuler.net/problem=5

// OEIS sequence:
// https://oeis.org/A003418

#include <stdio.h>
#include <stdlib.h>

int main() {
    int x = 2520;

    while(1) {
        for (int i = 2; i <= 20; i++) {
            if (x % i != 0) {
                break;
            }
            else if (i == 20) {
                printf("%d\n", x);
                exit(0);
            }
        }

        x += 2520;
    }

    return 0;
}
