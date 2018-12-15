def summation(lw,up,f):
    num = 0
    i = lw
    while i <= up:
        if f == "square":
            num += i**2
        elif f == "cube":
                num += i**3
        elif f == "inverse":
            if lw == 0:
                num += (i+1)**(-1)
            else:
                num += i**(-1)
        i += 1
    return num


def main():
    lw = int(input("Enter a lower bound for summation: "))
    up = int(input("Enter a upper bound for summation: "))
    f = str(input("Enter a function to be summed(square, cube, inverse): "))
    f = str.lower(f)
    result = summation(lw,up,f)
    print("The result of the summation is",result)

if __name__ == '__main__':
  main()
