#For Loop

def factorial(number):
    factorial_of_num = 1
    for each_num in range(1,number+1):
        factorial_of_num = factorial_of_num * each_num
    return(factorial_of_num)
number = int(input())
result = factorial(number)
print(result)

# While Loop

def factorial(number):
    factorial_of_num = 1
    counter = number
    while counter > 0:
        factorial_of_num = counter * factorial_of_num
        counter = counter - 1
    return(factorial_of_num)
number = int(input())
result = factorial(number)
print(result)