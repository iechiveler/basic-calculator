import sys

scelt = str(sys.argv[1])
var1 = int(sys.argv[2])
var2 = int(sys.argv[3])

def scelta(sce):
    if sce == '+':
        somma(var1,var2)
    elif sce == '-':
        sottrazione(var1,var2)
    elif sce == '/':
        divisione(var1,var2)
    elif sce == 'x':
        moltiplicazione(var1,var2)
    elif sce == '*':
        potenza(var1,var2)
    else:
        print('Scegli tra: +, -, /, x o *')


def somma(x,y):
    sum = x + y
    print(sum)
    return
    
def sottrazione(x,y):
    sottr = x - y
    print(sottr)
    return
    
def divisione(x,y):
    div = x / y
    print(div)
    return
    
def moltiplicazione(x,y):
    molt = x * y
    print(molt)
    return
def potenza(x,y):
    pot = x ** y
    print(pot)
    return

scelta(scelt)