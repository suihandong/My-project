import sums1

def main():
    target = input("Input target: ")
    while target.isnumeric() is False:
        target = input("Target must be an integer. Enter a valid target: ")

    alt = input("Input list of numbers separated by a space: ")
    alist = alt.split(" ")
    i = 0
    while i < len(alist):
        while alist[i].isnumeric() is False:
            alt = input("The list can only contain integers. Enter a valid list: ")
            alist = alt.split(" ")
            i += 1

    intlist = [0]*len(alist)
    for i in range(0,len(alist)):
        intlist[i]=int(alist[i])

    getsum = dongx460_4A.two_sums(intlist,int(target))
    print("The two numbers that sum up to",target,"are",getsum[0],"and",getsum[2])

    togo = input("Would you like to enter another list?(y/n): ")
    while togo == "y" or togo == "Y":
        target = input("Input target: ")
        while target.isnumeric() is False:
            target = input("Target must be an integer. Enter a valid target: ")

        alt = input("Input list of numbers separated by a space: ")
        alist = alt.split(" ")
        i = 0
        while i < len(alist):
            while alist[i].isnumeric() is False:
                alt = input("The list can only contain integers. Enter a valid list: ")
                alist = alt.split(" ")
                i += 1

        intlist = [0]*len(alist)
        for i in range(0,len(alist)):
            intlist[i]=int(alist[i])

        getsum = dongx460_4A.two_sums(intlist,int(target))
        print("The two numbers that sum up to",target,"are",getsum[0],"and",getsum[2])
        togo = input("Would you like to enter another list?(y/n): ")
if __name__ == '__main__':
  main()
