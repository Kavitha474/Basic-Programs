def is_prime(num):
    count = 0
    for each_num in range(1,num+1):
        if(num % each_num == 0):
            count = count + 1
    if(count == 2):
        return True
    else:
        return False

def prime_factors(number):
    for num in range(1,number+1):
        if(number % num == 0):
            is_prime_number = is_prime(num)
            if(is_prime_number):
                print(num)
number = int(input())
prime_factors(number)