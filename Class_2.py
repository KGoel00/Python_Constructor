class addition:
    x=0
    y=0
    def __init__(self):
        self.x = 2
        self.y = 3
        print(self.x+self.y)

    # def sumOfNum(self):
    #     print((self.x+self.y))

obj=addition()
# obj.sumOfNum()



class demo:
    name = ""  # field data
    sal = 0
    age = 0

    def __init__(self):
        print("This constructor is non-parameterized")


    def func(self):
        print("My name is %s and my salary is %d. I am %d years old" % (self.name, self.sal, self.age))

    def func(self, name, sal, age):
        print("My name is %s and my salary is %d. I am %d years old" % (name, sal, age))

obj1 = demo()
obj1.func("Sarah", 1500, 23)