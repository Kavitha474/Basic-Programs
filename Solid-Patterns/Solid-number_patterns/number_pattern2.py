'''
1 
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5 


'''

def number_pattren2(number):
    for row in range(1,number+1):
        result = (str(row)+" ") * row
        print(result)

number = int(input())
number_pattren2(number)