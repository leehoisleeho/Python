# 捕获异常
# try:
#     with open('test1.txt', 'r', encoding='UTF-8') as f:
#         print(f)
# except:
#     open('test1.txt', 'w')

# 捕获指定异常
# try:
#     1/0
# except NameError as e:
#     print(e)

# 捕获多个异常
# try:
#     1/0
# except(NameError,ZeroDivisionError) as e:
#     print(e)

# 捕获所有异常
# try:
#     1/0
# except Exception as e:
#     print(f'出现异常了 {e}')


#
# try:
#     print('1')
# except Exception as e:
#     print(f'出现异常了 {e}')
# else:
#     print('没有异常')


# try:
#     1/0
# except Exception as e:
#     print(f'出现异常了 {e}')
# finally:
#     print('有异常，我也要执行')

f = None
try:
    f = open('test1.txt', 'r', encoding='UTF-8')
    print(f.read())
except Exception as e:
    print('存在异常:', e)
finally:
    if f:
        f.close()