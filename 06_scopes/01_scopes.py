username = "Om Prakash Pandey"

def func():
    # username = "JavaScript"
    print(username)

print(username)
# func()


x = 99 
# def addNum(y):
#     z = x + y
#     return z

# result = addNum(1)
# print(result)

# def changeGlobalVarFun():
#     global x
#     x = 12
    
# changeGlobalVarFun()
# print(x)



def f1():
    x = 88
    def f2():
        print(x)
    return f2
myResult = f1()
myResult()


def myPow(num):
    def actual(x):
        return x ** num
    return actual



f = myPow(2)
g = myPow(3)

print(f(3))
print(g(3))