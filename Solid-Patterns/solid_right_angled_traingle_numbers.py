# Solid Right angled Traingle numbers
# While Loop

def solid_right_angled_traingle_numbers(no_of_rows):
    counter = 1
    while counter <= no_of_rows:
        output = (str(counter) * counter)
        print(output)
        counter = counter + 1
no_of_rows = int(input())
solid_right_angled_traingle_numbers(no_of_rows)

# For Loop

def solid_right_angled_traingle_numbers(no_of_rows):
    for each_row in range(1,no_of_rows+1):
        result = str(each_row) * each_row
        print(result)
no_of_rows = int(input())
solid_right_angled_traingle_numbers(no_of_rows)