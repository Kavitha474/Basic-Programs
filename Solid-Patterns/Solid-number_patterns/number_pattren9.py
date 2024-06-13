'''
      1 
    1 2 1 
  1 2 3 2 1 
1 2 3 4 3 2 1 

'''

def number_pattern9(number):
    for row in range(1,number+1):
        result = ""
        for col in range(1,row+1):
            result = result+str(col)+" "
        space = "  "
        front_spaces = space * (number - row)
        print(front_spaces + result,end ="")
        if(row >=2):
            right_traingle_col = row - 1
            right_traingle_result = ""
            while right_traingle_col >= 1:
                right_traingle_result = right_traingle_result + str(right_traingle_col) +" "
                right_traingle_col = right_traingle_col - 1
            print(right_traingle_result,end="")
        print()
            
number = int(input())
number_pattern9(number)