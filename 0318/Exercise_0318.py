# 1
# Defining a function to categorize and print scores based on the given criteria

def categorize_scores(scores):
    # Lists to hold categorized scores
    ge_60 = []  # Scores greater than or equal to 60
    lt_60 = []  # Scores less than 60

    # Iterate over the scores to categorize them
    for score in scores:
        if score >= 60:
            ge_60.append(score)
        else:
            lt_60.append(score)
    
    # Returning the categorized scores
    return ge_60, lt_60

# Simulating the input scores
input_scores = [48, 67, 52, 79, 94]

# Categorizing and retrieving the scores
greater_equal_60, less_than_60 = categorize_scores(input_scores)
print(">= 60:", greater_equal_60)
print(" < 60:", less_than_60)

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
