import turtle

class County:
    def __init__(self, country_name, pop_list):
        self.cn = country_name
        i = 0
        while i < len(pop_list):
            pop_list[i] = int(pop_list[i])
            i += 1
        self.pl = pop_list
        mi = (-1)/7
        m_val = 0
        b_val = 0
        for i in range(0,len(self.pl)):
            m_val += int(self.pl[i]) * mi
            mi += 2/35
        bi = 11/21
        for j in range(0,len(self.pl)):
            b_val += int(self.pl[i]) * bi
            bi -= 3/21
        self.m = m_val
        self.b = b_val

    def __lt__(self, rhand):
        if self.m < rhand.m:
            return True

    def getslope(self):
        return self.m

    def display(self, y_max = 200):
        yearlist = [2010, 2011, 2012, 2013, 2014, 2015]
        turtle.pencolor("red")
        x_year = [-300, -190, -80, 30, 140, 250]

        max_pop = self.pl[0]
        for idx in range(1,len(self.pl)):
            if max_pop < self.pl[idx]:
                max_pop = self.pl[idx]

        for i in range(0,len(self.pl)):
            if self.pl[i] == 0:
                y = -300
            elif self.pl[i] == max_pop:
                y = y_max

        y_one = max_pop / (y_max - (-300))
        ylst = []
        for j in range(0,len(self.pl)):
            val_y = self.pl[j] * y_one
            ylst.append(val_y)
            turtle.penup()
            turtle.goto(x_year[j],val_y-300)
            turtle.pendown()
            turtle.dot()

        k_val = (y_max + 300)/max_pop
        turtle.penup()
        turtle.goto(-300,k_val * ylst[0] - 300)
        turtle.pendown()
        turtle.goto(250,k_val * ylst[5] - 300)
        turtle.penup()
        turtle.goto(200,150)

        for k in range(0,len(x_year)):
            turtle.penup()
            turtle.goto(x_year[k],-350)
            turtle.pendown()
            turtle.write(yearlist[k])

        turtle.penup()
        turtle.goto(0,y_max)
        turtle.pendown()
        turtle.write(self.cn)
        turtle.penup()
        turtle.goto(250,y_max)
        turtle.pendown()
        turtle.write("y = ",k_val,"x + ")

class State(County):
    def __init__(self, name, poplst, county_list):
        County.__init__(self, name, poplst)
        self.cl = county_list
        #calculate the y and r

    def __lt__(self, rhand):
        if self.m < rhand.m:
            return True

    def getname(self):
        return self.cn

    def getCountyList(self):
        return self.cl

    def getslope(self):
        return self.m

    def display(self):
        turtle.pencolor("blue")
        x_year = [-300, -190, -80, 30, 140, 250]

        max_pop = self.pl[0]
        for idx in range(1,len(self.pl)):
            if max_pop < self.pl[idx]:
                max_pop = self.pl[idx]
            else:
                max_pop = max_pop

        for i in range(0,len(self.pl)):
            if self.pl[i] == 0:
                y = -300
            elif self.pl[i] == max_pop:
                y = 200

        y_one = max_pop / (200 - (-300))
        ylst = []
        for j in range(0,len(self.pl)):
            val_y = self.pl[j] * y_one
            ylst.append(val_y)
            turtle.penup()
            turtle.goto(x_year[j],val_y-300)
            turtle.pendown()
            turtle.dot()

        k_val = (y_max + 300)/max_pop
        turtle.penup()
        turtle.goto(-300,k_val * ylst[0] - 300)
        turtle.pendown()
        turtle.goto(250,k_val * ylst[5] - 300)
        turtle.penup()
        turtle.goto(200,150)

        for k in range(0,len(x_year)):
            turtle.penup()
            turtle.goto(x_year[k],-350)
            turtle.pendown()
            turtle.write(yearlist[k])

class Analysis:
    def __init__(self, state_list):
        self.sl = state_list

    def displayState(self, name):
        for i in range(0,len(self.sl)):
            state = self.sl[i]
            if name.lower() == state.getname().lower:
                state.display()

    def displayStateGreatestCounty(self, name):
        county = None
        for i in self.sl:
            if name.lower() == i.getname().lower:
                max_slope = (i.getCountyList())[0].getslope()
                for j in i.getCountyList():
                    if max_slope < j.getslope():
                        max_slope = j.getslope()
                county = j
        county.display()

    def displayStateLeastCounty(self, name):
        county2 = None
        for i in self.sl:
            if name.lower() == i.getname().lower:
                min_slope = (i.getCountyList())[0].getslope()
                for j in i.getCountyList():
                    if j.getslope() < min_slope:
                        min_slope = j.getslope()
                county2 = j
        county2.display()

    def clear(self):
        turtle.clear()

    def greatestState(self):
        max_growth = self.sl[0]
        for i in self.sl:
            if max_growth.getslope() < i.getslope():
                max_growth = i
        print(max_growth.getname())

    def leastState(self):
        min_growth = self.sl[0]
        for i in self.sl:
            if i.getslope() < min_growth.getslope():
                min_growth = i
        print(min_growth.getname())

f = open("censusdata.csv", "r")
flag = True
lst = f.readline()
county_list = []
state_list = []
pop_list = []
for line in f:
    lst = f.readline()
    lst = lst.lower()
    lst = lst.split(",")
    name = lst[0]
    pop_list = lst[1:]
    if "county" in name:
        c = County(name,pop_list)
        county_list.append(c)
    else:
        if flag:
            name = lst[0]
            pop_list = lst[1:]
            flag = False
        else:
            s = State(name,pop_list,county_list)
            state_list.append(s)
            county_list = []
            pop_list = lst[1:]
            name = lst[0]

a = Analysis(state_list)
