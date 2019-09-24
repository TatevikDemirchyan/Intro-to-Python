import Productcheck

def buy(product, num, price):
    if Productcheck.check(product,num)==True:
        print("You bought",product,"​​and spent",num*price)
    else:
        print("Sorry! We are out of this product")

def main():
    buy("pen", 20, 150)

if __name__== "__main__":
    main()