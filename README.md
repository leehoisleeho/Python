
<p align="center">
  <img src="https://i.pinimg.com/564x/ed/66/63/ed666327dd3ce274d94f2b3547155891.jpg" width="200" style="display: block; margin: 0 auto;">
</p>

## Python的学习笔记

> 每天学习一点新知识

### bool类型 
True本质上是一个数字记作1，False记作0 所以归到数字类型
除了可以定义布尔类型，还可以通过**比较运算符**来得到布尔类型

### 判断语句
#### if eles 语句中
1. if和其代码快，条件满足时就执行
2. else是搭配if使用，当if条件不满足时，就执行else里面的代码。 
3. elif 可以多条件判断，else做兜底。else不写的话，相当于3个独立的if语句

#### 判断语句嵌套
1. 关键在于空格缩进，python是根据缩进来判断层级关系。

### 循环语句
#### while
语法格式
```python
i = 100
while i < 100:
    print(i)
    i += 10
```
- 条件需要提供布尔类型 True继续 False停止
- 空格缩进
- 规划好循环终止的条件，不然就会无限循环下去
- 写法，现确定好开始的条件，和结局条件 ，再开始写要做的事。、

#### print的一些用法
- print('hello',end='') 不换行
- print('hello\tworld') 不换行

### for

是轮循机制，遍历循环♻️
语法格式

```python
str = 'hello world'
for item in str:
    print(f'item+ item')
```
**continue** 中断本次循环，进入下次循环

**break** 直接跳出循环体

### range

创建一组可以被遍历的序列

语法格式
```python
# 从0-7
list = range(8)
for item in list:
    print(item)

# 从1-7
list = range(1,8)
for item in list:
    print(item)
    
# 从1-7 步长是2
list = range(1,8,2)
for item in list:
    print(item)
```
### 函数
组织好的，可以重复使用的 ，代码片段
语法格式
```python
def fn():
    print('我是函数')

fn()
```
函数如果不return，依然有返回值，返回值是None

#### globe关键字
```python
num = 5 
def fun():
    global num 
    num = 500
```
函数内可以修改全局的变量。

### 数据容器 
批量存储和批量使用数据。

一种可以容纳多份数据的数据类型，容纳的每一份数据，称之为1个元素，每一个元素，可以是任意的数据类型
根据特点的不同，分别是：列表，元祖，字符串，集合，字典

### 列表
#### 定义
```python
# 定义1
list = ['zhangsan','lisi','wangwu']
name = list[0]
```
#### 下标索引
-1 , -2 ,依次提取最后一个和倒数第二个。

#### 常用操作
查看list.py

### 元祖 tuple
和列表差不多，元祖不可以被修改 。 可以理解成只读的列表

### 数据容器(序列)切片
序列就是内容连续，有序，可使用下标索引的一类数据容器。
切片就是从序列里面取出一部分序列。
```python
list = [1,2,3,4,5,6,7]
# 开始:结束:步长
# 步长默认为1 步长-1 是最后一个开始取
my_list = list[0:3]
print(my_list)

my_list = list[::2]
print(my_list)
```
### 集合set
**不支持重复元素**

**顺利会打乱** 所有不支持下标索引

### 字典dict
键值对 ```key:value``` 

### 数据容器通用方法
都可以用for循环进行遍历

len/max/min
容器长度/最大元素/最小元素

容器转换

str(容器)/list(容器)/tuple(容器)/set(容器)/

排序
```python
# sorted(容器,{})
# 排序完都变成列表
mylist = [1,2,3,6,1,23,4]
print(sorted(mylist,reverse=True))
```
### 函数扩展
详见fun.py





 





















