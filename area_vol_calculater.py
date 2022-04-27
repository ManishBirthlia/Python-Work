
# these are for areas
def area_of_circles(r):
    area=3.14*r*r
    return area

def area_of_sphere(r):
    area=4*3.14*r*r
    return area

def area_of_cylinder(r,h):
    area=2*3.14*r*r + 2*3.14*r*h
    return area

def area_of_cone(r,h):
    area=3.14*r*r+3.14*(r*r+h*h)**(1/2)
    return area
#these are for volumes 
def volume_of_sphere(r):
    volume=4/3*3.14*r^3
    return volume

def volume_of_cylinder(r,h):
    volume=3.14*(r^2)*h
    return volume

def volume_of_cone(r,h):
    volume=3.14*(r^2)*h/3
    return volume
#taking inputs
a=input('take any geomatry\n')
r=int(input('take radius\n'))
#workings
if a=="circle":
    print(f'surface area of circle is :{area_of_circles(r)}')
elif a=="sphere":
    print(f'surface area of sphere is :{area_of_sphere(r)}')
    print(f'volume of sphere is :{volume_of_sphere(r)}')
elif a=="cylinder":
    h=int(input('take height\n'))
    print(f'surface area of cylinder is :{area_of_cylinder(r,h)}')
    print(f'volume of cylinder is :{volume_of_cylinder(r,h)}')
elif a=="cone":
    h=int(input('take height\n'))
    print(f'surface area of cone is :{area_of_cone(r,h)}')
    print(f'volume of cone is :{volume_of_cone(r,h)}')
else:
    print('take geomatry of circle ,sphere ,cylinder or cone\nand run again')
