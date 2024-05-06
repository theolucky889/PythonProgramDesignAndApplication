def create_2d_list():
    return [[5 * r + c + 1 for c in range(5)] for r in range(4)]

matrix = create_2d_list()
print(matrix)

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

html_output = fill_table_2d(matrix)
print(html_output)

def save_html_to_file(html_content, file_name):
    with open(file_name, 'w') as file:
        file.write(html_content)
    print(f"HTML 已保存到 {file_name}")

html_output = fill_table_2d(matrix)

save_html_to_file(html_output, 'table_output.html')
