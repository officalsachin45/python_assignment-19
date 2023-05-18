def num():
    n=int(input("enter the number:"))
    if n in range(1,15):
        print("%s in a range"%str(n))
    else:
        print("the number outside given the range")
    
    
num()