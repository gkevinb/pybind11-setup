import time
import simple


def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)


n = 35

start_time = time.time()
a = fibonacci(n)
end_time = time.time()

elapsed_time_python = end_time - start_time

print(f"Answer: {a}, Time elapsed for n = {n}: {elapsed_time_python:.6f} seconds")

start_time = time.time()
a = simple.fibonacci(n)
end_time = time.time()

elapsed_time_cpp = end_time - start_time

print(f"Answer: {a}, Time elapsed for n = {n}: {elapsed_time_cpp:.6f} seconds")


print(f"Speedup: {elapsed_time_python / elapsed_time_cpp:.2f}x")