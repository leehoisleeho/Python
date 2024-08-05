
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












