class Person():
    def __init__(self, name ,lastname):
        self.name= name
        self.lastname= lastname
    def chenge_color(self,color):
        self.eyescolor= color
    def say_hello(self):
        print(f"hello, my name is {self.name}")

    #atributos de objeto persona
        #name
        #lastname
        pass
person1= Person("Daniela","Sanzana")
print(person1)
print(person1.name,person1.lastname)
person2=Person("Constanza","Reyes")
print(person2.name,person2.lastname)
person1.chenge_color("pink")
person2.chenge_color("green")
person1.say_hello()
person2.say_hello()