# Solid Right angled Traingle
# While Loop
'''
* 
* * 
* * * 
* * * * 
* * * * * 

'''

def solid_right_angled_traingle(no_of_rows):
    counter = 1
    while counter <= no_of_rows:
        output = ("* " * counter)
        print(output)
        counter = counter + 1
no_of_rows = int(input())
solid_right_angled_traingle(no_of_rows)

# For Loop

def solid_right_angled_traingle(no_of_rows):
    for each_row in range(1,no_of_rows+1):
        result = "* " * each_row
        print(result)
no_of_rows = int(input())
solid_right_angled_traingle(no_of_rows)