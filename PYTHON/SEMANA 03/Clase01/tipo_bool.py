
# Bool contiene los valores de True y Flase
# Tipos númericos -> es false para el 0(cero), true para los demás valores
print('**tipo Numericos**')
valor = 0 #False
resultado = bool(valor)
print(f'Valor: {valor}, Resultado: {resultado}')

valor = 10 #True
resultado = bool(valor)
print(f'Valor: {valor}, Resultado: {resultado}')

valor = -1 #True
resultado = bool(valor)
print(f'Valor: {valor}, Resultado: {resultado}')

valor = 0.0 #False
resultado = bool(valor)
print(f'Valor: {valor}, Resultado: {resultado}')

valor = 0.1 #True
resultado = bool(valor)
print(f'Valor: {valor}, Resultado: {resultado}')

valor = 1.1 #True
resultado = bool(valor)
print(f'Valor: {valor}, Resultado: {resultado}')

valor = -1.0 #True
resultado = bool(valor)
print(f'Valor: {valor}, Resultado: {resultado}')

valor = -0.0 #False
resultado = bool(valor)
print(f'Valor: {valor}, Resultado: {resultado}')

# Tipo String -> False ''(cadena vacia) True para los demas valores
print('**Tipo String**')

valor = '' #False
resultado = bool(valor)
print(f'Valor: {valor}, Resultado: {resultado}')

valor = 'Hola' #True
resultado = bool(valor)
print(f'Valor: {valor}, Resultado: {resultado}')

# Tipo Colecciones -> False para colecciones vacias, True para todas las demas 
print('**Tipo Colecciones**')

# Lista
valor = [] #False
resultado = bool(valor)
print(f'Valor de una lsta vacia: {valor}, Resultado: {resultado}')

valor = ['Lunes', 'Martes', 'Miercoles'] #True
resultado = bool(valor)
print(f'Valor de una lista con elementos: {valor}, Resultado: {resultado}')

valor = [1, 2, 3] #True
resultado = bool(valor)
print(f'Valor de una lista con elementos: {valor}, Resultado: {resultado}')

# Tupla
valor = () #False
resultado = bool(valor)
print(f'Valor de una tupla vacia: {valor}, Resultado: {resultado}')

valor = (1, 2, 3) #True
resultado = bool(valor)
print(f'Valor de una tupla con elementos: {valor}, Resultado: {resultado}')

# Diccionario
valor = {} #False
resultado = bool(valor)
print(f'Valor de un diccionario vacio: {valor}, Resultado: {resultado}')

valor = {'Nombre': 'Juan', 'Apellido': 'Sorato'} #True
resultado = bool(valor)
print(f'Valor de un diccionario con elementos: {valor}, Resultado: {resultado}')

# Sentencias de control con bool
if '': #False
    print('Regresa Verdadero')
else:
    print('Regresa falso')

    
if 'Hola': #True
    print('Regresa Verdadero')
else:
    print('Regresa falso')
    
# Otra forma
if bool ('Hola'): #True
    print('Regresa Verdadero')
else:
    print('Regresa falso')
    
if 0: #False
    print('Regresa Verdadero')
else:
    print('Regresa falso')
    
if 2: #True
    print('Regresa Verdadero')
else:
    print('Regresa falso')
    
# Ciclos 
variable = 3 #True
while variable:
    print('Regresa Verdadero')
    break
else:
    print('Regresa falso')
    
variable = 0 #False
while variable:
    print('Regresa Verdadero')
    break
else:
    print('Regresa falso')