def validatedate(month,day):
    if month <= 0 or month > 12 or day <= 0:
        return False
    else:
        while month ==2:
            if day >28:
                return False
            else:
                return True
        while month == 1 or month == 3 or month ==5 or month == 7 or month ==8 or month == 10 or month == 12:
            if day > 31:
                return False
            else:
                return True
        while month ==4 or month == 6 or month == 9 or month == 11:
            if day >30:
                return False
            else:
  return True
  
  def main():
    month = int(input("Month of birth: "))
    day = int(input("Day if birth: "))
    truth = validatedate(month,day)
    while truth == False:
        print("Invalid date")
        month = int(input("Month of birth: "))
        day = int(input("Day if birth: "))
        truth = validatedate(month,day)
    if truth == True:
        if month == 1:
            if day>=20:
                print("Aquarius")
            else:
                print("Capricorn")
        if month == 2:
            if day<=18:
                print("Aquariu")
            else:
                print("Pisces")
        if month == 3:
            if day<=20:
                print("Pisces")
            else:
                print("Aries")
        if month == 4:
            if day<=19:
                print("Aries")
            else:
                print("Taurus")
        if month == 5:
            if day<=20:
                print("Taurus")
            else:
                print("Gemini")
        if month == 6:
            if day<=20:
                print("Gemini")
            else:
                print("Cancer")
        if month ==7:
            if day<=22:
                print("Cancer")
            else:
                print("Leo")
        if month ==8:
            if day<=22:
                print("Leo")
            else:
                print("Virgo")
        if month ==9:
            if day<=22:
                print("Virgo")
            else:
                print("Libra")
        if month ==10:
            if day<=22:
                print("Libra")
            else:
                print("Scorpio")
        if month ==11:
            if day<=21:
                print("Scorpio")
            else:
                print("Sagittarius")
        if month ==12:
            if day<=21:
                print("Sagittarius")
            else:
                print("Capricorn")

if __name__ == '__main__':
  main()
