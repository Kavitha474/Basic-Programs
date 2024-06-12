# Square pattern (without using "* " * n)

n = int(input())

for row in range(n):
    result = ""
    for col in range(n):
        result = result + "* "
    print(result)

#while loop

def square_pattern(number):
    counter = 1
    while counter <= number:
        print("* "*number)
        counter = counter + 1

number = int(input())
square_pattern(number)

#For loop

def square_pattern(number):
    for num in range(1,number+1):
        print("* "*number)

number = int(input())
square_pattern(number)