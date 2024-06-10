# While loop

def sum_of_digits_of_num(number):
    sum = 0 
    while number > 0:
        digit = number%10
        number = int(number/10)
        sum = sum + digit
    return (sum)
number = int(input())
result = sum_of_digits_of_num(number)
print(result)

For Loop

def sum_of_digits_of_num(number):
    sum = 0 
    length = len(str(number))
    for each_num in range(length):
        digit = number % 10
        number = int(number/10)
        sum = sum + digit
    return (sum)
number = int(input())
result = sum_of_digits_of_num(number)
print(result)