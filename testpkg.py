import sys

names = ['matplotlib','numpy','sympy','scipy','pandas']
for name in names:
    try:
        exec("import "+name)
        print('{name}',"found")
    except:
        print("{0} NOT found".format(name)) 
