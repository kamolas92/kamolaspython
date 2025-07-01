# math_operations.py

def add(a, b):
    """Ikki sonni qo‘shish"""
    return a + b

def subtract(a, b):
    """Ikki sonni ayirish"""
    return a - b

def multiply(a, b):
    """Ikki sonni ko‘paytirish"""
    return a * b

def divide(a, b):
    """Ikki sonni bo‘lish"""
    if b == 0:
        raise ValueError("Bo‘luvchi 0 bo‘lmasligi kerak.")
    return a / b

# string_utils.py

def reverse_string(s):
    """Berilgan matnni teskarisiga o‘giradi"""
    return s[::-1]

def count_vowels(s):
    """Matndagi unli harflar sonini hisoblaydi"""
    vowels = 'aeiouAEIOU'
    return sum(1 for char in s if char in vowels)


# main.py

from math_operations import add, subtract, multiply, divide
from string_utils import reverse_string, count_vowels

# Matematika funksiyalari
print("5 + 3 =", add(5, 3))
print("10 - 4 =", subtract(10, 4))
print("6 * 7 =", multiply(6, 7))
print("20 / 4 =", divide(20, 4))

# Matn funksiyalari
text = "Salom Dunyo"
print("Reverse:", reverse_string(text))
print("Unli harflar soni:", count_vowels(text))








your_project/
├── geometry/
│   ├── __init__.py
│   └── circle.py
│
├── file_operations/
│   ├── __init__.py
│   ├── file_reader.py
│   └── file_writer.py
│
└── main.py

# geometry/circle.py
import math

def calculate_area(radius):
    """Doira yuzini hisoblaydi"""
    return math.pi * radius ** 2

def calculate_circumference(radius):
    """Doira uzunligini hisoblaydi"""
    return 2 * math.pi * radius

# file_operations/file_reader.py

def read_file(file_path):
    """Fayldan matnni o‘qib, string sifatida qaytaradi"""
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()
    
# file_operations/file_writer.py

def write_file(file_path, content):
    """Matnni faylga yozadi"""
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)


# main.py

from geometry.circle import calculate_area, calculate_circumference
from file_operations.file_writer import write_file
from file_operations.file_reader import read_file

# Doira hisoblari
radius = 5
area = calculate_area(radius)
circumference = calculate_circumference(radius)

print("Radius:", radius)
print("Yuza:", area)
print("Perimetr:", circumference)

# Faylga yozamiz
file_path = "circle_result.txt"
content = f"Radius: {radius}\nArea: {area:.2f}\nCircumference: {circumference:.2f}"
write_file(file_path, content)

# Fayldan o‘qiymiz
print("\nYozilgan fayl mazmuni:")
print(read_file(file_path))
