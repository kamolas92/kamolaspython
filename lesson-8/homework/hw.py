##homework8
#1.
try:
    1/0
except ZeroDivisionError:
    print("ZeroDivisonerror")

#2.
# def get_integer():
#     user_input = input("enter an integer: ")
#     try:
#         return int(user_input)
#     except ValueError:
#         raise ValueError('not integer-ku!')
# # Run the function
# get_integer()
try:
    int('Husan aka')
except Exception:
    print('not integerku')


#3.
# Python program to open a file and handle FileNotFoundError

filename = input("Enter the name of the file to open: ")

try:
    with open(filename, 'r') as file:
        content = file.read()
        print("\nFile content:")
        print(content)
except FileNotFoundError:
    print(f"\nError: The file '{filename}' was not found.")

#4.
# Python program to prompt for two numbers and raise TypeError if not numeric

def get_number(prompt):
    user_input = input(prompt)
    if not user_input.replace('.', '', 1).isdigit():
        raise TypeError(f"Invalid input '{user_input}': Input must be a number.")
    return float(user_input)

try:
    num1 = get_number("Enter the first number: ")
    num2 = get_number("Enter the second number: ")
    print(f"\nYou entered: {num1} and {num2}")
    print(f"Their sum is: {num1 + num2}")
except TypeError as e:
    print(f"\nError: {e}")

#5.
# Python program to open a file and handle PermissionError

filename = input("Enter the name of the file to open: ")

try:
    with open(filename, 'r') as file:
        content = file.read()
        print("\nFile content:")
        print(content)
except PermissionError:
    print(f"\nError: You do not have permission to read the file '{filename}'.")

#6.
# Python program to handle IndexError when accessing a list

my_list = ['apple', 'banana', 'cherry', 'date']

print("List contents:", my_list)

try:
    index = int(input("Enter an index to access an element from the list: "))
    print(f"The element at index {index} is: {my_list[index]}")
except IndexError:
    print("\nError: The index you entered is out of range.")
except ValueError:
    print("\nError: Please enter a valid integer index.")

#7.
# Python program to handle KeyboardInterrupt during input

try:
    number = float(input("Please enter a number: "))
    print(f"\nYou entered: {number}")
except KeyboardInterrupt:
    print("\n\nInput cancelled by user (KeyboardInterrupt).")
except ValueError:
    print("\nInvalid input. Please enter a valid number.")

#8.
# Python program to handle ArithmeticError during division

try:
    numerator = float(input("Enter the numerator: "))
    denominator = float(input("Enter the denominator: "))
    result = numerator / denominator
    print(f"\nResult: {numerator} / {denominator} = {result}")
except ArithmeticError as e:
    print(f"\nArithmetic error occurred: {e}")
except ValueError:
    print("\nInvalid input. Please enter numeric values.")

#9.
# Python program to handle UnicodeDecodeError when reading a file

filename = input("Enter the filename to open: ")

try:
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
        print("\nFile content:")
        print(content)
except UnicodeDecodeError:
    print(f"\nError: The file '{filename}' contains characters that could not be decoded using UTF-8 encoding.")
except FileNotFoundError:
    print(f"\nError: The file '{filename}' does not exist.")
except PermissionError:
    print(f"\nError: You do not have permission to open the file '{filename}'.")

#10.
# Python program to handle AttributeError on list operations

my_list = [1, 2, 3, 4, 5]

try:
    # Intentionally calling a non-existent method to raise AttributeError
    my_list.push(6)  # Lists have 'append()', not 'push()'
except AttributeError as e:
    print(f"\nAttributeError occurred: {e}")

#filehandling
#1.
# Python program to read an entire text file

filename = input("Enter the name of the text file to read: ")

try:
    with open(filename, 'r') as file:
        content = file.read()
        print("\n--- File Content ---")
        print(content)
except FileNotFoundError:
    print(f"\nError: The file '{filename}' was not found.")
except PermissionError:
    print(f"\nError: You do not have permission to read the file '{filename}'.")

#2.
# Python program to read the first n lines of a file

filename = input("Enter the name of the file: ")
try:
    n = int(input("Enter the number of lines to read: "))
    
    with open(filename, 'r') as file:
        print(f"\n--- First {n} lines of '{filename}' ---")
        for i in range(n):
            line = file.readline()
            if not line:  # End of file reached
                break
            print(line.strip())
except FileNotFoundError:
    print(f"\nError: The file '{filename}' was not found.")
except PermissionError:
    print(f"\nError: You do not have permission to read the file '{filename}'.")
except ValueError:
    print("\nError: Please enter a valid number.")

#3.
# Python program to append text to a file and display the text

filename = input("Enter the name of the file: ")

