'''
*                          * 
 *  *                    *  * 
 *  *  *              *  *  * 
 *  *  *  *        *  *  *  * 
 *  *  *  *  *  *  *  *  *  * 
 *  *  *  *  *  *  *  *  *  * 
 *  *  *  *        *  *  *  * 
 *  *  *              *  *  * 
 *  *                    *  * 
 *                          * 

'''

def butterfly_pattern(number):

    for row in range(1,number+1):
        spaces = "   "
        star = " * "
        left_traingle_back_spaces = spaces * (number - row)
        right_traingle_front_spaces = spaces * (number - row)
        no_of_stars = star * row
        result = no_of_stars + left_traingle_back_spaces + right_traingle_front_spaces + no_of_stars
        print(result)
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
butterfly_pattern(number)