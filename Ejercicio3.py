num1=int(input("Ingrese el primer numero"))
num2=int(input("Ingrese el segundo numero"))
num3=int(input("Ingrese el tercer numero"))
suma=int(num1+num2+num3)
print("La suma de los numeros es:",suma)
if suma %7==0:
    mensaje="El numero",suma, " es multiplo de 7"
else:
    mensaje="El numero",suma," no es multiplo de 7"
print(mensaje)
