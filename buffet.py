def main():
    print("Welcome to the Python Buffet, the hippest restaurant in town")
    print()
    olst = []
    ls = str(input("What would you like to order? "))
    count = 0
    i = 0

    while ls != "":
        if ls not in olst:
            olst.append(ls)
            if "burger" in ls:
                count += 3
            elif "soda" in ls:
                count += 2
            else:
                count +=5
        else:
            olst = olst
            print("Oops. You must have enternd",ls,"again by accident")
        ls = str(input("Would you like to order anything else? "))

    print("You have ordered the following:")

    while i < len(olst):
        print(olst[i])
        i += 1

    print("This will cost youa total of $", float(count))
    print("Thank you for your patronage!")

if __name__ == '__main__':
  main()
