def one_to_n_prime_sum(start_num,end_num):
    sum = 0
    for num in range(start_num,end_num+1):
        count = 0
        for each_num in range(1,num+1):
            if(num % each_num == 0):
                count = count + 1
        if(count == 2):
            print(num)
            sum = sum + num
    print(sum)

start_num = int(input())
end_num = int(input())
one_to_n_prime_sum(start_num,end_num)