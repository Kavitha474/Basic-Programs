def one_to_n_Armstrong_num(start_num,end_num):
    for num in range(start_num,end_num + 1):
        actual_num = num
        length = len(str(actual_num))
        sum = 0
        while num > 0:
          digit = num % 10
          sum = sum + (digit ** length)
          num = int (num / 10)
        if(sum == actual_num):
            print(actual_num)
            
start_num = int(input())
end_num = int(input())
one_to_n_Armstrong_num(start_num,end_num)