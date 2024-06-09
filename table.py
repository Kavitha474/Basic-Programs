While loop
def table_using_while(param1,param2):
    counter=1
    while counter <= param2:
        print(str(param1)+ " x "+ str(counter) + " = " + str(param1*counter))
        counter = counter + 1
n = int(input())
multiply_up_to = int(input())
table_using_while(n,multiply_up_to)

For loop
def table_using_for(param1,param2):
    for each_num in range(1,param2+1):
        print(str(param1)+ " x "+ str(each_num) + " = " + str(n*each_num))
n = int(input())
multiply_up_to = int(input())
table_using_for(n,multiply_up_to)