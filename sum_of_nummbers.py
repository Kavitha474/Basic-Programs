def sum_of_digits_range(start_num,end_num):
    sum = 0
    for num in range(start_num,end_num+1):
        while num>0:
            digit = num % 10
            sum = sum + digit
            num = int(num / 10)
    print(sum)
start_num = int(input())
end_num = int(input())
sum_of_digits_range(start_num,end_num)