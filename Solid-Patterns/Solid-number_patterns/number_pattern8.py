'''
      10 
    9 8 
  7 6 5 
4 3 2 1

'''
def number_pattren8(number):
    count = (2*(number)+2)
    for row in range(1,number+1):
        result = ""
        for each_row in range(1,row+1):
            result = result + str(count)+" "
            count = count-1
        space = "  "
        front_spaces = space * (number-row)
        print(front_spaces+result)

number = int(input())
number_pattren8(number)