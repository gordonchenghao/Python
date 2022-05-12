class Student:
    def __init__ (self, fname, lname):
        self.fname = fname
        self.lname = lname
        self.age = 18
    def __str__ (self):
        return f'don\' print me'

    def fullname (self):
        print(self.fname+" "+self.lname)

tom=Student("tom","h")
ollie=Student("vcsdv","fwv")
print(ollie)

tom.fullname()
ollie.fullname()
Student.fullname(tom)
Student.fullname(ollie)

