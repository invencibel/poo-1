class Person():
    def give_name(self,name,lastname):
        self.name = name
        self.lastname = lastname
dani = Person()
dani.give_name("dani","sanzana")
print(dani.name,dani.lastname)
bob=  Person()
bob.give_name("bob","esponja")
print(bob.name,bob.lastname)
patricio= Person()
patricio.give_name("patricio","estrella")
print(patricio.name,patricio.lastname)
