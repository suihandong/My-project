def intvert(lst):
    nlist = []
    inlist = []
    j = 0
    for i in range(len(lst)):
        if type(lst[i]) is int:
            nlist.append(lst[i])
        else:
            nlist = nlist
    for j in range(len(nlist)):
        inlist.append(nlist[len(nlist)-1])
        nlist.remove(nlist[len(nlist)-1])
  return inlist
