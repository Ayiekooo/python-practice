# factorial_loop.py
# Calculate factorial with a loop.

def factorial_loop(n):
    # start result at 1
    result = 1
    # multiply by each number from 2 up to n
    for i in range(2, n + 1):
        result *= i
    return result

if __name__ == "__main__":
    n = int(input("Enter a non-negative integer: "))
    if n < 0:
        print("No factorial for negative numbers!")
    else:
        print(n, "! =", factorial_loop(n))
