'''
Problem 1:
將一個任意長度串列，並依每列指定的行數來將串列內容呈現出來。

def show_list(lst, cols):
    pass
    
請隨機生成一個長度在 20 ~ 30 間的串列，同時將元素內容以隨機產生的數值填入，數值範圍為 1 ~ 99。
接著呼叫上述函式來將串列的內容顯示出來。
例如，假設已經產生的隨機串列 lst 內容如下:
lst = [86, 27, 7, 26, 30, 85, 88, 77, 80, 60, 97, 88, 42, 46, 61, 58, 14, 15, 88, 5, 66, 89, 8, 55, 11]

1) 呼叫 show_list(lst, 5)，的輸出結果:
86 27  7 26 30 
85 88 77 80 60 
97 88 42 46 61 
58 14 15 88  5 
66 89  8 55 11 

---------------
2) 呼叫 show_list(lst, 7)，的輸出結果:
86 27  7 26 30 85 88 
77 80 60 97 88 42 46 
61 58 14 15 88  5 66 
89  8 55 11 
'''
import random as rand
lst = [rand.randint(1, 99) for _ in range(rand.randint(20, 30))]

def show_list (lst, cols):
    for i, num in enumerate(lst):
        print(f"{num:2d}", end=" ")
        
        if (i + 1) % cols == 0:
            print()
    if len(lst) % cols !=0:
        print()
        
print("Show list 5 columns: ")
show_list(lst, 5)
print("\nShow list with 7 columns: ")
show_list(lst, 7)


'''
Problem 2:
請寫一個函式，讓使用者輸入年與月的資料後，印出該給定年月的月曆。
其中，年份的值可以是民國年或西元年，但預設為民國年。
def month_calendar(year, month=1, chinese=true):
	pass

接著請使用該函式，印出本月份的月曆，以及你出生那個月的月曆。

1) 閏年的判斷: 自行撰寫 is_leap(year)，回傳 True 或 False。
   閏年: 1) 西元年可以被 400 整除
         2) 西元年可以被 4 整除，而且不能被 100 整除、
         上述條件，只要其中一個成立即可。
         
2) 請寫一個函式或是定義一個串列，可以回傳或記錄每個月共有多少天。
   其中，如果該年是閏年的話，二月的天數會是29天。
   請測試下列月份:
   2000,2
   2024,2
   2024,3
   2024,4
   
3) 完成下列月曆內容的輸出:
   (1) 月份名稱(使用英文)置中輸出。
   (2) 星期名稱各佔三位，靠右對齊。
   (3) 指定月份的日期輸出，也是各佔三位，靠右對齊。

例如，以 2024 年 2 月為例，該月份的月曆輸出如下:
         February          
Sun Mon Tue Wed Thr Fri Sat
                 1   2   3  
 4   5   6   7   8   9  10  
11  12  13  14  15  16  17  
18  19  20  21  22  23  24  
25  26  27  28  29 
'''
def is_leap(year):
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        return True
    else:
        return False

def get_days_in_month(year, month):
    if month == 2:
        return 29 if is_leap(year) else 28
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    else:
       return 30
    
def calculate_day_of_week(year, month, day):
    if month < 3:
        month += 12
        year -= 1
    a = year % 100
    b = year // 100
    c = day + 13 * (month + 1) // 5 + a + a // 4 - 2 * b + b // 4
    return (c + 7) % 7

def month_calendar(year, month=1, chinese=True):
    if chinese:
        year += 1911
    
    month_names = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    print(month_names[month - 1].center(20))
    
    print("Sun Mon Tue Wed Thu Fri Sat")
    
    start_day = calculate_day_of_week(year, month, 1)
    
    adjusted_start_day = (start_day + 6) % 7
    
    print("    " * adjusted_start_day, end="")
        
    for days in range(1, get_days_in_month(year, month) + 1):
        print(f"{days:3} ", end ="")
        if ((days + adjusted_start_day) % 7 == 0):
            print()
    if ((days + adjusted_start_day) % 7 != 0):
        print()

year = int(input("Enter a year(ROC or Gregorian): "))
month = int(input("Enter a month (1-12): "))
calendar_type = input("Is the year in ROC format? (yes/no): ").lower()
chinese = calendar_type == "yes"

month_calendar(year, month, chinese)