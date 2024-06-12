# Square of N rows M cols
# While Loop

def square_pattern(no_of_rows):
    counter = 1
    while counter <= no_of_rows:
        result = (str(counter) * no_of_rows)
        print(result)
        counter = counter + 1
no_of_rows = int(input())
square_pattern(no_of_rows)

# For Loop

def square_pattern(no_of_rows):
    for each_row in range(1,no_of_rows+1):
        result = str(each_row) * no_of_rows
        print(result)
no_of_rows=int(input())
square_pattern(no_of_rows)