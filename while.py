import random

a = 20
while a < 30:
    a += 4
    print(a)

# 1-100的和
i = 1
sum_ = 0
while i <= 100:
    sum_ = i + sum_
    i += 1
print(sum_)

# 猜数字
# num = random.randint(1, 100)
# print(num)
# n = True
# while n:
#     num_ = int(input('请输入数组'))
#     if num_ == num:
#         print('猜对了，结束')
#         n = False
#     else:
#         if num_ > num:
#             print('猜大了')
#         else:
#             print('猜小了')

# 打印九九乘法表
i = 1
while i < 10:
    j = 1
    while j <= i:
        if j==i:
            print(f'{i}*{j}={i * j}\t')
        else:
            print(f'{i}*{j}={i*j}\t',end='')
        j += 1
    i += 1


