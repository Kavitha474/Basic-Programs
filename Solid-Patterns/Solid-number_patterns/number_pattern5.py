'''
        1 
      1 2 
    1 2 3 
  1 2 3 4 
1 2 3 4 5 

'''

def number_pattern5(number):
    for row in range(1,number+1):
        result = ""
        for each_row in range(1,row+1):
            result = result+ str(each_row) + " "
        space = "  "
        front_spaces = space * (number - row)
        print(front_spaces + result)

number = int(input())
number_pattern5(number)