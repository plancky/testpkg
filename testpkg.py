import sys

names = ['matplotlib','numpy','sympy','scipy','pandas']
for name in names:
    try:
        exec("import "+name)
        exec(f"print('{name} '+{name}.__version__)")
    except:
        print(f"{name} NOT found") 
