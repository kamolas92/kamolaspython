#1.Given a side of square. Find its perimeter and area.

side=int(input('enter the length of the side of the square:4'))
perimeter=4*side
area=side*side
print('kvadratning perimetri:',perimeter)
print('kvadratning yuzasi:',area)


#2.Given diameter of circle. Find its length.
diameter=int(input('enter the diameter of the circle:3'))
import math
circumference=3*math.pi
print('length:',circumference)

#3.Given two numbers a and b. Find their mean.
a=234
b=567
total=a+b
print('sum:',total)
mean=total/2
print('mean:',mean)

#4.Given two numbers a and b. Find their sum, product and square of each number.
a=9087
b=6732
sum=a+b
print('sum:',sum)
product=a*b
print('product:',product)
square_a=a**2
print('squareA:',square_a)
square_b=b**2
print('squareB:',square_b)
