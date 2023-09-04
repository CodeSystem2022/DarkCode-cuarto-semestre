# Profundizando en el tipo float
a = 3.0       #--> Variable tipo float

print(f'a: {a:.2f}') #--> .2f es para indicar los numeros a mostrar despues del punto

# Constructor de tipo float -> puede recibir int y str
a = float(10) # Le pasamos un tipo entero (int)
a = float('10')
print(f'a: {a:.2f}')

# Notación exponencial (valores positivos o negativos)

#valor positivo
a = 3e5
print(f'a: {a:.2f}')

#valor negativo
a = 3e-5
print(f'a: {a:.5f}')

# Cualquier calculo que incluye un float, todo cambia a float
a = 4.0 + 5
print(a)
a = 4.8 + 5
print(type(a))
print(f'{a:.2f}')