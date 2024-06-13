#Bottom Right traingle

#While loop 

'''
* * * * * 
  * * * * 
    * * * 
      * * 
        *
'''

def bottom_right_traingle(number):
  for row in range(number):
        spaces = "  "
        star = "* "
        no_of_spaces = spaces * row
        no_of_stars = star * number
        result = no_of_spaces + no_of_stars 
        print(result)
        number = number - 1
    
number = int(input())
bottom_right_traingle(number)

# #for loop 

def bottom_right_traingle(number):
  for row in range(number):
        spaces = "  "
        star = "* "
        no_of_spaces = spaces * row
        no_of_stars = star * number
        result = no_of_spaces + no_of_stars 
        print(result)
        number = number - 1
    
number = int(input())
bottom_right_traingle(number)