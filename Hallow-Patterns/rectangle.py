"""
* * * * * * 
*         * 
*         * 
* * * * * * 

"""


def hallow_rectangle(row,col):
    for each_row in range(1,row+1):
        if(each_row == 1 or each_row == row ):
            result = "* "*col
            print(result)
        else:
            star = "* "
            space = "  "
            total_spaces = col 
            count_mid_spaces = total_spaces - 2
            mid_spaces = space * count_mid_spaces
            result = star + mid_spaces + star
            print(result)

number_of_rows = int(input())
number_of_cols = int(input())
hallow_rectangle(number_of_rows,number_of_cols)