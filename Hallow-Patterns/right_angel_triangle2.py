"""
        * 
      * * 
    *   * 
  *     * 
* * * * * 

"""

def right_angle_triangle(num_of_rows):
    for each_row in range(1,num_of_rows+1):
        front_space = "  "
        front_spaces_count = num_of_rows - each_row
        front_spaces_in_row = front_space * front_spaces_count
        if ((each_row == 1) or (each_row == num_of_rows)):
            star = "* "
            count_of_stars = each_row
            stars_in_row  = star * count_of_stars
            result = front_spaces_in_row + stars_in_row
        else:
            star = "* "
            mid_spaces = "  "
            total_stars = each_row
            mid_spaces_count = total_stars - 2
            mid_spaces_in_row = mid_spaces * mid_spaces_count
            result = front_spaces_in_row  + star + mid_spaces_in_row + star
        print(result)
            
num_of_rows = int(input())
right_angle_triangle(num_of_rows)