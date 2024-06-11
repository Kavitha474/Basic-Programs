def one_to_n_strong_numbers(start_num,end_num):
    for num in range(start_num,end_num+1):
        actual_num=num
        total_sum = 0
        while num > 0:
            digit = num % 10
            fact = 1
            while digit>0:
                fact = fact * digit
                digit = digit - 1
            total_sum = total_sum + fact
            num = int(num/10)
        if(total_sum == actual_num):
            print(total_sum)

start_num = int(input())
end_num = int(input())
one_to_n_strong_numbers(start_num,end_num)