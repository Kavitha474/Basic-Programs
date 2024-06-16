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
        front_space = "  "
        front_space_count = each_row - 1
        front_spaces_in_row = front_space * front_space_count
        if(each_row == 1 or each_row == num_of_rows):
            star = "* "
            count_of_stars = num_of_rows - no_of_stars
            stars_in_row = star * count_of_stars
            result = front_spaces_in_row + stars_in_row
        else:
            star = "* "
            mid_spaces = "  "
            total_stars = num_of_rows - no_of_stars
            mid_spaces_count = total_stars - 2 
            mid_spaces_in_row = mid_spaces * mid_spaces_count
            result = front_spaces_in_row + star + mid_spaces_in_row + star
            
        no_of_stars = no_of_stars + 1    
        print(result)
            
            
num_of_rows = int(input())
right_angle_triangle(num_of_rows)