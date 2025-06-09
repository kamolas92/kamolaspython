#1
my_dict = {'apple': 10, 'banana': 2, 'cherry': 5, 'date': 7}
sorted_asc = dict(sorted(my_dict.items(), key=lambda item: item[1]))
print("Ascending:", sorted_asc)
sorted_desc = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))
print("Descending:", sorted_desc)
#2
numbers={0: 10, 1: 20}
numbers[2]=30
print(numbers)
#3
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

new_dict=dic1
new_dict.update(dic2)
new_dict.update(dic3)
print(new_dict)
#4
n=5
squares={x: x*x for x in range(1,n+1)}
print(squares)
#5
n=15
squares={x: x*x for x in range(1, n+1)}
print(squares)
#Set exercises
#1
sets={1,2,3,'Sitora','a'}
print(sets)
#2
my_set = {1, 2, 3, 'Sitora', 'a'}

for item in my_set:
    print(item)
  #3
my_set = {1, 2, 3, 'Sitora', 'a'}
my_set.add(4)
print(my_set)
#4
my_set = {1, 2, 3, 'Sitora', 'a'}
my_set.remove('a')
print(my_set)
#5
my_set = {1, 2, 3, 'Sitora', 'a'}
remove_item=('a')
if remove_item in my_set:                          
   my_set.remove(remove_item)
print(my_set)
