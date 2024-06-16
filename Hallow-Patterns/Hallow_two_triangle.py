"""
*                 * 
* *             * * 
*   *         *   * 
*     *     *     * 
* * * * * * * * * * 

"""
def Hallow_two_triangles(no_of_rows):
    for each_row in range(1,no_of_rows+1):
        star = "* "
        stars_in_row = star * each_row
        right_triangle_front_space = "  "
        right_triangle_front_space_count = no_of_rows - each_row
        right_triangle_front_spaces = right_triangle_front_space * right_triangle_front_space_count
        left_triangle_back_spaces = right_triangle_front_spaces
        if(each_row == 1 or each_row == no_of_rows):
            result = stars_in_row + left_triangle_back_spaces + right_triangle_front_spaces + stars_in_row
        else:
            mid_space = "  "
            mid_spaces_count = each_row - 2
            mid_spaces = mid_space * mid_spaces_count
            result = star + mid_spaces + star + left_triangle_back_spaces + right_triangle_front_spaces + star + mid_spaces + star
        print(result)

no_of_rows = int(input())
Hallow_two_triangles(no_of_rows)