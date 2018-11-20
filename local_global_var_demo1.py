f = 101 #global variable  and it will execute tfirst
print(f)

def fun1():
    f='string'   #global f is now redeclare as local variable
    print(f)     # run when fun1 will call

fun1()    # calling function so it will run at 2nd
print(f)    # run at 3rd
