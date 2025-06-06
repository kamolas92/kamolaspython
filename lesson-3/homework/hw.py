1.
list_fruits = ['Mango','Pineapple','Grape','DragonFruit','Raspberry','Blueberyy']
print(list_fruits[2])
2.
list_of_numbers = [1,2,3,4,5,6,7]
list_of_numbers_2 = [8,9,10,11,12,13,14]
print(list_of_numbers)
print(list_of_numbers_2)
list_of_numbers.extend(list_of_numbers_2)
print(list_of_numbers)
3.
list_of_elements = ["23","56","76","52","27","98","67"]
print([list_of_elements[i] for i in (0,3,6)])
4.
favorite_movie_list = ["The Great Gatsby","Oshin","The Boys","The Gentlemen"]
movies_tuple = tuple(favorite_movie_list)
print(movies_tuple)
5.
Cities = ["New york","Washington","Sydney","Tokyo","Paris","Tashkent"]
if "Paris" in Cities:
    print("Paris is in the list")
else:
    print("Paris is not in the list")
6.
numbers = [9,8,7,6,5,4,3,2,1]
duplicated = numbers * 2
print(duplicated)
7.
sonlar = [1,2,3,4,5,6,7,8,9]
sonlar[0],sonlar[-1]=sonlar[-1],sonlar[0]
print(sonlar)
8.
numbers_tuple = tuple(range(1, 11))
slice_tuple = numbers_tuple[3:7]
print(slice_tuple)
9.
colors = ["red", "blue", "green", "blue", "yellow", "blue"]
blue_count = colors.count("blue")
print(f'"blue" appears {blue_count} times in the list.')
print(f'The first occurrence of "lion" is at index {lion_index}.')
10.
animals = ("elephant", "tiger", "lion", "giraffe", "lion")
lion_index = animals.index("lion")
print(f'The first occurrence of "lion" is at index {lion_index}.')

11.
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
merged_tuple = tuple1 + tuple2
print(merged_tuple)
12.
my_list = [10, 20, 30, 40, 50]
my_tuple = (1, 2, 3, 4, 5, 6)
list_length = len(my_list)
tuple_length = len(my_tuple)
print(f"Length of the list: {list_length}")
print(f"Length of the tuple: {tuple_length}")

13.
numbers_tuple = (10, 20, 30, 40, 50)
numbers_list = list(numbers_tuple)
print(numbers_list)

14.
numbers = (12, 45, 7, 34, 89, 2)
max_value = max(numbers)
min_value = min(numbers)
print(f"Maximum value: {max_value}")
print(f"Minimum value: {min_value}")
15.
words = ("apple", "banana", "cherry", "date", "elderberry")
reversed_words = words[::-1]
print(reversed_words)
