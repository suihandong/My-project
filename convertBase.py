def conbase(dec,b):
    rem = ""
    if dec // b == 0:
        reminder = dec%b
        if reminder > 9:
            rem = chr(reminder+55)
        else:
            rem = str(reminder)
        return rem
    else:
        reminder = dec%b
        dec = dec//b
        if reminder > 9:
            rem = chr(reminder+55)
        else:
            rem = str(reminder)
        rem = conbase(dec,b) + rem
        return rem
def main():
    dec = int(input("Enter your decimal number: "))
    b = int(input("Enter the base you want to convert to: "))
    res = conbase(dec,b)

    print(dec,"in base",b,"is",res)
if __name__ == '__main__':
  main()
