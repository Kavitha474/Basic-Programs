'''
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 

'''


def number_pattern1(number):
    for row in range(1,number+1):
        result = ""
        for each_row in range(1,row+1):
            result = result + str(each_row)+" "
        print(result)

number = int(input())
number_pattern1(number)