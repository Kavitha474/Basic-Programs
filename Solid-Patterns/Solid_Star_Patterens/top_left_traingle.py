#Traingle1
# Nested Loops


'''
* 
* * 
* * * 
* * * * 
* * * * *

'''

number = int(input())

for row in range (1,number+1):
    result = ""
    for each_row in range (1,row+1):
        result = result + "* "
    print(result)

#While Loop 

def top_left_traingle(number):
    counter = 1 
    while counter <= number:
        result = "* "*counter
        print(result)
        counter = counter + 1 

number = int(input())
top_left_traingle(number)

#For Loop

def top_left_traingle(number):
    for row in range(1,number+1):
        result = "* "* row
        print(result)

number = int(input())
top_left_traingle(number)