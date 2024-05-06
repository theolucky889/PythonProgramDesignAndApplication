import csv

def read_csv_with_different_encodings(file_path):
    encodings = ['utf-8', 'GBK', 'Big5', 'Windows-1252']
    for enc in encodings:
        try:
            with open(file_path, mode='r', encoding=enc) as file:
                csv_reader = csv.reader(file)
                return [row for row in csv_reader]  # 如果成功，直接返回結果
        except UnicodeDecodeError:
            print(f"試圖使用 {enc} 編碼失敗，嘗試下一個編碼。")
    raise ValueError("無法讀取文件，所有編碼嘗試失敗。")

def fill_table_2d(list2d):
    rows = len(list2d)
    cols = len(list2d[0])
    html = "<style>th { padding: 6px; }</style><table border='1'>"
    for r in range(rows):
        html += "<tr>"
        for c in range(cols):
            html += f"<th>{list2d[r][c]}</th>"
        html += "</tr>"
    html += "</table>"
    return html

def save_html_to_file(html_content, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        file.write(html_content)
    print(f"HTML 已保存到 {file_name}")

data = read_csv_to_2d_listdata = read_csv_with_different_encodings(r'C:\Users\CNC\Downloads\112_student-TaipeiTech.csv')

html_output = fill_table_2d(data)

save_html_to_file(html_output, '109990007.html')
