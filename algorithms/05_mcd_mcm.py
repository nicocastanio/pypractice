"""
Algoritmo encontrado en: 
http://www.eljavatar.com/2014/05/Como-Hallar-el-Minimo-Comun-Multiplo-en-Python.html
"""
import math


# -------------------------------------------------------------------------- #  
# Opcion 1
# utilizando algoritmo de Euclides 
# M.C.M(A, B) = (A * B) / M.C.D(A, B)
# -------------------------------------------------------------------------- #  

""" Funcion para hallar el Maximo Comun Divisor """
def mcd(num1, num2):
    a = max(num1, num2)
    b = min(num1, num2)
    while b!=0:
        mcd = b
        b = a%b
        a = mcd
    return mcd
 
""" Funcion para hallar el Minimo Comun Multiplo """
def mcm(num1, num2):
    a = max(num1, num2)
    b = min(num1, num2)
    mcm = (a / mcd(a, b)) * b
    return mcm
    
""" Funcion Principal """
# Pedimos los datos al usuario
num1 = int(raw_input("Ingrese el primer numero\n"))
num2 = int(raw_input("Ingrese el segundo numero\n"))
# Mostramos el resultado en pantalla
print("El M.C.M. entre "+str(num1)+" y "+str(num2)+" es: "+str(mcm(num1, num2)))
raw_input()



# -------------------------------------------------------------------------- #  
# Opcion 2
# -------------------------------------------------------------------------- #
# Pedimos al usuario que ingrese los números
num1 = int(raw_input("Ingrese el primer numero\n"))
num2 = int(raw_input("Ingrese el segundo numero\n"))
# Seleccionamos el menor entre num1 y num2
menor = min(num1,num2)
# Realizamos un ciclo for para iterar entre
# 1 y el menor de los dos numeros
for i in range(1,menor):
    # Comprobamos la division exacta de num1 y num2 entre todos
    # todos los valores que toma i en el ciclo
    if (num1%i==0 and num2%i==0):
        # La división puede ser exacta para varios valores de i,
        # sin embargo sólo será mcd el último de estos valores
        mcd = i
        # Calculamos el Mínimo Común Múltiplo
        mcm = (num1*num2)/mcd
# Mostramos el resultado en pantalla
print("El M.C.M. entre "+str(num1)+" y "+str(num2)+" es: "+str(mcm))
raw_input()


  
# -------------------------------------------------------------------------- # 
# Opcion 3 
# L.C.M. (Least common multiple)
# -------------------------------------------------------------------------- #

def lcm(x, y):
   """ Esta función recibe dos enteros y devuelve el Mínimo Común Múltiplo.
   utiliza fuerza bruta para hallar el resultado. 
   """
   # tomar el mayor de los dos
   if x > y:
       mayor = x
   else:
       mayor = y

   while(True):
       if((mayor % x == 0) and (mayor % y == 0)):
           lcm = mayor
           break
       mayor += 1

   return lcm

