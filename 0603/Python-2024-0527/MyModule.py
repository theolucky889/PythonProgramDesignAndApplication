# 使用者自行定義的常數與函式

# 自定常數:
pi = 3.14159

# 字串版本的乘法表:
def table9x9():
    result = ""
    for r in range(1, 10):
        for c in range(1, 10):
            if c == 1:
                result += f"{r}x{c}={r*c} "
            else:
                result += f"{r}x{c}={r*c:2} "
        result += '\n'
        
    print(result)

# 顯示 __name__ 內容的函式:
def about():
    print(__name__, "in MyModule.py")
    
    
# 測試函式的功能是否正確:
if __name__ == "__main__":
    about()

    print(f"pi = {pi}")

    table9x9()