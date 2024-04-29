def fibonacci(n):
    if n <= 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# print fibonacci numbers
print("Fibonacci numbers: ", end="")
for i in range(10):  # adjust the range of fibonacci numbers
    print(fibonacci(i), end=",")
