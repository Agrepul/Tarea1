num1=int(input("Ingrese el primer numero"))
num2=int(input("Ingrese el segundo numero"))
num3=int(input("Ingrese el tercer numero"))
suma=int( num1 + num2 +num3)
pro=int (suma / 3)
print("el promedio final es:",pro)
if pro % 2 ==0:
    mensaje=pro,"Es un numero par"
else:
    mensaje=pro,"Es un numero impar"
print(mensaje)