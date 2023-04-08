#include "simple.h"


int fibonacci(int n) {
    if (n < 2) {
        return n;
    }
    return fibonacci(n - 1) + fibonacci(n - 2);
}

double leibnizPi(int n) {
    double pi = 0;
    int sign = 1;
    for (int i = 0; i < n; i++) {
        double term = sign / (2.0*i + 1);
        pi += term;
        sign = -sign;
    }
    return pi * 4;
}