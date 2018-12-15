#python project
def focalLength(obj, im):
    F = obj**(-1)+im**(-1)#F is 1/f
    f = F**(-1)
    return f
    
def main():
    print("Welcome to the Focal Length Calculator!")
    obj = float(input("Enter an object distance, in mm:  "))
    im = float(input("Enter an image distance, in mm: "))
    Focal_Length = focalLength(obj,im)
    print("Focal Length: ",Focal_Length," mm")
    
if __name__ == '__main__':
  main()
