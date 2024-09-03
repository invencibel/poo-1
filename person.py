class Person():
    def give_name(self,name,lastname):
        self.name = name
        self.lastname = lastname
dani = Person()
dani.give_name("dani","sanzana")
print(dani.name,dani.lastname)