try:
    text_to_append = input("Enter the text to append to the file: ")

    # Append text to the file
    with open(filename, 'a') as file:
        file.write(text_to_append + '\n')

    # Read and display the file content
    print(f"\n--- Content of '{filename}' after appending ---")
    with open(filename, 'r') as file:
        content = file.read()
        print(content)

except FileNotFoundError:
    print(f"\nError: The file '{filename}' was not found.")
except PermissionError:
    print(f"\nError: You do not have permission to modify the file '{filename}'.")

#4.
# Python program to read the last n lines of a file

filename = input("Enter the name of the file: ")

try:
    n = int(input("Enter the number of lines to read from the end: "))

    with open(filename, 'r') as file:
        lines = file.readlines()  # Read all lines into a list
        total_lines = len(lines)

        print(f"\n--- Last {n} line(s) of '{filename}' ---")
        for line in lines[-n:]:
            print(line.strip())

except FileNotFoundError:
    print(f"\nError: The file '{filename}' was not found.")
except PermissionError:
    print(f"\nError: You do not have permission to read the file '{filename}'.")
except ValueError:
    print("\nError: Please enter a valid number.")

#5. Python program to read a file line by line and store it into a list

filename = input("Enter the name of the file: ")

try:
    with open(filename, 'r') as file:
        lines_list = [line.strip() for line in file]  # Read and strip each line

    print("\n--- Lines stored in the list ---")
    for line in lines_list:
        print(line)

except FileNotFoundError:
    print(f"\nError: The file '{filename}' was not found.")
except PermissionError:
    print(f"\nError: You do not have permission to read the file '{filename}'.")

#6.
# Python program to read a file line by line and store it into a list variable

filename = input("Enter the name of the file: ")

try:
    with open(filename, 'r') as file:
        lines = file.readlines()  # Each line is a list element

    print("\n--- Lines stored in the 'lines' variable ---")
    for line in lines:
        print(line.strip())
except FileNotFoundError:
    print(f"\nError: The file '{filename}' was not found.")
except PermissionError:
    print(f"\nError: You do not have permission to read the file '{filename}'.")

#7.
# Python program to read a file line by line and store it into an array (list)

filename = input("Enter the name of the file: ")

try:
    with open(filename, 'r') as file:
        lines_array = [line.strip() for line in file]  # Read and strip each line

    print("\n--- Lines stored in array (list) ---")
    for line in lines_array:
        print(line)

except FileNotFoundError:
    print(f"\nError: The file '{filename}' was not found.")
except PermissionError:
    print(f"\nError: You do not have permission to read the file '{filename}'.")

#8. Python program to find the longest word(s) in a file

filename = input("Enter the name of the file: ")

try:
    with open(filename, 'r') as file:
        words = file.read().split()  # Split entire file into words

    if not words:
        print("The file is empty or contains no words.")
    else:
        max_length = max(len(word) for word in words)
        longest_words = [word for word in words if len(word) == max_length]

        print(f"\nLongest word(s) with length {max_length}:")
        for word in longest_words:
            print(word)
except FileNotFoundError:
    print(f"\nError: The file '{filename}' was not found.")
except PermissionError:
    print(f"\nError: You do not have permission to read the file '{filename}'.")

#9.
# Python program to count the number of lines in a text file

filename = input("Enter the name of the file: ")

try:
    with open(filename, 'r') as file:
        line_count = sum(1 for line in file)

    print(f"\nThe file '{filename}' has {line_count} line(s).")

except FileNotFoundError:
    print(f"\nError: The file '{filename}' was not found.")
except PermissionError:
    print(f"\nError: You do not have permission to read the file '{filename}'.")

#10.
# Python program to count the frequency of words in a file

from collections import Counter
import re

filename = input("Enter the name of the file: ")

try:
    with open(filename, 'r') as file:
        text = file.read().lower()  # Read the file and convert to lowercase

    # Use regex to find all words (ignores punctuation)
    words = re.findall(r'\b\w+\b', text)

    word_counts = Counter(words)

    print("\n--- Word Frequency ---")
    for word, count in word_counts.items():
        print(f"{word}: {count}")

except FileNotFoundError:
    print(f"\nError: The file '{filename}' was not found.")
except PermissionError:
    print(f"\nError: You do not have permission to read the file '{filename}'.")

#11.
# Python program to get the file size of a plain file

import os

filename = input("Enter the name of the file: ")

try:
    size = os.path.getsize(filename)
    print(f"\nThe size of '{filename}' is {size} bytes.")
except FileNotFoundError:
    print(f"\nError: The file '{filename}' was not found.")
except PermissionError:
    print(f"\nError: You do not have permission to access the file '{filename}'.")

#12.
# Python program to write a list to a file

filename = input("Enter the name of the file to write to: ")

# Example list
items = ['Apple', 'Banana', 'Cherry', 'Date', 'Elderberry']

try:
    with open(filename, 'w') as file:
        for item in items:
            file.write(item + '\n')

    print(f"\nList has been written to '{filename}' successfully.")
