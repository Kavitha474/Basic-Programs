While Loop
def sum_of_natural_nums(param1,param2):
    sum = 0
    counter =param1
    while param2 >= counter:
        sum = sum + counter
        counter = counter + 1
    return (sum)
start_num = int(input())
end_num = int(input())
result = sum_of_natural_nums(start_num,end_num)
print(result)

For Loop
def sum_of_natural_nums(param1,param2):
    sum = 0
    for each_num in range(param1,param2+1):
        sum = sum + each_num
    return (sum)
start_num = int(input())
end_num = int(input())
result = sum_of_natural_nums(start_num,end_num)
print(result)