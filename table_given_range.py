While loop

def table_using_while(param1,param2,param3):
    counter=param1
    while counter <= param3:
        print(str(param2)+ " x "+ str(counter) + " = " + str(param2*counter))
        counter = counter + 1
multiplication_start_with = int(input())
n = int(input())
multiply_up_to = int(input())
table_using_while(multiplication_start_with,n,multiply_up_to)

For loop

def table_using_for(param1,param2,param3):
    for each_num in range(param1,param3+1):
        print(str(param2)+ " x "+ str(each_num) + " = " + str(param2*each_num))
multiplication_start_with = int(input())
n = int(input())
multiply_up_to = int(input())
table_using_for(multiplication_start_with,n,multiply_up_to)
