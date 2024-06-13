'''
1 
2 1 
3 2 1 
4 3 2 1 
5 4 3 2 1 

'''

def number_pattren3(number):
    for row in range(1,number+1):
        result = ""
        while row > 0:
            result = result + str(row)+" "
            row = row - 1
        print(result)

number = int(input())
number_pattren3(number)