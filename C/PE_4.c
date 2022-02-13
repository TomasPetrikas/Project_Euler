// Largest palindrome product
//
// https://projecteuler.net/problem=4

#include <stdbool.h>
#include <stdio.h>

int is_palindrome(int n) {
    int original = n;
    int reversed = 0;
    int remainder;

    while (n != 0) {
        remainder = n % 10;
        reversed = reversed * 10 + remainder;
        n /= 10;
    }

    if (original == reversed) {
        return true;
    }
    else {
        return false;
    }
}

int main() {
    int x = 0;
    int largest = 0;
    int largest1, largest2;

    for (int i = 900; i < 1000; i++) {
        for (int j = 900; j < 1000; j++) {
            x = i * j;
            if (is_palindrome(x) == true && x > largest) {
                largest = x;
                largest1 = i;
                largest2 = j;
            }
        }
    }

    printf("%d * %d = %d\n", largest1, largest2, largest);
    printf("%d\n", largest);

    return 0;
}
