def test_return():
    return 1,2,3
x,y,z = test_return()
print(x,y,z)

def test_return_1():
    return {
        1,2,3
    }
x,y,z = test_return_1()

print(x,y,z)