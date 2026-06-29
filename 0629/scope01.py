# vartest_global.py
a = 1 
def vartest(): 
    global a 
    a = a+1
    return a

a = vartest() 
print(a)
