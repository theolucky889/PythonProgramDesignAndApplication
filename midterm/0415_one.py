file_path = r"C:\Users\CNC\Downloads\109990007.txt"

with open(file_path, 'r', encoding='utf-8') as file:
    msg = file.read().strip() 

for i in range(len(msg)):
    rotated_msg = msg[-i:] + msg[:-i]
    print(rotated_msg)
