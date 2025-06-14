#1. 
def is_prime(n):
    if n <= 1:
        return False  
    for i in range(2, int(n ** 0.5) + 1):  
        if n % i == 0:
            return False  
    return True  
print(is_prime(4))
print(is_prime(7))
#2.
def digit_sum(k):
    total = 0
    while k > 0:
        total += k % 10    
        k //= 10           
    return total
print(digit_sum(24))
print(digit_sum(502))
#3.
def print_powers_of_two(N):
    power = 2
    while power <= N:
        print(power, end=" ")
        power *= 2
print(print_powers_of_two(10))
