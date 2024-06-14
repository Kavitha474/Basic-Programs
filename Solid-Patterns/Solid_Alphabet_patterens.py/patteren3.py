"""
A 
B C 
D E F 
G H I J 
K L M N O 

"""


def alpha_pattern1(number):
    count = 0
    for row in range(1,number+1):
        for col in range(row):
            alpha = chr(65+count)
            print(alpha,end=" ")
            count = count + 1
        print()
            

number = int(input())
alpha_pattern1(number)