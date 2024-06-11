# While Loop

number = int(input())
length = len(str(number))
actual_num = number
def armstrong_num(number):
    sum = 0
    while number > 0:
        digit = number % 10
        number = int(number/10)
        sum = sum + digit ** length
    if(sum == actual_num):
        return("Armstrong number")
    else:
        return("Not an Armstrong number")
result = armstrong_num(number)
print(result)