# while loop

number = int(input())
actual_num = number
def strong_num(number):
    sum = 0
    while number > 0:
        digit = number % 10
        fact_number = 1
        while digit > 0:
            fact_number = fact_number * digit
            digit = digit - 1
        sum = sum + fact_number
        number=int(number/10)
    if(sum == actual_num):
        return ("strong Number")
    else:
        return("Not a strong number")
result=strong_num(number)
print(result)