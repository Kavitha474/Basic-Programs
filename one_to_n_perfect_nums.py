def one_to_n_perfect_num(start_num,end_num):
    for num in range(start_num,end_num+1):
        sum = 0
        for each_num in range(1,num):
            if(num % each_num == 0):
                sum = sum + each_num
        if(sum == num):
            print(sum)
start_num = int(input())
end_num = int(input())
one_to_n_perfect_num(start_num,end_num)