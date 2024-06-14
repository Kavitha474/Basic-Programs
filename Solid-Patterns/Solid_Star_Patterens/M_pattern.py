# M Pattern 

'''
 *  *  *  *  *  *  *  *  *  * 
 *  *  *  *        *  *  *  * 
 *  *  *              *  *  * 
 *  *                    *  * 
 *                          * 
'''

def M_pattern(number):
    for row in range (number):
        space = "   "
        star = " * "
        left_traingle_back_spaces = space * row
        right_traingle_back_spaces = space * row
        no_of_stars = star * number
        result = no_of_stars + left_traingle_back_spaces + right_traingle_back_spaces + no_of_stars
        print(result)
        number = number -1

number = int(input())
M_pattern(number)