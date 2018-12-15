def game(ch1,ch2):
    if ch1 == "r" or ch1 =="R":
        if ch2 == "s" or ch2 == "S":
            return 1
        elif ch2 == "p" or ch2 =="R":
            return 2
    if ch1 == "s" or ch1 == "S":
        if ch2 == "p" or ch2 =="P":
            return 1
        elif ch2 == "r" or ch2 == "R":
            return 2
    if ch1== "p" or ch1 == "P":
        if ch2 =="r" or ch2 =="R":
            return 1
        elif ch2 == "s" or ch2 == "S":
            return 2

def main():
    i = 1
    count = 0
    c1 = 0
    c2 = 0
    while count <3:
        print("Round # ",i)
        ch1 = str(input("Player 1's Choice: "))
        ch2 = str(input("Player 2's Choice: "))
        if ch1 == ch2:
            count += 0
            print("No one wins this round")
        elif ch1 != ch2:
            win = game(ch1,ch2)
            print("Player",win,"wins this round")
            if win == 1:
                c1 +=1
            elif win == 2:
                c2 += 1
            count +=1
        i += 1
    if c1 > c2:
        print("Player 1 wins the game")
    elif c2>c1:
        print("Player 2 wins the game")

if __name__ == '__main__':
  main()
