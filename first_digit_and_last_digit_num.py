def first_and_last_digit_of_num(number):
    first_digit = number % 10
    print(first_digit)
    while number >= 10:
        number = int (number/10)
    last_digit = number % 10
    print(last_digit)
      
number = int(input())
first_and_last_digit_of_num(number)
