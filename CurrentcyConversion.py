python project
def main():
    print("Welcome to the Currency Conversion Program!")
    dollar = float(input("Enter an amount in U.S. Dollars: $ "))
    val1 = dollar * 0.83
    euro = format(val1, ".2f")
    val2 = dollar *111.14
    yen = format(val2, ".2f")
    val3 = dollar * 0.000076
    bitcion = format(val3, ".2f")
    print("$",dollar,"=",euro,"euro")
    print("$",dollar,"=",yen,"yen")
    print("$",dollar,"=",bitcion,"bitcion")
    
if __name__ == '__main__':
  main()
