# -*- coding: utf8 -*-
# 中文用户一定得先用第一行来声明编码，同时文件本身也要存储为UTF-8
# 单行注释：给程序员的超快速Py脚本解说
# 注释的#号后面要有空格

import os  # 导入了os.py模块


def main():  # 用def关键字定义一个函数。函数名main在此处并不是必须的。调用在这段脚本的最后部分。
    print('演示字符/字符串操作.单行字符串的声明用单/双引号都可以')
    print("This is Alice\'s greeting.")  # 行内注释至少要间隔2个空格
    print('This is Bob\'s greeting.')

    print('=' * 10 + " (字符可乘)")  # 字符可乘，等于：'=========='
    # 字符串可相加，不同类型不可相加。（如：str和int不能相加）

    print('当前工作目录为' + os.getcwd())  # get current working directory

    print('演示foo函式调用， 声明在后述代码')
    foo(0, 50)  # 函式调用， 声明在后述代码

    counter = 0  # 变量要先实例化，才可以进一步计算
    counter += 1
    counter = 'this is a string'  # 变量类型可变，即 动态语言

    food = ['apple', 'pear', 'banana', 'blueberry'] # list类型对象，其实可以包含不同类型的数据，甚至可以包含其它列表对象
    print('list对象可以直接打印：')
    print(food)
    for i in food:
        print('我就爱吃整只' + i)

    str_test = 'abc'
    for i in range(len(str_test)):  # range()为内置函数，返回类似[0,1,2,3,4,5,6,7,8,9]的数字列表
        print(str_test[i])  # 字符串相当于数组
    print("count to 10:")
    for i in range(10):  # range(start, stop[, step]) start 默认为0，step默认为1
        print('Now the counter is ' + str(i))  # str类型和int类型不能直接相加
    for i in range(10-1, -1, -1):
        print('Now the counter is_ ' + str(i))  # str类型和int类型不能直接相加
    for i in range(0):
        print('Now the counter is__ ' + str(i))  # str类型和int类型不能直接相加


    print('演示实例化类')
    people = People('William', 10, 30)
    people.speak()

    print('演示python中变量的传递是通过传递标记传递的。')
    pair1 = [0, 2]
    pair2 = pair1  # 此处实际上是将pair2的标记指向pair1，而非值的拷贝。此时两个变量指向相同。(相当于把引用传递给pair2.）
    (pair2[0], pair2[1]) = (pair2[1], pair2[0])  # python中没有swap函数，因为没有必要交换两个数的值.实际上直接交换两个变量的标记即可。
    print(pair1)
    print(pair2)  # 因为传递给pari2的是pair1的标记，所以实际上pair1现在和pair2是同一个变量。
    # python 中，数据在内存中的位置不变，赋值只是改变了标记。（变量名与数据的指向关系）
    # 更详细地演示与C的不同：
    a = 3
    b = a  # 此处把b也指向3
    a = 5  # 此处把a指向5，但b仍然指向3
    # 此时a= 5, b = 3. 与C结果相同，但实现机制完全不同
    a = 8
    b = 9
    tmp = a  # 此处把tmp指向8
    a = b  # 此处把a指向9
    b = tmp  # 此处把b指向8
    # 和C一样实现交换的语句，但内部实现机制完全不同
    # 交换a 和 b 的标记可以简化为：
    (a, b) = (b, a)  # 相当于C中的swap函数，但不是交换值，而是交换标记指向


def foo(para1, para2): # 定义函数时要有冒号
    res = para1 + para2
    print('%s 加 %s 等于 %s' % (para1, para2, res))  # 格式化输出，类似C的格式
    if res < 50:  # if/for 等语句块也要加冒号哦！！
        print('sum < 50')
    elif (res>=50) and ((para1 == 0) or (para2 == 51)):  # elif也不要忘了冒号！！
        print("演示：逻辑运算符不用&& || 直接用 and or")
    else:
        print('emm...')


# 类定义
class People:
    # 定义基本属性
    name = 'none'
    age = 0
    # 定义私有属性,私有属性在类外部无法直接进行访问(可用于函数或变量)
    __weight = 0  # 伪私有，实际名称为_People__weight，用此名称可外部访问

    # 定义构造方法
    def __init__(self, n, a, w):  # 所有method第一个变量必须是self，self表示实例本身，而不是类本身。
        self.name = n
        self.age = a
        self.__weight = w

    def speak(self):
        print("%s 说: 我 %d 岁。" % (self.name, self.age))



''' 一般在脚本最后部分调用主函数main；
 当且仅当我们直接运行当前脚本时，__name__才为__main__；
 这样，当脚本被当作模块improt时，__name__ != '__main__',main()函数不会被调用运行；
 因此，此处一般用于安置测试代码 '''
if __name__ == '__main__':
    main()
    """ 多行注释可以使用3个单引号或3个双引号
并且多行注释只要开始的三个引号缩进正确，后面的内容不遵守缩进规则也可以 """
