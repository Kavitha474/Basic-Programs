'''
1 
2 3 
4 5 6 
7 8 9 10 
11 12 13 14 15

'''

def number_pattren4(number):
    count = 1
    for row in range(1,number+1):
        result = ""
        for each_row in range(1,row+1):
            result = result + str(count)+" "
            count = count+1
        print(result)

number = int(input())
number_pattren4(number)