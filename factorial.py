def fac(n):
    if n == 0 or n == 1:
        return 1
    t = n*fac(n-1)
    return t

def getsin(angle,num_term):
    if num_term == 1:
        return angle
    else:
        return  ((-1)**(num_term-1))*((angle)**(2*num_term-1)/fac(2*num_term-1)) + getsin(angle,num_term-1)

def main():
    angle = float(input("Enter the angle to approximate(in radians): "))
    num_term = int(input("Enter the number of terms to compute: "))
    sin = getsin(angle,num_term)
    print("sin","(",angle,")","is approximately",sin)
if __name__ == '__main__':
  main()
