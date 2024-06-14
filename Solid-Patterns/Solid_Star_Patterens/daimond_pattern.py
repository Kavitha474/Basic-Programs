# Daimond pattern

'''
         *  
       *   *  
     *   *   *  
   *   *   *   *  
 *   *   *   *   *  
   *   *   *   *  
     *   *   *  
       *   *  
         *  
'''
def daimond_pattern(number):

    for row in range (1,number+1):
        space = "  "
        star = " *  "
        front_spaces = space * (number - row)
        no_of_stars = star * row
        result = front_spaces + no_of_stars
        print(result)
    for row in range (1,number):
        space = "  "
        star = " *  "
        front_spaces = space * (row)
        no_of_stars = star * (number - 1)
        result = front_spaces + no_of_stars
        print(result)
        number = number - 1
    
number = int(input())
daimond_pattern(number)