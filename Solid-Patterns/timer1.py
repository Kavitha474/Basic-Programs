'''

    *               * 
    * *           * * 
    * * *       * * * 
    * * * *   * * * * 
    * * * * * * * * * 
    * * * *   * * * * 
    * * *       * * * 
    * *           * * 
    *               * 

'''

def timer1(number):
    for row in range(number):
        space = "  "
        star = "* "
        left_traingle_back_spaces = space* (number - row)
        right_traingle_front_spaces = space * (number - (row+1))
        no_of_stars = star * (row + 1)
        result = no_of_stars + left_traingle_back_spaces + right_traingle_front_spaces + no_of_stars
        print(result)

    for row in range(1):
        star = "* "
        result = star * ((2*number)+1)
        print(result)
    
    for row in range(number):
        space = "  "
        star = "* "
        left_traingle_back_spaces = space * (row+1)
        right_traingle_front_spaces = space * (row)
        no_of_stars = star * (number - row)
        result = no_of_stars + left_traingle_back_spaces + right_traingle_front_spaces + no_of_stars
        print(result)

number = int(input())
timer1(number)