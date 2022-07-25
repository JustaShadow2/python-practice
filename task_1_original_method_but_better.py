
class area_perim:
    def __init__(self, area, perim):
        self.area = int(area)
        self.perim = int(perim)

    def calculate(self):
        if name in ('rectangle','Rectangle','square','Square','paralellogram','Paralellogram'):
            self.side1 = int(input('Input a length : '))
            self.side2 = int(input('Input a base : '))
            self.area = self.side1*self.side2
            self.perim = self.side1+self.side2+self.side1+self.side2
            
        elif name in ('triangle','Triangle'):
            height = int(input('Input a height : '))
            base1 = int(input('Input a base : '))
            side1 = int(input('Input a side length : '))
            side2 = int(input('Input another side length : '))
            self.area = height*base1//2
            self.perim = side1+side2+base1

        elif name in ('circle','Circle'):
            radius = int(input('Input a radius : '))
            self.area = radius*radius*3.14
            self.perim = radius*6.28

        elif name in ('trapezoid','Trapezoid'):
            base1 = int(input('Input the first base : '))
            base2 = int(input('Input the second base : '))
            height = int(input('Input the height : '))
            side1 = int(input('Input the first side : '))
            side2 = int(input('Input the second side : '))
            total_base = base1+base2
            self.area = total_base*height//2
            self.perim = side1+side2+total_base

    def __str__(self):
        return f'Area of the shape is {self.area}, perimeter of the shape is {self.perim}' 

name = input('Which shape do you want to calculate?')



p1 = area_perim
p1.calculate(name)
print(p1)


