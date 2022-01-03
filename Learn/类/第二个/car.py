class Car():
    """一次模拟汽车的简单尝试"""

    """ def __init__(self,make,model,year):
         #初始化汽车属性
         self.make = make
         self.model = model
         self.year = year

     def get_descriptive_name(self):
         long_name = str(self.year) + "年" +self.make + "制造了" + self.model
         print(long_name)

 my_new_car = Car('中国','比亚迪','2000')
 my_new_car.get_descriptive_name()

    #给属性指定默认值
    def __init__(self, make, model, year):
        #初始化汽车属性
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + "年" + self.make + "制造了" + self.model
        return long_name

    def read_odometer(self):
        #打印一条指出汽车里程的消息
        print("这辆车现在的时速是" + str(self.odometer_reading))

    def update_odometer(self,mileage):


my_new_car = Car('中国','红旗',1999)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

my_new_car.odometer_reading = 10
my_new_car.read_odometer()

"""
#修改属性的值
    #1、直接修改属性值
    def __init__(self, make, model, year):
        # 初始化汽车属性
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + "年" + self.make + "制造了" + self.model
        return long_name

    def read_odometer(self):
        # 打印一条指出汽车里程的消息
        print("这辆车现在的时速是" + str(self.odometer_reading))

    def update_odometer(self, mileage):
        #self.odometer_reading = mileage
        """将里程表读数设置为指定值
            禁止将里程表读数往回调
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("你不能把速度往回调")

    def increment_odmeter(self,miles):
        """将里程表读数增加指定量"""
        self.odometer_reading += miles
my_new_car = Car('audi','a4',2016)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()

my_new_car.update_odometer(100)
my_new_car.update_odometer(10)
my_new_car.increment_odmeter(20)
my_new_car.read_odometer()


