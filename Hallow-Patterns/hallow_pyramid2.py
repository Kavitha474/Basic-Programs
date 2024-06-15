"""
1 
2 2
3   3
4     4
5       5
4     4
3   3
2 2
1

"""

def hallow_pyramid2(num_of_rows):
    for row in range(1,num_of_rows+1):
        if(row == 1):
            each_row = str(row)+" "
        else:
            space = "  "
            mid_space_count = row - 2 
            mid_spaces = space * mid_space_count
            each_row = str(row)+" " + mid_spaces + str(row)
        print(each_row)
        
    bottom_triangle_rows = num_of_rows - 1
    while bottom_triangle_rows > 1:
        space = "  "
        mid_space_count = bottom_triangle_rows - 2 
        mid_spaces = space * mid_space_count
        each_row = str(bottom_triangle_rows)+" " + mid_spaces + str(bottom_triangle_rows)
        bottom_triangle_rows = bottom_triangle_rows - 1
        if(num_of_rows == bottom_triangle_rows):
            each_row = str(bottom_triangle_rows)
        print(each_row)
    print(1)
                

num_of_rows = int(input())
hallow_pyramid2(num_of_rows)