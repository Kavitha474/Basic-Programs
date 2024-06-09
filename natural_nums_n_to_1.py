For Loop
def n_to_one_natural_num_using_for(param1):
    for each_num in range(1,param1+1):
        result = param1
        print(result)
        param1 = param1 - 1
number = int(input())
n_to_one_natural_num_using_for(number)

While Loop 
def n_to_one_natural_num_using_while(param1):
    counter = 1
    while counter <= param1:
        print(param1)
        param1 = param1 - 1
number = int(input())
n_to_one_natural_num_using_while(number)