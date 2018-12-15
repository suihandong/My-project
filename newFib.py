def newFib(first,second,term):
    termlist = [first,second]
    for i in range (term - 2):
        newNum = first + second
        termlist.append(newNum)
        first = second
        second = newNum
    return termlist

def main():
    fir = int(input("Enter the first term of the series: "))
    sec = int(input("Enter the second term of the series: "))
    term = int(input("Enter the number of terms you want to see: "))
    nfib = newFib(fir,sec,term)
    print("The first ",term," terms of the new series are: ")
    idx = 0
    for idx in range(term):
        print(nfib[idx]," ",end="")

if __name__ == '__main__':
  main()
