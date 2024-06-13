#Timer pattern 
'''

 *   *   *   *   *  
   *   *   *   *  
     *   *   *  
       *   *  
         *  
       *   *  
     *   *   *  
   *   *   *   *  
 *   *   *   *   *

'''

def timer_pattern(number):
    for row in range(number):
        space = "  "
        star = " *  "
        front_spaces = space * row
        no_of_stars = star * (number-row)
        result = front_spaces + no_of_stars
        print(result)
    for row in range(2,number+1):
        space = "  "
        star = " *  "
        front_spaces = space * (number-row)
        no_of_stars = star * row
        result = front_spaces + no_of_stars
        print(result)

number = int(input())
timer_pattern(number)