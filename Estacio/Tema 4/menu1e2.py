def func1():
    global x
    x=10
    print(f'Funcão func1 - x ={x}')

def func2():
    global x
    x=20
    print(f'Função func2 - x ={x}')
    return x

x = 0
print(f'Programa principal -x {x}')
func1()

print(f'Programa prinicipal -x {x}')
func2()

print(f'Programa prinicipal -z {x}')