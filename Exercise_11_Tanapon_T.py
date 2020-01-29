number = int(input("Enter a number : "))
for a in range(number):
    space = " " * (number - (a+1))
    star = "*" * ((a*2)+1)
    print(space, star)