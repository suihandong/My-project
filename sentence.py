def main():
    sen = str(input("Enter a sentence: "))
    sen = str.lower(sen)
    nsen = sen.split(" ")

    wlist = []
    idx=0
    while idx<len(nsen):
        ch = nsen[idx]
        if ch not in wlist:
            wlist.append(ch)
        idx+=1

    loc = []
    c = [0]*len(wlist)
    alist = list(nsen)
    i = 0
    j = 0
    while i < len(wlist):
        while j < len(nsen):
            count = nsen.count(wlist[i])
            c[i]= count
            if wlist[i] == nsen[j]:
                loc.append(j)
            else:
                loc = loc
            j +=1
        i += 1
        j = 0

    result = []
    x = 0
    y = 0
    for x in range(0,len(wlist)) or y in range(0,len(loc)):
        result.append(wlist[x])
        result.append(loc[y:y+c[x]])
        y = y + c[x]
        x+=1

    m = 0
    n = 0
    while m < len(result):
        print(result[m]," ",end = "")
        while n <len(result[m+1]):
            print(result[m+1][n]," ",end = "")
            n+= 1
        print()
        m += 2
        n = 0

    togo = input("Do you want to enter another sentence(Y/N)? ")
    while togo == "y" or togo == "Y":
        sen = str(input("Enter a sentence: "))
        sen = str.lower(sen)
        nsen = sen.split(" ")

        wlist = []
        idx=0
        while idx<len(nsen):
            ch = nsen[idx]
            if ch not in wlist:
                wlist.append(ch)
            idx+=1

        loc = []
        c = [0]*len(wlist)
        alist = list(nsen)
        i = 0
        j = 0
        while i < len(wlist):
            while j < len(nsen):
                count = nsen.count(wlist[i])
                c[i]= count
                if wlist[i] == nsen[j]:
                    loc.append(j)
                else:
                    loc = loc
                j +=1
            i += 1
            j = 0

        result = []
        x = 0
        y = 0
        for x in range(0,len(wlist)) or y in range(0,len(loc)):
            result.append(wlist[x])
            result.append(loc[y:y+c[x]])
            y = y + c[x]
            x+=1

        m = 0
        n = 0
        while m < len(result):
            print(result[m]," ",end = "")
            while n <len(result[m+1]):
                print(result[m+1][n]," ",end = "")
                n+= 1
            print()
            m += 2
            n = 0
        togo = input("Do you want to enter another sentence(Y/N)? ")

if __name__ == '__main__':
  main()
