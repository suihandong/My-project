def two_sums(aList, target):
    for i in range(0,len(aList)-1):
        if type(aList[i]) is int and type(target) is int:
            togo = True
        else:
            togo = False

    i = 0
    j = 1
    if togo == False:
        return("ERROR")
    else:
        while i < len(aList):
            while j < len(aList):
                if int(aList[i])>0 and int(aList[j])<0:
                    result = int(aList[i]) - abs(int(aList[j]))
                elif int(aList[i])>0 and int(aList[j])>0:
                    result = int(aList[i]) + int(aList[j])
                elif int(aList[i])<0 and int(aList[j])>0:
                    result = int(aList[j]) - abs(int(aList[i]))
                elif int(aList[i])<0 and int(aList[j])<0:
                    result = (-1)*(abs(int(aList[i])) + abs(int(aList[j])))
                if target != result:
                    j += 1
                else:
                    return(aList[i], " ",aList[j])
            i += 1
j = i+1
