'''
        1 
      2 1 
    3 2 1 
  4 3 2 1 
5 4 3 2 1 


'''

def number_pattren7(number):
    for row in range(1,number+1):
        actual_row = row
        result = ""
        while row > 0:
            result = result + str(row)+" "
            row = row - 1
        space = "  "
        front_spaces = space * (number-actual_row)
        print(front_spaces+result)

number = int(input())
number_pattren7(number)