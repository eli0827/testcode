class Person(object):

    def __init__(self,name,age=0):
        self.name=name
        self.age=age
#类对象
class Worker(Person):
    #类属性
    count=0
    def __init__(self,name,age):
        super().__init__(name,age)

    @classmethod
    def setAutoCount(cls):
        cls.count+=1

    @classmethod
    def printLog(self):
        print("log test")
#实例对象
xiaoming =Worker("小明",19)
xiaoming.setAutoCount()
print(Worker.count)
xiaoli =Worker("小李子",20)
xiaoli.setAutoCount()
xiaoli.count +=2
print(id(xiaoli.count))
print(id(Worker.count))
Worker.printLog()