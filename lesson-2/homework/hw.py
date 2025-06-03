1.
user_name = input("What is your name?:")
yearof_birth = int(input("what year were you born?:"))
current_year = datetime.now().year
age = current_year - yearof_birth
print ( f"Hello {user_name}. You are {age} years old. ")
2. 
txt = 'LMaasleitbtui'
print(txt[::2])
print(txt[1::2])
3.
txt = 'MsaatmiazD'
print(txt[::2])
print(txt[-1::-2])
4.
txt = "I'am John. I am from London"
print(txt[-6::])
5.
user_input = input('enter_string:')
reversed_string = user_input[::-1]
print('reversed_String:',reversed_string)
6.
string = 'Hushmuomala'
vowels = 'aeiou'
cnt = 0
for i in string:
    if i.lower() in vowels:
        cnt = cnt+1
cnt
7.
num = input("2 4 3 1 3 2 5 4 6: ")

numbers= list(map(int, num.split()))

if numbers:
    maksimum = max(numbers)
    print("Max_input:", maksimum)
else:
    print("empty.")
8.
word = input('Kiyik:')
reverse_word = word[::-1]
if reverse_word == word:
    print('yes,it is a palindrome!')
else:
    print('no,it is not a palindrome!')
  9.
e_mail = input('enter your email address:')
if '@' in e_mail:
    domain = e_mail.split('@')[1]
    print('the domain is:',domain)
else:
    print("invalid email address. please include an '@' symbol.")
  10.
import random
import string
password_length = int(input("enter the desired password length:"))
characters = string.ascii_letters+string.digits+string.punctuation
password = ''.join(random.choice(characters) for _ in range(password_length))
print("your random password is:",password)
