def absError(aval,mval):
    if aval > mval:
        return round(aval-mval,6)
    else:
        return round(mval-aval,6)
        
def relError(aval,mval):
    abse = absError(aval,mval)
    return round(abse/aval,6)
