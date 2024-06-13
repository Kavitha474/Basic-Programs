#Upper W pattern

number = int(input())

for row in range(1,number+1):
    spaces = "   "
    star = " * "
    left_traingle_back_spaces = spaces * (number - row)
    right_traingle_front_spaces = spaces * (number - row)
    no_of_stars = star * row
    result = no_of_stars + left_traingle_back_spaces + right_traingle_front_spaces + no_of_stars
    print(result)