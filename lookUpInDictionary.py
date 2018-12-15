def lookup(d,item):
    code = {'pizza':127829, 'chicken':127831, 'apple':127822, 'peach':127825, 'cherry':127826, 'yam':127840, 'pineapple':127821, 'cookie':127850, 'bread':127838, 'lemon':127819, 'banana':127820, 'strawberry':127827}
    if item in d and item in code:
        return (item,chr(code[item])*d[item])
    elif item in d and item not in code:
        return (item,d[item])

def addItem(d,item):
    if item in d:
        d[item] += 1
    else:
        d[item] = 1

def subItem(d,item):
    if item in d:
        d[item] -= 1
        if d[item] == 0:
            del d[item]

def show(d):
    code = {'pizza':127829, 'chicken':127831, 'apple':127822, 'peach':127825, 'cherry':127826, 'yam':127840, 'pineapple':127821, 'cookie':127850, 'bread':127838, 'lemon':127819, 'banana':127820, 'strawberry':127827}
    klist = list(d.keys())
    for i in range(0,len(klist)):
        if klist[i] not in code:
            print(klist[i]," ",d[klist[i]])
        print(klist[i]," ",chr(code[klist[i]])*d[klist[i]])


def main():
    d = {}
    wtc = input("=> ")
    wtc= str.lower(wtc)
    wtcl = wtc.split(" ")
    if len(wtcl) >1:
        item = wtcl[1]
    if wtcl[0] =="lookup":
        lookup(d,item)
        if item in d:
            res = lookup(d,item)
            print(res[0], " ",res[1])
    elif wtcl[0] == "add":
        addItem(d,item)
    elif wtcl[0] == "sub":
        subItem(d,item)
    elif wtcl[0] == "show":
        show(d)
    while wtc != "quit":
        wtc = input("=> ")
        wtc= str.lower(wtc)
        wtcl = wtc.split(" ")
        if len(wtcl) >1:
            item = wtcl[1]
        if wtcl[0] =="lookup":
            lookup(d,item)
            if item in d:
                res = lookup(d,item)
                print(res[0], " ",res[1])
        elif wtcl[0] == "add":
            addItem(d,item)
        elif wtcl[0] == "sub":
            subItem(d,item)
        elif wtcl[0] == "show":
            show(d)
if __name__ == '__main__':
  main()
