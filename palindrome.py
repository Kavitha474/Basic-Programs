# For Loop

number = input()
length_of_num = len(number)
isPalindrome = True
for index in range(length_of_num):
    if(number[index] != number[length_of_num-1-index]):
        isPalindrome = False
if isPalindrome:
    print("Palindrome")
else:
    print("Not a palindrome")