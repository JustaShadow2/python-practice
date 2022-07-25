'''
Arjun Atwal
Mr. Park
Python OOP Assessment

This program automates simple calculations, in this case calculating area and perimeter of different shapes
User inputs side measurements and shape specification, and the code outputs the area and perimeter
'''
#WHY DOES RETURN MAKE IT NOT WORK, ALWAYS OUTPUTS <function triangle.calc_triangle at 0x000001EA99446EE0>...see below for what happens after substituting return for print function. edit : solved, I just want to make a note that it took a solid 2 hours of constant tempter tantrums 

class Triangle:                                                                                                                     #code for triangle
    def __init__(self, base, height, side1, side2):                                                                                 #2 inputs, base and height
        self.__base = int(base)
        self.__height = int(height)
        self.side1 = int(side1)
        self.side2 = int(side2)
        self.perim_triangle = 0
        self.area_triangle = 0

    def calc_triangle(self):                                                                                                        #calculates area and perimeter
        self.area_triangle = self.__base*self.__height//2                                                                            #//2 keeps it as int isntead of float. if float, code has a seizure
        self.perim_triangle = self.__base+self.side1+self.side2

    def __str__(self):                                                                               
        return f'Area of the triangle is {self.area_triangle}, perimeter of the triangle is {self.perim_triangle}'                #returns area and perimeter as the values to the class (base override)

    def __repr__(self):
        return f'Area of the triangle is {self.area_triangle}, perimeter of the triangle is {self.perim_triangle}'                #used for debugging, less user friendly. therefore it is not called (base override)

class Rectangle:                                                                                                                    #code for rectangles, squares, parallelograms and other shapes with the same area and perimiter formula
    def __init__(self, side1, side2):                                                                                               #2 inputs for side lengths
        self.__side1 = int(side1)
        self.__side2 = int(side2)
        self.area_rectangle = 0
        self.perim_rectangle = 0

    def calc_rectangle(self):                                                                                                       #calculates area and perimeter
        self.area_rectangle = self.__side1*self.__side2
        self.perim_rectangle = self.__side1+self.__side1+self.__side2+self.__side2

    def __str__(self):                                                                                 
        return f'Area of the shape is {self.area_rectangle}, perimeter of the shape is {self.perim_rectangle}'                    #returns area and permimeter as the values to the class

    def __repr__(self):
        return f'Area of the shape is {self.area_rectangle}, perimeter of the shape is {self.perim_rectangle}'                    #used for debugging, less user friendly. therefore it is not called

class Circle:                                                                                                                       #code for circle
    def __init__(self, radius):                                                                                                     #only need radius
        self.__radius = int(radius)
        self.area_circle = 0
        self.circ_circle = 0

    def calc_circle(self):                                                                                                          #calculates area and perimeter
        self.area_circle = self.__radius*self.__radius*3.14                                                                          #sub pi for 3.14, less accurate but easier to work with and close enough that margin for error is excusable
        self.circ_circle = self.__radius*6.28

    def __str__(self):                                                                               
        return f'Area of the circle is {self.area_circle}, circumfrence of the circle is {self.circ_circle}'                      #returns area and perimeter as the values to the class

    def __repr__(self):
        return f'Area of the circle is {self.area_circle}, circumfrence of the circle is {self.circ_circle}'                      #used for debugging, less user friendly. therefore it is not called

class Trapezoid:
    def __init__(self, base1, base2, height, side1, side2):                                                                         #a lot of inputs are needed since only some of the values can be used for both area and perimeter
        self.__base1 = int(base1)
        self.__base2 = int(base2)
        self.__height = int(height)                                                                                                 #height and base are used for area
        self.__side1 = int(side1)
        self.__side2 = int(side2)
        self.area_trapezoid = 0
        self.perim_trapezoid = 0                                                                                                    #side and base are used for perimeter

    def calc_trapezoid(self):                                                                                                       #calculates area and perimeter
        self.__base_total = self.__base1+self.__base2
        self.__side_total = self.__side1+self.__side2
        self.area_trapezoid = self.__base_total*self.__height//2
        self.perim_trapezoid = self.__base_total+self.__side_total

    def __str__(self):                                                                               
        return f'Area of the trapezoid is {self.area_trapezoid}, perimeter of the trapezoid is {self.perim_trapezoid}'            #returns area and perimeter as the values to the class

    def __repr__(self):
        return f'Area of the trapezoid is {self.area_trapezoid}, perimeter of the trapezoid is {self.perim_trapezoid}'            #used for debugging, less user friendly. therefore it is not called

shape = input('input a shape (rectangle, square, parallelogram, trapezoid, triangle, circle) : ')                                   #determines which class is called                           

if shape == 'triangle':
    user_input1 = input('input a base : ')                                                                                          #asks for values
    user_input2 = input('input a height : ')
    user_input3 = input('input a side length : ') 
    user_input4 = input('input another side length : ')                                                          
    p1 = Triangle(user_input1, user_input2, user_input3, user_input4)                                                                                         #sets p1 = class, using the values given as the attributes
    p1.calc_triangle()                                                                                                              #runs the calculation function within the class
    print(p1)                                                                                                             #calls the returned value, prints it

if shape == 'trapezoid':                                                                                                            #same code as above, but for trapezoids and its related class and functions
    user_input1 = input('input a base : ')                                                                  
    user_input2 = input('input another base : ')
    user_input3 = input('input a height : ')
    user_input4 = input('input a side length : ')
    user_input5 = input('input another side length : ')
    p1 = Trapezoid(user_input1, user_input2, user_input3, user_input4, user_input5)                         
    p1.calc_trapezoid()                                                                                     
    print(p1)

if shape == 'circle':                                                                                                               #same code as above, but for circles and its related class and functions
    user_input1 = input('input a radius : ')                                                                
    p1 = Circle(user_input1)                                                                                
    p1.calc_circle()
    print(p1)                                                             

if shape in ('square', 'rectangle', 'parallelogram'):                                                                               #same code as above, but for squares, rectangles and paralellograms and their related class anf functions
    user_input1 = input('input a side length : ')                                                                 
    user_input2 = input('input another side length : ')                                                           
    p1 = Rectangle(user_input1, user_input2)                                                                
    p1.calc_rectangle() 
    print(p1)                                                                                     