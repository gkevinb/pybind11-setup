import timeit

import simple

def leibniz_pi(n):
    pi = 0
    sign = 1
    for i in range(n):
        term = sign / (2*i + 1)
        pi += term
        sign = -sign
    return pi * 4

# Benchmark the leibniz_pi function by running it 100000 times
n = 1000000

print(leibniz_pi(100))
print(leibniz_pi(1000))
print(leibniz_pi(10000))

elapsed_time_python = timeit.timeit(lambda: leibniz_pi(1000), number=n)

print(f"Time elapsed for {n} runs: {elapsed_time_python:.6f} seconds")

elapsed_time_cpp = timeit.timeit(lambda: simple.leibniz_pi(1000), number=n)

print(f"Time elapsed for {n} runs: {elapsed_time_cpp:.6f} seconds")


print(f"Speedup: {elapsed_time_python / elapsed_time_cpp:.2f}x")