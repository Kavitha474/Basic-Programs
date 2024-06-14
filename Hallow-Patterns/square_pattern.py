"""
* * * * * 
*       * 
*       * 
*       * 
* * * * * 

"""

def hallow_pattern(number):
    for row in range(1,number+1):
        if(row == 1 or row == number):
            print("* "* number,end="")
        else:
            total_stars = number
            star = "* "
            space = "  "
            mid_spaces_count = total_stars - 2
            mid_spaces = space * mid_spaces_count
            result = star + mid_spaces + star
            print(result,end="")
        print()

number = int(input())
hallow_pattern(number)