# 1
n = 5
count = 0
over_60 = ">= 60:"
less_60 = "< 60:"

while count < n:
    inp = input(f"number {count + 1}:")
    value = int(inp)
    if value >= 60:
        over_60 = over_60 + f" {str(value)}"
    else:
        less_60 += f" {str(value)}"
    count = count + 1 # count += 1
print(">= 60:", over_60)
print(" < 60:", less_60)

#2
# Defining a function to print the desired text pattern

def print_number_pattern():
    for i in range(1, 6):  # Looping from 1 to 5
        # Constructing and printing the string for each line
        print("".join(str(j) for j in range(1, i + 1)))
print_number_pattern()
        

# 3
# Defining a function to print the desired text pattern

def print_inverted_number_pattern():
    for i in range(9, 0, -1):  # Looping from 9 to 1
        # Constructing each line by combining spaces and numbers
        line = ' ' * (i - 1) + ''.join(str(j) for j in range(i, 10))
        print(line)
print_inverted_number_pattern()
        

# 4
# Defining a function to print the desired text pattern based on the given message

def print_rotated_message(msg):
    for i in range(len(msg)):
        # Rotate the string by slicing and concatenating
        rotated_msg = msg[-i:] + msg[:-i]
        print(rotated_msg)

# Test message
test_msg = "台北科技大學不分系王大同"

print_rotated_message(test_msg)
