def parse_string(astring):
    bstr = ",.?![]()-"
    for idx in bstr:
        astring = astring.replace(idx,"")
    omstr = "to,the,and,I,of,he,she,a,I'll,I've,but,by,we,whose,how,go,such,this,me,can,she's,he's,have,has,had,an,did,so,to,we'll,on,him,well,or,be,as,those,there,are,do,too,if,it,at,what,that,you,will,in,with,not,for,is,my,o,her,his,am"
    omstr = omstr.lower()
    omlist = omstr.split(",")
    #print(omlist)
    dic = {}
    nwl = []
    astring = astring.lower()
    wl = astring.split(" ")
    for i in range(0,len(wl)):
        if wl[i] not in omlist:
            nwl.append(wl[i])
    

    for k in range(0,len(nwl)):
        if nwl[k] in dic:
            dic[nwl[k]] += 1
        else:
            dic[nwl[k]] = 1
   
    klist = list(dic.keys())
    for h in range(0,len(klist)):
        if dic[klist[h]] < 5:
            print(klist[h], " ", "*"*dic[klist[h]])
        elif dic[klist[h]] == 5:
            print(klist[h], " ", "X")
        else:
            val = dic[klist[h]] % 5
            re = dic[klist[h]] // 5
  print(klist[h], " ", "X"*val, "*"*re)
