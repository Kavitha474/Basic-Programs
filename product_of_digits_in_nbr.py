While loop

def product_of_digits_of_num(number):
    product = 1
    while number > 0:
        digit = number%10
        number = int(number/10)
        product = product * digit
    return (product)
number = int(input())
result = product_of_digits_of_num(number)
print(result)