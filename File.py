def mine_file(fname):
    f = open(fname, "r")
    cf = f.read()
    c_f = cf.lower()

    bdstr = ";.-,?!:"
    for idx in bdstr:
        c_f = c_f.replace(idx,"")
        c_f = c_f.replace("\n"," ")
    c_f = c_f.split(" ")
    word_count = len(c_f)

    udic = {}
    for j in range(0,len(c_f)):
        if c_f[j] not in udic:
            udic[c_f[j]] = 1
        else:
            udic[c_f[j]] += 1
    unique_count = len(udic)

    apo_count = 0
    for k in range(0,len(c_f)):
        if "'" in c_f[k]:
            apo_count += 1

    print("For the file ", fname, ":")
    print("Word Count: ", word_count)
    print("Unique Word Count: ", unique_count)
    print("Apostrophe Word Count: ",apo_count)
    klist = list(udic.keys())
    for h in range(0,len(klist)):
        if udic[klist[h]] >= 5:
            print(klist[h], ":", udic[klist[h]])
    f.close()
    
def main():
    mine_file("macbeth.txt")
if __name__ == '__main__':
main()
