While Loop
def given_range_odd_nums_in_while(param1,param2):
    counter = param1
    while (counter <= param2):
        if(counter % 2 != 0):
            print(counter)
        counter = counter + 1
start_num = int(input())
end_num = int(input())
given_range_odd_nums_in_while(start_num,end_num)

For Loop
def given_range_odd_nums_in_for(param1,param2):
    for each_num in range(param1,param2+1):
        if(each_num % 2 != 0):
            print(each_num)
start_num = int(input())
end_num = int(input())
given_range_odd_nums_in_for(start_num,end_num)