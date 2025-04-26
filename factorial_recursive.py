# factorial_recursive.py
# Calculate factorial using recursion.

def factorial_recursive(n):
    # base case: 0 or 1 gives 1
    if n <= 1:
        return 1
    # otherwise multiply n by factorial of n-1
    return n * factorial_recursive(n - 1)

if __name__ == "__main__":
    n = int(input("Enter a non-negative integer: "))
    if n < 0:
        print("Can't do factorial for negative!")
    else:
        print(n, "! =", factorial_recursive(n))
