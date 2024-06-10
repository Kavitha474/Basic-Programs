While Loop
def reverse_of_num(param1):
    reverse_num = ""
    while param1 > 0:
        digit = str(param1 % 10)
        param1 = int(param1 / 10)
        reverse_num = reverse_num + digit 
    return reverse_num
number = int(input())       
result = reverse_of_num(number)
print(result)