#1.
txt = 'abcabcdabcdeabcdefabcdefg'
vowels = 'uiaeoAOIUE'
cnt = 2
while cnt < len(txt):
    if txt[cnt] not in vowels:
        txt = txt[:cnt+1] + '_' + txt[cnt +1:]
        vowels += txt[cnt]
        cnt = cnt + 4
        continue
    cnt = cnt + 1
txt
# 2.
n = int(input())
i=0
while i < n:
    print(i**2)
    i = i + 1

#3.
  ##1.
i = 1
while i <= 10:
    print(i)
    i += 1
  ##2
for i in range(1,7):       
    for j in range(1, i + 1):
        print(j,end=' ')
    print()
  ##3.range
number_given = int(input("enter the number given:"))
total = 0
for number in range(1,number_given+1):
    total = total + number
total
  ##4.
given_n = int(input("enter number:"))
for i in range(1,11):
    print(given_n*i)
  ##5.
numbers = [12, 75, 150, 180, 145, 525, 50]

for number in numbers:
    if number > 500:
        break
    if number > 150:
        continue
    if number % 5 == 0:
        print(number)

  ##6.
num = int(input("Enter a number: "))
count = 0

while num != 0:
    num = num // 10 
    count += 1

print("Total digits:", count)

  ##7.
n = 5

for i in range(n, 0, -1):       
    for j in range(i, 0, -1):      
        print(j, end=" ")
    print()  

  ##8.
numbers = [10, 20, 30, 40, 50]
for i in range(len(numbers) - 1, -1, -1):
    print(numbers[i])

  ##9.
for i in range(-10, 0):
    print(i)

    ##10.
for i in range(5):
    print(i)
else:
    print("Done!")

  ##11.
start = 25
end = 50

print("Prime numbers between", start, "and", end, "are:")

for num in range(start, end + 1):
    if num > 1:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                break
        else:
            print(num)

  ##12.
a, b = 0, 1
n = 10

print("Fibonacci series up to", n, "terms:")

for i in range(n):
    print(a)
    a, b = b, a + b

  ##13.
def factorial(number):
    if number in [0,1]:
        return 1
    else:
        return number * factorial(number - 1)

factorial(5)

#4.
list1 = [1, 1, 2]
list2 = [2, 3, 4]

uncommon = [x for x in list1 if x not in list2] + [x for x in list2 if x not in list1]
print(uncommon)

list1 = [1, 2, 3]
list2 = [4, 5, 6]

# Use set symmetric difference
uncommon = list(set(list1).symmetric_difference(set(list2)))
print(uncommon)

list1 = [1, 1, 2, 3, 4, 2]
list2 = [1, 3, 4, 5]

uncommon = [x for x in list1 if x not in list2] + [x for x in list2 if x not in list1]
print(uncommon)
