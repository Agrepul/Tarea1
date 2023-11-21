num1=int(input("Ingrese el primer numero"))
num2=int(input("Ingrese el segundo numero"))
num3=int(input("Ingrese el tercer numero"))
if num1 > num2 :
    mensaje=num1 , "Es mayor"
elif num2 > num3:
        mensaje= num2,"Es mayor"
elif num3 > num2:
        mensaje=num3,"Es mayor"
else:
    mensaje="Todos los numeros son iguales"
print(mensaje)