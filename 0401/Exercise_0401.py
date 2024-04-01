constellation_dates = {
    '魔羯座': "12.22~1.19",
    '水瓶座': "1.20~2.18",
    '雙魚座': "2.19~3.20",
    '牡羊座': "3.21~4.19",
    '金牛座': "4.20~5.20",
    '雙子座': "5.21~6.20",
    '巨蟹座': "6.21~7.22",
    '獅子座': "7.23~8.22",
    '處女座': "8.23~9.22",
    '天秤座': "9.23~10.22",
    '天蠍座': "10.23~11.21",
    '射手座': "11.22~12.21",
}

def get_constellation(month, day):
    for constellation, date_range in constellation_dates.items():
        start_month, start_day, end_month, end_day = map(int, date_range.replace('~', '.').split('.'))

        if (month == start_month and day >= start_day) or (month == end_month and day <= end_day):
            return constellation, f'{start_month}.{start_day} ~ {end_month}.{end_day}'
       
        if start_month > end_month:
            if (month == start_month and day >= start_day) or (month == 1 and day <= end_day):
                return constellation, f'{start_month}.{start_day} ~ {end_month}.{end_day}'
            
    return None, None
    
month = int(input('Enter a month (in numbers): '))
date = int(input('Enter a Date (in numbers): '))
constellation, date_range = get_constellation(month, date)
print(f'Your Constellation is {constellation}: ({date_range})')


def group_names_surname(namestr):
    names = namestr.split('、')
    surname_dict = {}

    for name in names:
        surname = name[0]
        given_name = name[1:]

        if surname in surname_dict:
            surname_dict[surname].append(given_name)
        else:
            surname_dict[surname] = [given_name]
            
    return surname_dict

def print_name(surname_dict):
    for surname, given_names in surname_dict.items():
        print(f'{surname}: {", ".join(given_names)}')

namestr = "廖靜宜、吳百凱、陳懿沛、蔡仁芸、王彥君、陳鈺瑋、林珊群、許萬昌、黃靜東、陳佩舜、林怡喜"
surname_dict = group_names_surname(namestr)
print_name(surname_dict)



