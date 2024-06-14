"""
* 
* * 
*   * 
*     * 
* * * * * 

"""

def hallow_right_angle_triangle(number):
    
    for row in range(1,number+1):
        if(row ==1 or row == number):
            print("* "*row)
        else:
            star = "* "
            space = "  "
            total_stars = row
            mid_space_count = total_stars - 2 
            mid_spaces = space * mid_space_count
            result = star + mid_spaces + star
            print(result)

number = int(input())
hallow_right_angle_triangle(number)