print('欢迎来到黑马儿童游乐场')
age = int(input('请输入你的年龄'))
if age>=18:
    print('你已经成年，需要买票10元')
else:
    print('你未满18岁，可以免费游玩')


##
height = int(input('请输入你的身高'))
vip = int(input('请输入你的vip等级'))
if height<120:
    print('可以免费')
elif vip >= 3:
    print('可以免费玩')
else:
    print('买票，10元')