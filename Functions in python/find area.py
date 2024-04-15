# Take base and height as a input and calculate area of triangle from a function
# Take length and width of a rectangle and calculate area of rectangle from a function
def calculate_area(base,height,shape):
    if shape=='triangle':
        area = 1 / 2 * int(base) * int(height)
        return (area)
    elif shape=='rectangle':
        area=int(base) * int(height)
        return (area)
    else:
        return(print("Try again!"))

shape_type=input("Enter shape:")
if shape_type=='triangle':
    base_val = input("Enter base of triangle:")
    height_val = input("Enter height of triangle:")
    triangle_area = calculate_area(base_val, height_val,'triangle')
    print("Area is of triangle:", triangle_area)
elif shape_type=='rectangle':
    length_val = input("Enter length of rectangle:")
    width_val = input("Enter width of rectangle:")
    rectangle_area = calculate_area(length_val, width_val, 'rectangle')
    print("Area is of rectangle:", rectangle_area)
else:
    print('You can ask only for either triangle or rectangle. Try again!')








