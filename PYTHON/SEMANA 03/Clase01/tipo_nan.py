import math
from decimal import Decimal
# NaN (Not a Number) 
a = float('NaN')
print(f'a: {a}') 
print(type(a))

# -- Módulo math --   *-> No es sensible a Mayusculas y minusculas (en consola salen en minusculas)

# Preguntamos si a es tipo nan --> True
a = float('nan')
print(f'Es de tipo NaN(Not a Number)?: {math.isnan(a)}')
#Preguntamos si a es tipo nan --> False
a = float('8.25')
print(f'Es de tipo NaN(Not a Number)?: {math.isnan(a)}')

# --Módulo Decimal--   *-> No es sensible a Mayusculas y minusculas (en consola salen en minusculas)
a = Decimal('NaN') 
print(f'Es de tipo NaN(Not a Number)?: {math.isnan(a)}')


