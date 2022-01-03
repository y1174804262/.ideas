class Dog():
    """一次模拟小狗的简单尝试"""
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def sit(self):
        """模拟小狗被命令时蹲下"""
        print(self.name + "请蹲下")

    def roll(self):
        """模拟小狗被命令时打滚"""
        print(self.name + "请滚")

my_dog = Dog('张凯',21)
my_dog.sit()
my_dog.roll()

your_dog = Dog("张如辉",22)
your_dog.sit()