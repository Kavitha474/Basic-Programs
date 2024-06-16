"""
* * * * * 
*     * 
*   * 
* * 
* 

"""



def right_angle_triangle(num_of_rows):
    no_of_stars = 0
    for each_row in range(1,num_of_rows+1):
        if(each_row == 1 or each_row == num_of_rows):
            star = "* "
            count_of_stars = num_of_rows-no_of_stars
            result = star * count_of_stars
        else:
            space = "  "
            star = "* "
            total_stars = num_of_rows-no_of_stars
            mid_spaces_count = total_stars - 2
            mid_spaces = space * mid_spaces_count
            result = star + mid_spaces + star
        no_of_stars = no_of_stars + 1
        print(result)
            
num_of_rows = int(input())
right_angle_triangle(num_of_rows)