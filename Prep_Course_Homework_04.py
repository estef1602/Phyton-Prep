#!/usr/bin/env python
# coding: utf-8

# ## Flujos de Control

# 1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla si es mayor o menor a cero

# In[4]:
num = 4
if int(num) > 0:
    print("el número " + str(num) + " es mayor que 0")
elif num < 0:
    print("El número "+ str(num) + " es menor que 0")
else:
    print("El número " + str(num)+ " es igual que 0")


# 2) Crear dos variables y un condicional que informe si son del mismo tipo de dato

# In[5]:
a = 20
b = 'amor'
if (type (a) == type(b)):
    print ('Las dos variables son del mismo tipo')
else :
    print('Las dos variables son de diferente tipo')

# 3) Para los valores enteros del 1 al 20, imprimir por pantalla si es par o impar

# In[7]:
for c in range(1,21):
    if c % 2 == 0:
        print(f'El numero {str(c)} es par')
    else:
        print(f'El numero {str(c)} es impar')


# 4) En un ciclo for mostrar para los valores entre 0 y 5 el resultado de elevarlo a la potencia igual a 3

# In[9]:
for d in range(0,6):
    print(f'El número {str(d)} elevado a la potencia 3 es igual a {str (d**3)}')

# 5) Crear una variable que contenga un número entero y realizar un ciclo for la misma cantidad de ciclos

# In[10]:
e = 6
for f in range(0,e):
    print('Este es el ciclo número '+ str(f))

# 6) Utilizar un ciclo while para realizar el factoreo de un número guardado en una variable, sólo si la variable contiene un número entero mayor a 0

# In[33]:
g = -2
if (type (g)== int):
    if (g > 0):
        fac=g
        while(g > 2):
            g -= 1
            fac *= g
        print('El factorial es ', fac)
    else:
        print('La variable no es mayor a cero ')
else:
    print('La variable no es un entero')

# 7) Crear un ciclo for dentro de un ciclo while

# In[38]:
h = 7
while h < 10:
    print('While número '+ str(h))
    for g in range(0,(h+1)):
        print('For número '+ str(g))
    h += 1

# 8) Crear un ciclo while dentro de un ciclo for

# In[3]:
j = 6
for i in range(0,j):
    print('for número '+ str(i))
    k = j
    while k > 0:
        print('While número '+ str(k))
        k-=1
        if j <= 0:
            break

# 9) Imprimir los números primos existentes entre 0 y 30

# In[54]:
maxi = 30
l = 0
primo = True
while(l < maxi):
    for m in range(2,l):
        if (l%m == 0):
            primo = False
    if (primo):
        print(l)
    else:
        primo=True
    l+=1

# 10) ¿Se puede mejorar el proceso del punto 9? Utilizar las sentencias break y/ó continue para tal fin

# In[55]:
maxi = 30
l = 0
primo = True
while(l < maxi):
    for m in range(2,l):
        if (l%m == 0):
            primo = False
            break
    if (primo):
        print(l)
    else:
        primo=True
    l+=1


# 11) En los puntos 9 y 10, se diseño un código que encuentra números primos y además se lo optimizó. ¿Es posible saber en qué medida se optimizó?

# In[56]:
ciclos_sin_break=0
maxi = 30
l = 0
primo = True
while(l < maxi):
    for m in range(2,l):
        ciclos_sin_break +=1
        if (l%m == 0):
            primo = False

    if (primo):
        print(l)
    else:
        primo=True
    l+=1
print('Ciclos sin break '+str(ciclos_sin_break))

# In[57]:
ciclos_con_break=0
maxi = 30
l = 0
primo = True
while(l < maxi):
    for m in range(2,l):
        ciclos_con_break +=1
        if (l%m == 0):
            primo = False
            break
    if (primo):
        print(l)
    else:
        primo=True
    l+=1
print('ciclos con break '+str(ciclos_con_break))
print('Se optimizó a un '+ str(ciclos_con_break/ciclos_sin_break) + '% de ciclos aplicando break')


# 12) Aplicando continue, armar un ciclo while que solo imprima los valores divisibles por 12, dentro del rango de números de 100 a 300

# In[62]:
n=99
while (n <= 300):
    n+=1
    if(n % 12 != 0):
        continue
    print(n,'es divisible por 12')

# 13) Utilizar la función **input()** que permite hacer ingresos por teclado, para encontrar números primos y dar la opción al usario de buscar el siguiente

# In[73]:
sigue =1
l = 1
primo = True
while(sigue == 1):
    for m in range(2,l):
        if (l%m == 0):
            primo = False
    if (primo):
        print(l)
        print('¿Quiere ver el siguiente número? 1.Si 2.No ')
        if (input() != '1'):
            print('Se finaliza la busqueda')
            break
    else:
        primo=True
    l+=1


# 14) Crear un ciclo while que encuentre dentro del rango de 100 a 300 el primer número divisible por 3 y además múltiplo de 6

# In[75]:
x=100
while(x <= 300):
    if (x % 6 == 0):
        print('El primer número entre 100 a 300 que es multiplo de 6 y divisible por 3 es: ', str(x))
        break
    x += 1


