#1.
def is_leap(year):
    if not isinstance(year, int):
        raise ValueError("Year must be an integer.")

    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
print(is_leap(1999))
print(is_leap(2020))
#2.
def check_weird(n):
    if n % 2 != 0:
        print("Weird")
    elif 2 <= n <= 5:
        print("Not Weird")
    elif 6 <= n <= 20:
        print("Weird")
    else:
        print("Not Weird")
print(check_weird(2))
print(check_weird(3))
#3.
#solution 1
def even_numbers_with_if(a, b):
    if a > b:
        a, b = b, a  
    start = a if a % 2 == 0 else a + 1
    return list(range(start, b + 1, 2))
print(even_numbers_with_if(3,10))
#solution2
def even_numbers_no_if(a, b):
    a, b = min(a, b), max(a, b)        
    start = a + (a % 2)                
    return list(range(start, b + 1, 2))
print(even_numbers_no_if(3,10))
