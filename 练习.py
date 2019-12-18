#class parent:

#    def hello(self):
        
#        print("正在调用父类的函数...")

#class child(parent):

#    pass

#p = parent()

#p.hello()

#q = child()

#q.hello()


import random as r

class Fish ():

    def __init__(self):

        self.x = r.randint(0, 10)

        self.y = r.randint(0, 10)

    def move(self):

        self.x  -= 1

        print("我的位置是:", self.x, self.y)

class Goldfish(Fish):

    pass

class Carp(Fish):

    pass

class Salmon(Fish):

    pass

class Shark(Fish):

    def __init__(self):

        Fish.__init__(self)

        self.hungry = True

    def eat(self):

        if self.hungry :

            print("吃货的梦想就是天天有吃的^_^")
            self.hungry = False

        else:

            print("太撑了，吃不下了!")

fish = Fish()

fish.move()

goldfish = Goldfish()

goldfish.move()
goldfish.move()
goldfish.move()
    
shark = Shark()

shark.eat()

shark.eat()

shark.eat()

shark.move()

shark.move()


class Foo1:

    def Base1(self):

        print("我是Foo1,我为Base1代言...")

class Foo2:

    def Base2(self):

         print("我是Foo2,我为Base2代言...")

class C(Foo1, Foo2):     #双重继承

    pass

c = C()

c.Base1()

c.Base2()
             
         