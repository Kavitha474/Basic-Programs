"""
     1 
    1 1 
   1 2 1 
  1 3 3 1 
 1 4 6 4 1 
1 5 10 10 5 1 

"""


def find_factorial(num):
    if(num == 0 or num == 1):
        return 1
    else:
        factorial_value = 1
        while num > 0:
            factorial_value = factorial_value * num 
            num = num - 1
        return factorial_value

def find_n_c_r_value(n,r):
    n_factorial = find_factorial(n)
    r_factorial = find_factorial(r)
    n_minus_r = n - r 
    n_minus_r_factorial = find_factorial(n_minus_r)
    denominator_value = r_factorial * n_minus_r_factorial
    result = int(n_factorial / denominator_value)
    return result


def pascal_triangle(number_of_rows):
    
    for row in range(number_of_rows):
        result = ""
        for col in range(row+1):
            n_c_r_value = find_n_c_r_value(row,col)
            result = result + str(n_c_r_value) + " "
        space = " "
        front_spaces = space * (number_of_rows - (row+1))
        print(front_spaces+result,end="")
        print()

number_of_rows = int(input())
pascal_triangle(number_of_rows)