import os
import zipfile

with zipfile.ZipFile('Pictures.zip', 'r') as f:
    f.extractall('Pictures')

imgs = [f for f in os.listdir('C:/Users/CNC/Downloads/Python-2024-0527/Python-2024-0527/Pictures') if f.lower().endswith(('.jpg', '.avif', 'webp'))]

html = ''

for img in imgs:
    html += f'<img src="./Pictures/{img}" height=250px">'

with open('index.html', 'w') as f:
    f.write(html)