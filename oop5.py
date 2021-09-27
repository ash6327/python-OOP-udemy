class animal:
    def __init__(self,name:str,breed:str):
        self.name = name
        self.breed=breed

    def __eq__(self,other):
        if self.breed==other.breed:
            return True
        else:
            return False
a1=animal('tim','dog')
a2=animal('ash','cat')
a3=animal('cutey','dog')

print(a1==a2)
print(a1==a3)