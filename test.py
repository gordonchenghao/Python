class Animal:
    def __init__ (self, age, sex, name):
        self.age=age
        self.sex=sex
        self.name=name
    def greeting (self):
        print("Hello, I am "+self.name)
    def eat (self,food):
        print("I want to eat "+food)

a=Animal(2,"male","Tom")
a.greeting()
a.eat("can food")

class Dog(Animal):
    def __init__ (self, age, sex, name,price):
        super().__init__(age, sex, name)
        self.price=price
    def bark (self):
        print("My price is "+str(self.price))
b=Dog(3,"female","kk",1000)
b.bark()