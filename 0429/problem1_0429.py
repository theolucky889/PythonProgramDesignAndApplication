def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
# Print factorial 1 - 25
for i in range(1, 26):
    result = factorial(i)
    print(f"{i}! = {result}")
