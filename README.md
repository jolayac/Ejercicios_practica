# Ejercicios_practica
Ejercicios de práctica Python elaborados por Sebastián Olaya

A contitnuación, se mostrarán los esultados entregados por la terminal al ejecutar el código de desarrollo de algunos ejercicios (19 en total). 


13. Ejercicio:
Escribir un programa en Python que imprima por pantalla los números del 5 al 15.000.
Conveniente usar bucles.
"""
for i in range(5, 15000):
   print (i)

![alt text](<Screenshot 2025-09-03 at 23.50.20.png>)

14. Ejercicio:
Escribir un programa en Python que imprima 200 veces la palabra “hola”. Nota: en el
código fuente que usted escriba debe figurar solamente una vez la palabra “hola”.
"""
print ("hola "*200)

![alt text](<Screenshot 2025-09-03 at 23.48.57.png>)


15. Ejercicio:
Escribir un programa en Python que imprima por pantalla los cuadrados de los 30
primeros números naturales.
"""
for i in range(1,31):
    print (i**2)

![alt text](<Screenshot 2025-09-03 at 23.47.59.png>)


16. Ejercicio:
Escribir un programa en Python que multiplique los 20 primeros número naturales
(1*2*3*4*5...).
"""
multi = 1
for i in range(21):
    if i < 20:
        multi = multi*(i+1)
    elif i == 20:
        multi = multi*(i+1)
        print("Resultado: ", multi)
        break

![alt text](<Screenshot 2025-09-03 at 23.24.18.png>)

17. Ejercicio:
Escribir un programa en Python que sume los cuadrados de los cien primeros números
naturales, mostrando el resultado en pantalla. 

numero = 0
suma = 0

while numero < 100:
    numero = numero+1
    suma = (numero**2)+suma
print(
    f"La suma de los cuadrados de los cien primeros números naturales es: {suma}")

![alt text](<Screenshot 2025-09-03 at 23.19.25.png>)


20. Ejercicio:
Escribir un programa en Java que calcule el área de un rectángulo del cual se le
proporcionará por el teclado su altura y anchura (números decimales).
"""
base = float(input("Ingrese la base del rectángulo: "))
altura = float(input("Ingrese la altura del rectángulo: "))
area = base*altura
print(f"El área del rectángulo es: {area}")

![alt text](<Screenshot 2025-09-03 at 23.43.30.png>)


21. Ejercicio:
Escribir un programa en Java que lea dos números del teclado y diga cual es el
mayor y cual el menor.
"""
num1 = float(input("Ingrese un número: "))
num2 = float(input("Ingrese el número con el que quiere comparar: "))
if num1 > num2:
    print(f"El número {num1} es mayor que {num2}")
elif num1 < num2:
    print(f"El número {num1} es menor que {num2}")
else:
    print(f"El número {num1} es igual que {num2}")

![alt text](<Screenshot 2025-09-03 at 23.45.55.png>)


Planeo continuar practicándo en los próximos días. Python es mucho más iteresante ahora con VS Code en lugar de IDLE