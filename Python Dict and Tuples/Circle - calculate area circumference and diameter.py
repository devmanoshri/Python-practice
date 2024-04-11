
import math
def main():
    radius= float(input("Enter radius of the circle:"))
    diameter = round(2*radius,2)
    area= round(math.pi*radius**2,2)
    circumference= round(2*math.pi*radius,2)
    print("Radius of the circle:",radius)
    print("Diameter of the circle:", diameter)
    print("Area of the circle:", area)
    print("Circumference of the circle:", circumference)

if __name__ == '__main__':
    main()
