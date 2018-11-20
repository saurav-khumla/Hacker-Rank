f=101
print(f)
def fun1():
    global f
    print(f)    #global variable data work when function is called
    f = 'string'

fun1()   #it call the function
print(f)   # it give updated string data.