image_links = [
    "https://stats.moe.gov.tw/bookcase/smallpic/Higher/113.png",
    "https://stats.moe.gov.tw/bookcase/smallpic/High/113.png",
    "https://stats.moe.gov.tw/bookcase/smallpic/Basic/113.png",
    "https://stats.moe.gov.tw/bookcase/smallpic/Oversea/113.png",
    "https://stats.moe.gov.tw/bookcase/smallpic/Native/113.png",
    "https://stats.moe.gov.tw/bookcase/smallpic/Son_of_Foreign_All/113.png",
    "https://stats.moe.gov.tw/bookcase/smallpic/International_Comparison/112.png",
    "https://stats.moe.gov.tw/bookcase/smallpic/Education_Statistics/112.png",
    "https://stats.moe.gov.tw/bookcase/smallpic/Education_in_Taiwan/112.png",
    "https://stats.moe.gov.tw/bookcase/smallpic/High_Graduate/112.png"
]

html_content = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ebook Display</title>
    <style>
        table {{
            width: 100%;
            border-collapse: collapse;
        }}
        td {{
            border: 1px solid #ccc;
            padding: 10px;
            text-align: center;
        }}
        img {{
            width: 100%;
            max-width: 200px;  # Control the size to be uniform
            height: auto;
        }}
    </style>
</head>
<body>
    <table>
        <tr>
            <td><img src="{0}" alt="Book 1"></td>
            <td><img src="{1}" alt="Book 2"></td>
            <td><img src="{2}" alt="Book 3"></td>
            <td><img src="{3}" alt="Book 4"></td>
            <td><img src="{4}" alt="Book 5"></td>
        </tr>
        <tr>
            <td><img src="{5}" alt="Book 6"></td>
            <td><img src="{6}" alt="Book 7"></td>
            <td><img src="{7}" alt="Book 8"></td>
            <td><img src="{8}" alt="Book 9"></td>
            <td><img src="{9}" alt="Book 10"></td>
        </tr>
    </table>
</body>
</html>
'''.format(*image_links)

output_file = '109990007.html'

with open(output_file, 'w') as file:
    file.write(html_content)

print(f"HTML file has been created at {output_file}")
