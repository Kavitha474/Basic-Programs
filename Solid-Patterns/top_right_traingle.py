# #Nested Loop 

number = int(input())

for row in range(1):
    counter = 1
    while number >= counter:
        spaces = "  " 
        front_spaces = spaces * (number - counter)
        star = "* "
        no_of_stars = star * counter
        result =front_spaces + no_of_stars
        print(result)
        counter = counter + 1
    

    
# #while Loop

def top_right_traingle(number):
    counter = 1
    while number >= counter:
        spaces = "  " 
        front_spaces = spaces * (number - counter)
        star = "* "
        no_of_stars = star * counter
        result = front_spaces + no_of_stars
        print(result)
        counter = counter + 1
        
number = int(input())
top_right_traingle(number)

#For Loop

def top_right_traingle(number):
    for row in range (1,number+1):
        spaces = "  " 
        front_spaces = spaces * (number - row)
        star = "* "
        no_of_stars = star * row
        result = front_spaces + no_of_stars
        print(result)
    
number = int(input())
top_right_traingle(number)