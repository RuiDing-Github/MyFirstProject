'''
-1、什么是元组
-2、元组的创建方式
-3、元组的遍历
-4、什么是集合
-5、集合的创建
-6、集合的增、删、改、查操作
- 7、集合生成式
'''

'''
- 元组
- Python内置的数据结构之一，是一个不可变序列

- 不可变序列与可变序列
- 不变可变序:字符串、元组    不变可变序列：没有增、删，改的操作
- 可变序列:列表、字典       可变序列：可以对序列执行增、删、改操作，对象地址不发生更改
'''
s='hello'
print(id(s))
s=s+'world'
print(id(s))
'''
1892187039920
1892195598576  字符串改变，其实是赋值给了一个新的变量，地址已经改变了'''

'''
元组的创建方式 
1.直接小括号
2. 使用内置函数tuple() 
3. 只包含一个元组的元素需要使用逗号和小括号
'''
t1=('hello','world',20)
print(t1,type(t1) )
t0='hello','world',20
print(t0,type(t0) )

t2=tuple( ('hello','world',20) )
print(t2,type(t2) )

t3=('hello',)
print(t3)
t3='hello',   #这样也可也
print(t3)

'''
空元组   lst=[] lst=list() d={}  d=dict()  t=() t=tuple()'''

'''
为什么要将元组设计成不可变序列
-在多任务环境下，同时操作对象时不需要加锁
- 因此，在程序中尽量使用不可变序列
- 注意事项：元组中存储的是对象的引用
a)如果元组中对象本身不可对象，则不能再引用其它对象   int  str
b)如果元组中的对象是可变对象，则可变对象的引用不允许 改变，但数据可以改变  list 和 diction
'''
t = (10,[20,30],9)

print(t[0],type(t[0])),id(t[0])
print(t[1],type(t[1])),id(t[1])
print(t[2],type(t[2])),id(t[2])
'''尝试将 list 类型 [20,30] 修改成100'''
# t[1]=100 #报错，因为元组tuple是不允许修改元素
'''但由于list是可变序列，因此可修改list里的内容  增删改 ，但列表的地址不变'''

t[1].append(100)
print(t)

'''
元组是可迭代对象，所以可以使用for...in进行遍历
'''

'''
- 集合
- Python语言提供的内置数据结构
- 与列表、字典一样都属于可变类型的序列
- 集合是没有value的字典
'''
'''
1. 直接{} 
2. set()
集合中的元素不允许重复
集合中的元素 可以为列表 ，可以为元组， 可以为字符串 也可以为集合
'''
s={'hello','world',78,78}
print(s)
s=set(range(6))
s=set([1,2,2,3,4,5])
print(s)  #{1, 2, 3, 4, 5}

set() #空集合，不用s={ } ,因为s={}，是空字典，空集合要用s=set{}

'''
集合为可变序列，存在增删修改的操作

- 集合元素的判断操作
- ind 或 not in
- 集合元素的新增操作
- 调用add()方法, 一次添中一个元素
- 调用update()方法至少添中一个元素
- 集合元素的删除操作
- 调用remove()方法, 一次删除一个指定元素，如果指定的元素不存在抛出 KeyError
- 调用discard()方法，一次删除一个指定元素  如果指定的元素不存在抛出 也不会报错。
- 调用pop()方法, 一次只删除一个任意元素  不能添加参数，任意参数 
- 调用clear()方法, 清空集合
'''

'''
- 两个集合是否相等
- 可以使用运算符==或!=进行判断   (不管顺序，只管里面的元素）

-一个集合是否是另一个集合的子集
- 可以调用方法issubset进行判断  s1.issubset(s2)
- B是A的子集

-一个集合是否是另一个集合的超集
- 可以调用方法issuperset进行判断   s1.issuperse(s2)
- A是B的超集

-两个集合是否没有交集 可以调用方法isdisjoint进行判断  s1.isdisjoint(s2)
'''


'''
集合的操作'''
s1 = {10, 20, 30}
s2 = {20, 30, 40, 50}
'''交集'''
print(s1.intersection(s2))
print(s1 & s2)  #intersection（） 等价于 &， 即交集操作
'''并集'''
print(s1.union(s2))
print(s1 | s2)   #union() 等价于 |
'''差集'''
print(s1.difference(s2))
print(s1 - s2)  #difference()= -
'''对称茶几'''
print(s1.symmetric_difference(s2))
print(s1 ^ s2)

'''集合生成式 ，不可逆序列没有生成式'''
s={i*i  for i in range(6)}
'''列表生成式'''
lst = [ i*i for i in range(6)]
'''字典生存式'''