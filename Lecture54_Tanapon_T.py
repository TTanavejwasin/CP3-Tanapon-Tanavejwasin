def login():
    usernameInput = input("Usename : ")
    usernamePassword = input("Password : ")
    if usernameInput == "Tanapon" and usernamePassword == "1234":
        return showMenu()
    else:
        return login()
def showMenu():
    print("-------iShop-------")
    print("1. Vat Calculator")
    print("2. Price Calculator")
    return menuSelect()
def menuSelect():
    userSelect = int(input("Enter Number : "))
    if userSelect == 1:
        return vatCalculator(totalprice=int(input("Total Price is : ")))
    elif userSelect == 2:
        return priceCalculator()
    else:
        return menuSelect()

def vatCalculator(totalprice):
    vat = int(input("Vat : "))
    result = totalprice + (totalprice * vat / 100)
    print(result)
    return menuSelect()

def priceCalculator():
    price1 = int(input("The First Product is : "))
    price2 = int(input("The Second Product is : "))
    return vatCalculator(price1 + price2)

login()









