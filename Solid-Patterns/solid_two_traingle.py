#WHILE LOOP

def two_right_angle_traingle(number):
    count1 = 1
    while count1 <=2:
        count = 1
        while number >= count:
            result = str(count) * count
            print(result)
            count = count + 1
        count1 = count1 + 1
number = int(input())
two_right_angle_traingle(number)

# FOR LOOP 

def two_right_angle_traingle(number):
    for num in range (2):
        for each_num in range(1,number+1):
            result = str(each_num) * each_num
            print(result)
number = int(input())
two_right_angle_traingle(number)