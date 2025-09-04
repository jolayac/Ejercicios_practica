"""
1.1.Imprimir por pantalla:

1. Ejercicio:
Escribir un programa en Python que imprima por pantalla la frase “Hola, ya se
imprimir frases”.
"""
#print("Hola, ya sé imprimir frases")
"""
2. Ejercicio:
Escribir un programa en Python que imprima por pantalla un número entero, por
ejemplo el 273, o el 597.
"""
#print(124)
"""
3. Ejercicio:
Escribir un programa en Python que imprima por pantalla un número decimal, por
ejemplo el 5.3, ó el 7.5.
"""
#print(5.5)
"""
1.2.Operaciones básicas y bucles:

4. Ejercicio:
Escribir un programa en Python que imprima por pantalla la suma de 1234 y 532.
"""
#print("1234 + 532 =", 1234+532)
"""
5. Ejercicio:
Escribir un programa en Python que imprima por pantalla la resta de 1234 y 532.
"""
#print("1234 - 532 =", 1234-532)
"""
6. Ejercicio:
Escribir un programa en Python que imprima por pantalla la multiplicación de 1234 y
532.
"""
#print("1234 * 532 =", 1234*532)
"""
7. Ejercicio:
Escribir un programa en Python que imprima por pantalla la división de 1234 entre
532.
"""
#print("1234 / 532 =", 1234/532)
"""
8. Ejercicio:
Escribir un programa en Python que imprima por pantalla los números del 1 al 3.
"""
#print(1,2,3)
"""
9. Ejercicio:
Escribir un programa en Python que imprima por pantalla los números del 1 al 9.
"""
#print(1,2,3,4,5,6,7,8,9)
"""
10. Ejercicio:
Escribir un programa en Python que imprima por pantalla los números del 1 al 10.000.
Conveniente usar bucles.
"""
#for i in range(1, 10001):
#    print(i)
"""
11. Ejercicio:
Escribir un programa en Python que imprima por pantalla los números del 5 al 10.
"""
#for i in range(5, 11):
#    print(i)
"""
12. Ejercicio:
Escribir un programa en Python que imprima por pantalla los números del 5 al 15.
"""
#for i in range(5, 16):
#    print(i)
"""
13. Ejercicio:
Escribir un programa en Python que imprima por pantalla los números del 5 al 15.000.
Conveniente usar bucles.
"""
#for i in range(5, 15000):
#   print (i)
"""
14. Ejercicio:
Escribir un programa en Python que imprima 200 veces la palabra “hola”. Nota: en el
código fuente que usted escriba debe figurar solamente una vez la palabra “hola”.
"""
#print ("hola "*200)
"""
15. Ejercicio:
Escribir un programa en Python que imprima por pantalla los cuadrados de los 30
primeros números naturales.
"""
#for i in range(1,31):
#    print (i**2)
"""
16. Ejercicio:
Escribir un programa en Python que multiplique los 20 primeros número naturales
(1*2*3*4*5...).
"""
"""
multi=1
for i in range(21):
    if i<20:
        multi=multi*(i+1)
    elif i==20:
        multi=multi*(i+1)
        print ("Resultado: ",multi)
        break
"""
"""
17. Ejercicio:
Escribir un programa en Python que sume los cuadrados de los cien primeros números
naturales, mostrando el resultado en pantalla. 
""
numero=0
suma=0

while numero<100:
    numero=numero+1
    suma=(numero**2)+suma
print(f"La suma de los cuadrados de los cien primeros números naturales es: {suma}")
"""
"""
20. Ejercicio:
Escribir un programa en Java que calcule el área de un rectángulo del cual se le
proporcionará por el teclado su altura y anchura (números decimales).
"""
"""
base=float(input("Ingrese la base del rectángulo: "))
altura=float(input("Ingrese la altura del rectángulo: "))
area=base*altura
print(f"El área del rectángulo es: {area}")
"""
"""
21. Ejercicio:
Escribir un programa en Java que lea dos números del teclado y diga cual es el
mayor y cual el menor.
"""
"""
num1=float(input("Ingrese un número: "))
num2=float(input("Ingrese el número con el que quiere comparar: "))
if num1>num2:
    print(f"El número {num1} es mayor que {num2}")
elif num1<num2:
    print(f"El número {num1} es menor que {num2}")
else:
    print(f"El número {num1} es igual que {num2}")
"""