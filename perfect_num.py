# While loop

number = int(input())
def perfect_number(number):
    sum = 0
    counter = 1
    while number > counter:
        if(number % counter == 0):
            sum = sum + counter
        counter = counter + 1
    if(sum == number):
        return("Perfect number")
    else:
        return("Not a Perfect number")
result = perfect_number(number)
print(result)

# For loop

number = int(input())
def perfect_number(number):
    sum = 0
    for each_num in range(1,number):
        if(number % each_num == 0):
            sum = sum + each_num
    if(sum == number):
        return("Perfect number")
    else:
        return("Not a Perfect number")
result = perfect_number(number)
print(result)