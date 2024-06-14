"""
A 
A B 
A B C 
A B C D 
A B C D E 

"""


def alpha_pattern1(number):
    for row in range(1,number+1):
        for col in range(row):
            alpha = chr(65+col)
            print(alpha,end=" ")
        print()

number = int(input())
alpha_pattern1(number)