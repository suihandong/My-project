class Complex:
    def __init__(self, real = 0.0, imag = 0.0):
        self.r = float(real)
        self.i = float(imag)

    def __add__(self, rhand):
        nr = self.r + rhand.r
        ni = self.i + rhand.i
        return Complex(nr, ni)

    def __sub__(self, rhand):
        n_r = self.r - rhand.r
        n_i = self.i - rhand.i
        return Complex(n_r, n_i)

    def __mul__(self, rhand):
        newr = (self.r * rhand.r) - (self.i * rhand.i)
        newi = (self.r * rhand.i) + (rhand.r * self.i)
        return Complex(newr, newi)

    def __truediv__(self, rhand):
        if rhand.r == 0 and rhand.i == 0:
            return ("None; Divide by Zero Error!")
        else:
            new_r = ((self.r * rhand.r) + (self.i * rhand.i))/((rhand.r**2) + (rhand.i**2))
            new_i = ((self.i * rhand.r) - (self.r * rhand.i))/((rhand.r**2) + (rhand.i**2))
            return Complex(new_r, new_i)

    def __str__(self):
        if self.r == 0 and self.i != 0:
            return str(self.i) + "i"
        elif self.i == 0 and self.r != 0:
            return str(self.r)
        elif self.i == 0 and self.r == 0:
            return str(0)
        elif self.i <0:
            return str(self.r) + str(self.i) + "i"
        else:
            return str(self.r) + "+" + str(self.i) + "i"

def main():
    r1 = float(input("Enter the real part of the first complex number: "))
    i1 = float(input("Enter the imaginary part of the first complex number: "))
    r2 = float(input("Enter the real part of the second complex number: "))
    i2 = float(input("Enter the imaginary part of the second complex number: "))
    c1 = Complex(r1,i1)
    c2 = Complex(r2,i2)
    print("C1 = ", c1)
    print("C2 = ", c2)
    print("C1 + C2 = ", c1+c2)
    print("C1 - C2 = ", c1-c2)
    print("C1 * C2 = ", c1*c2)
    print("C1 / C2 = ", c1/c2)

if __name__ == '__main__':
  main()
