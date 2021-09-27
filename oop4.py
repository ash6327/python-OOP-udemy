class employee:
    min_age=18
    min_pay=20000
    def __init__(self,name,age,role):
        self.name = name
        self.age = age
        self.role=role

    @classmethod
    def set_min_age(cls,age):
        cls.min_age = age
    
    @classmethod
    def set_min_pay(cls,age):
        cls.min_age = age                               #classmethod is used to manipulate class variables.

    @classmethod
    def convert_string(cls,string:str):
        a,b,c=string.split(',')
        return cls(a,b,c)                                 #use of classmethod as constructor.

        

    @staticmethod
    def is_developer(role:str):                         #staticmethod is used to create independent variable functions inside classs.
        if role.lower()=='developer':
            return True
        else:
            return False
    
    @property
    def show(self):
        print(f"{self.name} is a {self.role} and is {self.age} years old")


print(employee.min_age)
employee.set_min_age(20)
print(employee.min_age)
print(employee.convert_string('ash,18,developer').show)