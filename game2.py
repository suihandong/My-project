def board():
    play = []
    i = 0
    for i in range(3):
        row = [" "]*3
        play.append(row)
        i += 1
    return play

def location(play,l,a):
    if l == 0:
        play[0][0]=a
    elif l == 1:
        play[0][1]=a
    elif l == 2:
        play[0][2]=a
    elif l == 3:
        play[1][0]=a
    elif l == 4:
        play[1][1]=a
    elif l == 5:
        play[1][2]=a
    elif l == 6:
        play[2][0]=a
    elif l == 7:
        play[2][1]=a
    elif l == 8:
        play[2][2]=a
    return play

def occupy(play,l):
    if l == 0:
        if play[0][0] == " ":
            return True
        else:
            return False
    elif l ==1:
        if play[0][1] == " ":
            return True
        else:
            return False
    elif l ==2:
        if play[0][2] == " ":
            return True
        else:
            return False
    elif l ==3:
        if play[1][0] == " ":
            return True
        else:
            return False
    elif l ==4:
        if play[1][1] == " ":
            return True
        else:
            return False
    elif l ==5:
        if play[1][2] == " ":
            return True
        else:
            return False
    elif l ==6:
        if play[2][0] == " ":
            return True
        else:
            return False
    elif l ==7:
        if play[2][1] == " ":
            return True
        else:
            return False
    elif l ==8:
        if play[2][2] == " ":
            return True
        else:
            return False

def togo(play):
    if play[0]==["x","x","x"] or play[0]==["o","o","o"]:
        return True
    elif play[1]==["x","x","x"] or play[1]==["o","o","o"]:
        return True
    elif play[2]==["x","x","x"] or play[2]==["o","o","o"]:
        return True
    elif play[0][0]==play[1][0]==play[2][0]=="x" or play[0][0]==play[1][0]==play[2][0]=="o":
        return True
    elif play[0][1]==play[1][1]==play[2][1]=="x" or play[0][1]==play[1][1]==play[2][1]=="o":
        return True
    elif play[0][2]==play[1][2]==play[2][2]=="x" or play[0][2]==play[1][2]==play[2][2]=="o":
        return True
    elif play[0][0]==play[1][1]==play[2][2]=="x" or play[0][0]==play[1][1]==play[2][1]=="o":
        return True
    elif play[0][2]==play[1][1]==play[2][0]=="x" or play[0][2]==play[1][1]==play[2][0]=="o":
        return True
    else:
        return False

def win(play):
    winer1 = "Player 1 wins!"
    winer2 = "Player 2 wins!"
    if play[0]==["x","x","x"] or play[1]==["x","x","x"] or play[2]==["x","x","x"]:
        return winer1
    elif play[0][0]==play[1][0]==play[2][0]=="x" or play[0][1]==play[1][1]==play[2][1]=="x" or play[0][2]==play[1][2]==play[2][2]=="x":
        return winer1
    elif play[0][0]==play[1][1]==play[2][2]=="x" or play[0][2]==play[1][1]==play[2][0]=="x":
        return winer1
    elif play[0]==["o","o","o"] or play[1]==["o","o","o"] or play[2]==["o","o","o"]:
        return winer2
    elif play[0][0]==play[1][0]==play[2][0]=="o" or play[0][1]==play[1][1]==play[2][1]=="o" or play[0][2]==play[1][2]==play[2][2]=="o":
        return winer2
    elif play[0][0]==play[1][1]==play[2][1]=="o" or play[0][2]==play[1][1]==play[2][0]=="o":
        return winer2

def main():
    count = 0
    play = board()
    go = togo(play)
    while count < 9 and go != True:
        if count % 2 == 0:
            l = int(input("Player 1, where would you like to move? "))
            oc = occupy(play,l)
            while oc != True:
                print("Sorry, that space is already taken")
                h = 0
                while h < 3:
                    print(play[h])
                    h += 1
                l = int(input("Player 1, where would you like to move? "))
                oc = occupy(play,l)
            a = "x"
            loc = location(play,l,a)
        elif count % 2 != 0:
            l = int(input("Player 2, where would you like to move? "))
            oc = occupy(play,l)
            while oc != True:
                print("Sorry, that space is already taken")
                h = 0
                while h < 3:
                    print(play[h])
                    h += 1
                l = int(input("Player 2, where would you like to move? "))
                oc = occupy(play,l)
            a = "o"
            loc = location(play,l,a)
        count += 1
        i = 0
        while i < 3:
            print(play[i])
            i += 1
        go = togo(play)
    winer = win(play)
    print(winer)

if __name__ == '__main__':
  main()
