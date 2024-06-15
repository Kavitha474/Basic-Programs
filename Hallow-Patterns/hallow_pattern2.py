"""
# # # # # 
+     + 
+   + 
+ + 
+ 

"""

def hallow_pattern(number):
    
    for each_row in range(1,number+1):
        hash = "# " * number
        spaces= "  "
        plus = "+ "
        if(each_row == 1):
            row = hash
        elif(each_row == number):
            row = plus
        else:
            mid_spaces = spaces * (number - (each_row+1))
            row = plus + mid_spaces + plus
        print(row)

number = int(input())
hallow_pattern(number)