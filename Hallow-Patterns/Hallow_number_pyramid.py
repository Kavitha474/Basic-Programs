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

def inverted_halow_pyramid(num_of_rows):
    for row in range(1,num_of_rows+1):
        front_space = "  "
        front_spaces_count = num_of_rows - row
        front_spaces_in_row = front_space * front_spaces_count
        if(row == 1):
            each_row = front_spaces_in_row + str(row)+" "
        else:
            space = "  "
            mid_space_count = row - 2 
            mid_spaces = space * mid_space_count
            each_row = front_spaces_in_row+str(row)+" " + mid_spaces + str(row)
        print(each_row)
    
    space_count = num_of_rows - 1
    for row in range(2,num_of_rows+1):
        front_space = "  "
        front_spaces_count = row -1
        front_spaces_in_row = front_space * front_spaces_count
        if(row == num_of_rows):
            each_row = front_spaces_in_row + str(1)+" "
        else:
            space = "  "
            total_nums = space_count 
            mid_space_count = total_nums  - 2
            mid_spaces = space * mid_space_count
            each_row = front_spaces_in_row+str(space_count)+" " + mid_spaces + str(space_count)
        print(each_row)
        space_count = space_count - 1
    
num_of_rows = int(input())
inverted_halow_pyramid(num_of_rows)