#  定义一个A类
class A:
    def __init__(self):
        # 实例的初始化，每次对类实例化对象的时候，先自动执行这个方法
        self.a = "hello world"

    def printHello(self):
        # 这是A类里面的方法
        print("hello")

# 类的实例化
# a = A()
# # 执行a对象里面的printHello()方法
# a.printHello()



f = open("trains.txt","r")
# 获取一行数据
row = f.readline()
f.close()
print("row:",row)
row1 = row.replace("\n",'')
print("row1:",row1)
row2 = row1.split("\t")
print("row2:",row2)
