#include <stdio.h>
#include <stdlib.h>

void swap(int *x, int *y) {
    int u = *x, v = *y;
    int s = (u - v) >> (sizeof(int) * 8 - 1);
    *x = v * (1 + s) - u * s;
    *y = u * (1 + s) - v * s;
}

int main(int argc, char *argv[]) {
    int a = 3;
    int b = 15;
    int c = -13;
    int d = 5;
    int *p = &a;
    int *q = &b;
    int *r = &c;
    int *s = &d;
    swap(&a, &b), swap(&b, &a);
    swap(&c, &d), swap(&d, &c);
}
