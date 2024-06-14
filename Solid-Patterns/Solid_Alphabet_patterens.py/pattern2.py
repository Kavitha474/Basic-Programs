"""
A
BB
CCC
DDDD
EEEEE

"""


def alpha_pattern1(number):
    for row in range(1,number+1):
        alpha = chr(65+(row-1))
        result = str(alpha*row)
        print(result,end="")
        print()

number = int(input())
alpha_pattern1(number)