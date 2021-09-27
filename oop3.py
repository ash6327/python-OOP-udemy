class circle:
    def __init__(self,radius):
        if self.radius<0:
            raise ValueError("enter value higher than 0")
        else:
            self.radius=radius
        
    @property
    def rad(self,radius:float):
            self.radius=radius
    @rad.setter
    def rad(self,new_radius):
        if new_radius<0:
            raise ValueError("Enter value higher than 0")
        else:
            self.radius=new_radius

    @property
    def diam(self):
        diameter=2*self.radius
        return diameter


    @property
    def circum(self):
        return 2*3.14*self.radius
    
    def area(self):
        return 3.14*self.radius**2

c1=circle(10)
print(c1.radius,c1.diam,c1.circum,c1.area())

c2=circle(-1)
print(c2.radius,c2.diam,c2.circum,c2.area())
