# Solid Rectangle pattern M rows and N columns

# While Loop

'''
* * * * * * * 
* * * * * * * 
* * * * * * * 
'''

def solid_rectangle(no_of_rows,no_of_cols):
    counter = 1
    while counter <= no_of_rows:
        output = ("*" * no_of_cols)
        print(output)
        counter = counter + 1
 
no_of_rows = int(input())
no_of_cols = int(input())   
solid_rectangle(no_of_rows,no_of_cols)

# For Loop

def solid_rectangle(no_of_rows,no_of_cols):
    for each_row in range(no_of_rows,no_of_cols+1):
        result = "*"*no_of_cols
        print(result)
no_of_rows = int(input())
no_of_cols = int(input())
solid_rectangle (no_of_rows,no_of_cols)