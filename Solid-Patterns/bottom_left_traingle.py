#Nested Loop 
#bottom Left traingle

'''
* * * * * 
* * * * 
* * * 
* * 
* 
'''

number = int(input())

for row in range(number):
    result = ""
    counter = number
    while counter > 0:
        result = result + "* "
        counter = counter - 1
    print(result)
    number = number -1
    
#while Loop

def bottom_left_traingle(number):
    counter = number
    while counter > 0:
        result = "* "*counter
        counter = counter - 1
        print(result)
    
number = int(input())
bottom_left_traingle(number)

#For Loop
def bottom_left_traingle(number):
    for row in range (number):
        result = "* "*number
        number = number - 1
        print(result)
    
number = int(input())
bottom_left_traingle(number)