except PermissionError:
    print(f"\nError: You do not have permission to write to '{filename}'.")

#13.
# Python program to copy the contents of a file to another file

source_file = input("Enter the source file name: ")
destination_file = input("Enter the destination file name: ")

try:
    with open(source_file, 'r') as src:
        content = src.read()

    with open(destination_file, 'w') as dest:
        dest.write(content)

    print(f"\nContents copied from '{source_file}' to '{destination_file}' successfully.")

except FileNotFoundError:
    print(f"\nError: The file '{source_file}' was not found.")
except PermissionError:
    print(f"\nError: You do not have permission to access one of the files.")

#14.
# Python program to combine each line from two files

file1 = input("Enter the first file name: ")
file2 = input("Enter the second file name: ")

try:
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        print("\n--- Combined Lines ---")
        for line1, line2 in zip(f1, f2):
            combined_line = line1.strip() + " " + line2.strip()
            print(combined_line)

except FileNotFoundError as e:
    print(f"\nError: {e.filename} was not found.")
except PermissionError:
    print(f"\nError: You do not have permission to access one of the files.")

#15.# Python program to read a random line from a file

import random

filename = input("Enter the name of the file: ")

try:
    with open(filename, 'r') as file:
        lines = file.readlines()

    if not lines:
        print("\nThe file is empty.")
    else:
        random_line = random.choice(lines)
        print("\nRandom line from the file:")
        print(random_line.strip())

except FileNotFoundError:
    print(f"\nError: The file '{filename}' was not found.")
except PermissionError:
    print(f"\nError: You do not have permission to read the file '{filename}'.")

#16.
# Python program to assess if a file is closed or not

filename = input("Enter the name of the file: ")

try:
    file = open(filename, 'r')
    print(f"\nIs the file '{filename}' closed? {file.closed}")  # Should be False

    # Do something with the file (optional)
    content = file.read()

    # Close the file manually
    file.close()

    print(f"Is the file '{filename}' closed after calling close()? {file.closed}")  # Should be True

except FileNotFoundError:
    print(f"\nError: The file '{filename}' was not found.")
except PermissionError:
    print(f"\nError: You do not have permission to access the file '{filename}'.")

#17.
# Python program to remove newline characters from a file and print the result

filename = input("Enter the name of the file: ")

try:
    with open(filename, 'r') as file:
        content = file.read().replace('\n', '')  # Remove all newline characters

    print("\n--- File content without newlines ---")
    print(content)

except FileNotFoundError:
    print(f"\nError: The file '{filename}' was not found.")
except PermissionError:
    print(f"\nError: You do not have permission to read the file '{filename}'.")

#18.
# Python program to count the number of words in a text file

filename = input("Enter the name of the text file: ")

try:
    with open(filename, 'r') as file:
        text = file.read()
        words = text.split()  # Split by any whitespace
        word_count = len(words)

    print(f"\nThe file '{filename}' contains {word_count} word(s).")

except FileNotFoundError:
    print(f"\nError: The file '{filename}' was not found.")
except PermissionError:
    print(f"\nError: You do not have permission to read the file '{filename}'.")

#19.
# Python program to extract characters from multiple text files and store them in a list

import os

# Ask the user to enter file names separated by commas
file_names = input("Enter the text file names (separated by commas): ").split(',')

# Strip whitespace from each filename
file_names = [name.strip() for name in file_names]

char_list = []

for filename in file_names:
    try:
        with open(filename, 'r') as file:
            content = file.read()
            char_list.extend(list(content))  # Add each character to the list
        print(f"Characters extracted from '{filename}'")
    except FileNotFoundError:
        print(f"\nError: File '{filename}' was not found.")
    except PermissionError:
        print(f"\nError: You do not have permission to read file '{filename}'.")

# Display result
print("\n--- All characters extracted into the list ---")
print(char_list)

#20.
# Python program to generate 26 text files named A.txt to Z.txt

import string

for letter in string.ascii_uppercase:  # 'A' to 'Z'
    filename = f"{letter}.txt"
    try:
        with open(filename, 'w') as file:
            file.write(f"This is file {filename}\n")
        print(f"Created {filename}")
    except Exception as e:
        print(f"Error creating {filename}: {e}")

#21.
# Python program to write the alphabet to a file with specified letters per line

import string

filename = input("Enter the name of the file to create: ")
letters_per_line = int(input("Enter the number of letters per line: "))

alphabet = string.ascii_lowercase  # or use string.ascii_uppercase for uppercase

try:
    with open(filename, 'w') as file:
        for i in range(0, len(alphabet), letters_per_line):
            line = alphabet[i:i + letters_per_line]
            file.write(line + '\n')

    print(f"\nFile '{filename}' created with {letters_per_line} letters per line.")
except Exception as e:
    print(f"\nError: {e}")
