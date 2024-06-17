"""
Even number

*  *  *  *  *  *  
*        *     *  
*        *     *  
*  *  *  *  *  *  
*        *     *  
*  *  *  *  *  *  

"""

def printHallowSquare(number):
    star = "*  "
    space = "   "
    for row in range(1, number+1):
        for column in range(1, number+1):
            if((row == 1) or  (row == number) or (column ==1) or (column == number) or (column == int(number/2)+1) or (row == int(number/2)+1)):
                print(star, end="")
            else:
                print(space, end="")
        print()
number =int(input())
printHallowSquare(number)
