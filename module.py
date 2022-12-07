# 模块的调用：一个python文件，以.py结尾 
from class_1 import Animal
from class_1 import Dag,Cat

animal = Animal("animal")
animal.greet()
dog = Dag("dog")
dog.greet()

import class_1
cat = class_1.Cat("cat")
cat.greet()