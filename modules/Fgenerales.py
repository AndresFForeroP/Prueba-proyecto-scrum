import os
import sys

def limpiar_p():
    if sys.platform == 'linux' or sys.platform == 'darwin':
        os.system('clear')
    else:
        os.system('cls')
def pausar_p():
    if sys.platform == 'linux' or sys.platform == 'darwin':
        x = input('Presione enter para continuar ')
    else:
        os.system('pause')
def validartipo(tipo,msg):
    match tipo:
        case 1:
            try:
                x = int(input(msg))
            except Exception:
                print('El valor ingresado no es entero')
                pausar_p()
                return validartipo(tipo,msg)
            else:
                return x
        case 2:
            try:
                x = float(input(msg))
            except Exception:
                print('El valor ingresado no es float')
                pausar_p()
                return validartipo(tipo,msg)
            else:
                return x

def sabertipo(variable):
    try:
        if variable.type():
            return 'alfabetico'
        elif variable.isalnum():
            return 'alfanumerico'
    except Exception:
        return 'entero'