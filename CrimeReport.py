def crime_report(fnameCSV):
    theft_dic = {}
    burglary_dic = {}
    robbery_dic = {}

    f = open(fnameCSV, 'r')
    fline = f.readline()
    fline = f.readline()
    dis = []
    cri = []
    while len(fline) != 0:
        fline = fline.lower()
        fline = fline.split(",")
        dis.append(fline[2])
        cri.append(fline[5])
        fline = f.readline()

    for i in range(0,len(dis)):
        if "theft" in cri[i]:
            if dis[i] in theft_dic:
                theft_dic[dis[i]] += 1
            else:
                theft_dic[dis[i]] = 1
        if "burglary" in cri[i]:
            if dis[i] in burglary_dic:
                burglary_dic[dis[i]] += 1
            else:
                burglary_dic[dis[i]] = 1
        if "robbery" in cri[i]:
            if dis[i] in robbery_dic:
                robbery_dic[dis[i]] += 1
            else:
                robbery_dic[dis[i]] = 1

    nf = open("stealingOffenses.txt", "w")
    klst = list(burglary_dic.keys())
    klst.sort()
    nf.write("Burglaries by District:\n")
    for x in range(0,len(klst)):
        nf.write(str(klst[x]) + " : " + str(burglary_dic[klst[x]]) + "\n")
    nf.write("\n")
    nf.write("Thefts by District:\n")
    for y in range(0,len(klst)):
         nf.write(str(klst[y]) + " : " + str(theft_dic[klst[y]]) + "\n")
    nf.write("\n")
    nf.write("Robberies by District:\n")
    for z in range(0,len(klst)):
         nf.write(str(klst[z]) +  " : " + str(robbery_dic[klst[z]]) + "\n")
    nf.write("\n")
    nf.close()
    f.close()

def main():
  crime_report("SacramentocrimeJanuary2006.csv")
