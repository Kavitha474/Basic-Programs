For Loop

number = int(input())
for factor in range(1,number+1):
    if(number % factor == 0):
        print(factor)

While Loop

number = int(input())
factor = 1
while number >= factor:
    if(number % factor == 0):
        print(factor)
    factor = factor + 1