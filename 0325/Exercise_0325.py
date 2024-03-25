# 1
def string_length(msg):
    length = 0
    for m in msg:
        if ord(m) < 128:
            length += 1
        else:
            length += 2
    
    return length
string_length("abc北科大")	

# 2
msg = "EECS109990007鄧仲淵"
def string_length(msg):
    length = 0
    for m in msg:
        if ord(m) < 128:
            length += 1
        else:
            length += 2
    return length
n = len(msg)
for i in range( len(msg) ):
    print(' ' * ((string_length(msg[0:(len(msg)- i - 1)]))), end=' ')
    print(f"{msg[-(i+1):]}")

    # 3
namestr = "林豐祥、伊姿和、唐雅婷、陳弘婷、杜淑娟、曹俐火、王郁婷、吳鈺桂、陳瑞瑜、郭志豪、郭天芝"
names = namestr.split('、')

surnames = [name[0] for name in names]
surnames.sort()

surname_counts = {}
for surname in surnames:
    if surname in surname_counts:
        surname_counts[surname] += 1
    else:
        surname_counts[surname] = 1

for surname, count in surname_counts.items():
    print(f"{surname}: {count}")
