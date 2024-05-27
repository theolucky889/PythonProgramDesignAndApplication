import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

url = 'https://stats.moe.gov.tw/bookcase/'
r = requests.get(url)

html_content = r.text

s = BeautifulSoup(html_content, 'html.parser')

img_tags = s.find_all('img', class_='datalistImg')

image_links = [urljoin(url, img['src']) for img in img_tags]
book_links = [urljoin(url, img.find_parent('a')['href']) for img in img_tags]

table = '<table>'
for i in range(0, len(image_links), 5):
    table += '<tr>'
    for img_link, book_link in zip(image_links[i:i+5], book_links[i:i+5]):
        table += f"<td><a href='{book_link}' target='_blank'><img src='{img_link}' height='250'></a></td>"
    table += '</tr>'
table += '</table>'

with open('109990007_hw2.html', 'w') as f:
    f.write(table)

