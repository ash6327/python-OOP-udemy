class person:
    def set_details(self,name,age=0):
        self.name=name
        self.age=age
    def display(self):
        print(f'My name is :{self.name}.I am {self.age} years old')
    def greet(self):
        if self.age>50:
            print("how are you doing")
        else:
            print("how you doin")

p1=person()
p1.set_details('ash',21)
p2=person()
p2.set_details('ashi',21)

p1.display()
p1.greet()
p2.display()
p2.greet()