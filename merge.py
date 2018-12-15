def merge2(sen1, sen2):
    result = []
    nlist1 = sen1.split(" ")
    nlist2 = sen2.split(" ")
    i = 0

    if len(nlist1)%2==0 and len(nlist2)%2==0:
        if len(nlist1) == len(nlist2):
            while i < len(nlist1):
                result.append(nlist1[i:i+2])
                result.append(nlist2[i:i+2])
                i += 2

        elif len(nlist1)<len(nlist2):
            while i < len(nlist1):
                result.append(nlist1[i:i+2])
                result.append(nlist2[i:i+2])
                i += 2
            result.append(nlist2[i:])

        elif len(nlist2)<len(nlist1):
            while i < len(nlist2):
                result.append(nlist1[i:i+2])
                result.append(nlist2[i:i+2])
                i += 2
            result.append(nlist1[i:])

    if len(nlist1)%2!=0 and len(nlist2)%2==0:
        if len(nlist1) > len(nlist2):
            while i < len(nlist2):
                result.append(nlist1[i:i+2])
                result.append(nlist2[i:i+2])
                i += 2
            result.append(nlist1[i:])

        elif len(nlist1) < len(nlist2):
            while i < len(nlist1)-1:
                result.append(nlist1[i:i+2])
                result.append(nlist2[i:i+2])
                i += 2
            result.append(nlist1[i:])
            result.append(nlist2[i:])

    if len(nlist1)%2==0 and len(nlist2)%2!=0:
        if len(nlist1) > len(nlist2):
            while i < len(nlist2)+1:
                result.append(nlist1[i:i+2])
                result.append(nlist2[i:i+2])
                i += 2
            result.append(nlist2[i:])
            result.append(nlist1[i:])

        elif len(nlist1) < len(nlist2):
            while i < len(nlist1):
                result.append(nlist1[i:i+2])
                result.append(nlist2[i:i+2])
                i += 2
            result.append(nlist2[i:])

    if len(nlist1)%2!=0 and len(nlist2)%2!=0:
        if len(nlist1)==len(nlist2):
            while i < len(nlist1)-1:
                result.append(nlist1[i:i+2])
                result.append(nlist2[i:i+2])
                i += 2
            result.append(nlist1[i:])
            result.append(nlist2[i:])

        elif len(nlist1)<len(nlist2):
            while i < len(nlist1)-1:
                result.append(nlist1[i:i+2])
                result.append(nlist2[i:i+2])
                i += 2
            result.append(nlist1[i:])
            result.append(nlist2[i:])

        elif len(nlist1)>len(nlist2):
            while i < len(nlist2)+1:
                result.append(nlist1[i:i+2])
                result.append(nlist2[i:i+2])
                i += 2
            result.append(nlist2[i:])
            result.append(nlist1[i:])



    res = ""
    x = 0
    y = 0

    while x < len(result):
        while y < len(result[x]):
            res = res + result[x][y] + " "
            y += 1
        y = 0
        x += 1
  return res
