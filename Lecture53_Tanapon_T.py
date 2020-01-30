Number = int(input("Number : "))
def vatCalculate(totalprice):
    result = totalprice+(totalprice*7/100)
    return result
print(vatCalculate(Number))