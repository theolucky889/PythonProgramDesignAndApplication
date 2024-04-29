def show_fib(n):
    if n <= 0:
        return None
    fib_sequence = []
    a, b = 1, 1
    for i in range(n):
        if i < 2:
            fib_sequence.append(1)
        else:
            a, b = b, a + b
            fib_sequence.append(b)
    return fib_sequence

while True:
    n = int(input("請輸入要顯示幾項的 Fibonacci 數列: "))
    if n <= 0:
        print("請重新輸入！")
    else:
        fib_list = show_fib(n)
        print(fib_list)
        break
