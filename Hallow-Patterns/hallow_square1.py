"""
ODD number
* * * * * * * * * * * 
* *               * * 
*   *           *   * 
*     *       *     * 
*       *   *       * 
*         *         * 
*       *   *       * 
*     *       *     * 
*   *           *   * 
* *               * * 
* * * * * * * * * * * 

Even Number

* * * * * * * * * * 
* *             * * 
*   *         *   * 
*     *     *     * 
*       * *       * 
*       * *       * 
*     *     *     * 
*   *         *   * 
* *             * * 
* * * * * * * * * * 

"""

def hallow_butterfly(num_of_rows):
    def find_even_num_hallow_butturfly(num_of_rows): 
        top_triangle_rows = num_of_rows
        top_triangle_rows = int(num_of_rows/2)
        for each_row in range(1,top_triangle_rows+1):
            back_spaces = "  "
            left_tri_back_spaces_count = top_triangle_rows - each_row
            left_tri_back_spaces =  back_spaces * left_tri_back_spaces_count
            right_front_spcaes = left_tri_back_spaces
            star = "* "
            if(each_row == 1):
                stars_count = num_of_rows
                stars_in_row = star * stars_count
                result = stars_in_row
            else:
                hallow_mid_spaces = "  "
                total_stars = each_row
                hallow_mid_spaces_count = total_stars - 2
                mid_spaces = hallow_mid_spaces * hallow_mid_spaces_count
                result = star + mid_spaces + star + left_tri_back_spaces + right_front_spcaes + star + mid_spaces + star
            print(result)
                
        bottom_triangles_rows = int(num_of_rows/2)
        front_space_count = 0
        while bottom_triangles_rows > 0:
            star = "* "
            total_stars = num_of_rows
            mid_space = "  "
            total_stars = bottom_triangles_rows - 2
            mid_spaces = mid_space * total_stars
            back_spaces = "  "
            left_tri_back_spaces_count = front_space_count
            left_tri_back_spaces =  back_spaces * left_tri_back_spaces_count
            right_front_spcaes = left_tri_back_spaces
            if(bottom_triangles_rows == 1):
                result = star * num_of_rows
            else:
                result = star + mid_spaces + star + left_tri_back_spaces + right_front_spcaes + star + mid_spaces + star
            bottom_triangles_rows = bottom_triangles_rows - 1
            front_space_count = front_space_count + 1
            print (result)
            
    def find_odd_num_hallow_butturfly(num_of_rows):
        top_triangle_rows = num_of_rows
        top_triangle_rows = int(num_of_rows/2)+1
        for each_row in range(1,top_triangle_rows+1):
            back_spaces = "  "
            left_tri_back_spaces_count = top_triangle_rows - each_row
            left_tri_back_spaces =  back_spaces * left_tri_back_spaces_count
            right_front_spcaes = back_spaces * (left_tri_back_spaces_count-1)
            star = "* "
            if(each_row == 1):
                stars_count = num_of_rows
                stars_in_row = star * stars_count
                result = stars_in_row
            elif(each_row == top_triangle_rows):
                hallow_mid_spaces = "  "
                total_stars = each_row
                hallow_mid_spaces_count = total_stars - 2
                mid_spaces = hallow_mid_spaces * hallow_mid_spaces_count
                result = star + mid_spaces + star + left_tri_back_spaces + right_front_spcaes + mid_spaces + star
            else:
                hallow_mid_spaces = "  "
                total_stars = each_row
                hallow_mid_spaces_count = total_stars - 2
                mid_spaces = hallow_mid_spaces * hallow_mid_spaces_count
                result = star + mid_spaces + star + left_tri_back_spaces + right_front_spcaes + star + mid_spaces + star
            print(result)
        
        bottom_triangles_rows = int(num_of_rows/2)
        front_space_count = 0
        while bottom_triangles_rows > 0:
            star = "* "
            total_stars = num_of_rows
            mid_space = "  "
            total_stars = bottom_triangles_rows - 2
            mid_spaces = mid_space * total_stars
            back_spaces = "  "
            left_tri_back_spaces_count = front_space_count
            left_tri_back_spaces =  back_spaces * left_tri_back_spaces_count
            right_front_spcaes = back_spaces * (left_tri_back_spaces_count+1)
            if(bottom_triangles_rows == 1):
                result = star * num_of_rows
            else:
                result = star + mid_spaces + star + left_tri_back_spaces + right_front_spcaes + star + mid_spaces + star
            bottom_triangles_rows = bottom_triangles_rows - 1
            front_space_count = front_space_count + 1
            print (result)

    if(num_of_rows % 2 == 0):
        find_even_num_hallow_butturfly(num_of_rows)
    else:
        find_odd_num_hallow_butturfly(num_of_rows)


num_of_rows = int(input())
hallow_butterfly(num_of_rows)