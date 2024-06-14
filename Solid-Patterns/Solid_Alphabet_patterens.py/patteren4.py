"""
        A 
      A B A 
    A B C B A 
  A B C D C B A 
A B C D E D C B A 

"""


def alpha_pattern1(number):
    for row in range(1,number+1):
        result = ""
        for col in range(row):
            alpha = chr(65+col)
            result = result+alpha+" "
        spaces = "  "
        front_spaces = spaces *  (number - row)
        print(front_spaces+result,end ="")
        
        if(row >= 2):
            right_triangle_col =  row - 1
            right_triangle_result = ""
            while right_triangle_col >= 1:
                alpha = chr(65+(right_triangle_col - 1))
                right_triangle_result = right_triangle_result + alpha + " "
                right_triangle_col = right_triangle_col - 1
            print(right_triangle_result,end="")
        print()
            
                

number = int(input())
alpha_pattern1(number)