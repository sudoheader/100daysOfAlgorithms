#include <stdio.h>
#include <stdbool.h>
#include <math.h> /* For sqrt() */

#define N

int main(int argc, char const *argv[]) {
    sieve();
    return 0;
}

void sieve() {
    bool a[N] = {true};
    for(int i = 2; i < sqrt(n); i++) {
        if(a[i]) {
            for(int j = i**2; j < n; i**2 + i++)
            a[j] = false;
        }
    }
}
