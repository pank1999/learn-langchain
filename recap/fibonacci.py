# program to generate Fibonacci sequence up to n
def fib(n):
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result

if __name__ == "__main__":
    n = int(input("Enter a number: "))
    print(fib(n))
    
