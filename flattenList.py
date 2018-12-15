def flattenList(alist):
    if len(alist) ==0:
        return alist
    else:
        if type(alist[0]) is list:
            return flattenList(alist[0])+flattenList(alist[1:])
        else:
  return [alist[0]]+flattenList(alist[1:])
