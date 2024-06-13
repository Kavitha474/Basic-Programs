'''
        1 
      2 2 
    3 3 3 
  4 4 4 4 
5 5 5 5 5 

'''

def number_pattern6(number):
    for row in range(1,number+1):
        space = "  "
        front_spaces = space * (number - row)
        result = (str(row)+" ") * row
        print(front_spaces + result)

number = int(input())
number_pattern6(number)