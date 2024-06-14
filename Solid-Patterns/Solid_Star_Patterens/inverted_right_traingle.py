#Inverted Traingle 
#without using "*" * n

'''
* * * * * 
* * * * 
* * * 
* * 
* 
'''

number = int(input())
for row in range (number):
    result = ""
    for col in range (number):
        result = result + "* "
    print(result)
    number = number - 1

# while Loop 

def Inverted_right_traingle(number):
    counter = number
    while counter > 0:
        print("* " * counter)
        counter = counter-1
number = int(input())
Inverted_right_traingle(number)

#for Loop

def Inverted_right_traingle(number):
    count = number
    for row in range(number):
        result = "* " * count
        count = count - 1
        print(result)

number = int(input())
Inverted_right_traingle(number)