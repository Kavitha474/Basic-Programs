def power_of_number(number, power):
    result = 1
    while(power > 0):
        result =  result * number
        power = power - 1
    return result

number = int(input())
power = int(input())
if(power > 0):
    result_power_of_number = power_of_number(number, power)
else:
    updated_result = power_of_number(number, -(power))
    result_power_of_number = 1/updated_result
print(result_power_of_number)