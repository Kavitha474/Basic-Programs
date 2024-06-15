"""
_ _ _ _ _ _ 
|         / 
|       / 
|     / 
|   / 
| /

"""

def hallow_pattern(number):
    print("_ " * (number+1))
    
    for each_row in range(1,number+1):
        spaces= "  "
        pipe = "| "
        farword_slash = "/ "
        mid_spaces = spaces * (number - each_row)
        row = pipe + mid_spaces + farword_slash
        print(row)

number = int(input())
hallow_pattern(number)