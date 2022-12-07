# 继承和多态
class Animal():
    def __init__(self,name) -> None:
        self.name = name
    def greet(self):
        print("Hello,I am an %s"%self.name)
# Dag类继承Animal,Dag继承Animal，Animal的init就会被继承给Dag(子类和父类的关系)
class Dag(Animal):
    def greet(self):
        print(f"'wang..',I am %s"%self.name)
    def run(self):
        print(f"I am running")
class Cat(Animal):
    def greet(self):
        print(f"'miao..',I am a %s"% self.name)  
# 多态
# 定义一个hello方法，hello方法的参数是animal 
def hello(animal): 
    # 将animal 实例化为Animal,每次调用hello 方法后，animal参数的方法就会被调用
    animal.greet()
animal = Animal("animal")
animal.greet()
dog = Dag("dog")
hello(dog)    # 多态，使用hello调用子类中的greet方法
cat = Cat("cat")
hello(cat)