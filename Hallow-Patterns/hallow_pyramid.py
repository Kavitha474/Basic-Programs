"""
    * 
   * * 
  *   * 
 *     * 
* * * * * 

"""

def hallow_pyramid(num_of_rows):
    for row in range (1,num_of_rows+1):
        space = " "
        count_of_front_spaces = (num_of_rows - row)
        front_spaces = space * count_of_front_spaces
        star = "* "
        count_of_stars = row 
        stars_in_each_row = star * count_of_stars
        if(row == 1 or row == num_of_rows):
            each_row = front_spaces + stars_in_each_row
        else:
            space = "  "
            total_stars = row 
            mid_spaces_count = total_stars - 2
            mid_spaces = space * mid_spaces_count
            each_row = front_spaces + star + mid_spaces + star
        
        print(each_row)

num_of_rows = int(input())
hallow_pyramid(num_of_rows)