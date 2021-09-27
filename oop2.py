class person:
    def __init__(self,name:str,age:int):
        self.name=name
        self.age=age
    def display(self):
        print(f'My name is :{self.name}.I am {self.age} years old')
    def greet(self):
        if self.age>50:
            print("how are you doing")
        else:
            print("how you doin")

p1=person('ash',21)
p1.display()
p1.greet()