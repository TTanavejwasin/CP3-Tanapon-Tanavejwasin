UserName = input("Username : ")
PassWord = input("Password : ")
if UserName == "Tanapon" and PassWord == "Tanavejwasin":
    print("Welcome To Apple")
    print("Please Select The Type of Apple Product")
    print("1.Iphone")
    print("2.Ipad")
    print("3.Mac")
    Iphone = 20000
    Ipad = 18000
    Mac = 40000
    UserSelect = int(input(":"))
    if UserSelect == 1:
        print("Price is :",Iphone)
    elif UserSelect == 2:
        print("Price is :",Ipad)
    elif UserSelect == 3:
        print("Price is : ",Mac)
    else:
        print("Please Select The Type of Apple Product")
else:
    print("Username or Password is wrong")
