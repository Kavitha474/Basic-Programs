# For Loop

def prime_num(number):
    count =0 
    for each_num in range(1,number+1):
        if(number % each_num == 0):
            count = count + 1
    if(count == 2):
        return("Prime number")
    else:
        return("Not a Prime number")
number = int(input())
result = prime_num(number)
print(result)

# while Loop

def prime_num(number):
    count =0 
    counter = 1
    while number >= counter:
        if(number % counter == 0):
            count = count + 1
        counter = counter + 1
    if(count == 2):
        return("Prime number")
    else:
        return("Not a Prime number")
number = int(input())
result = prime_num(number)
print(result)