num1 = int(input ("Ingrese el primer valor entero"))
num2= int ( input ("Ingrese ek segundo valor entero"))
if num1 > num2:
    mensaje=num1 , "Es mayor y ",num2,"Es menor"
elif num2 > num1:
    mensaje=num2 ,"Es mayor y ",num1,"Es menor"
else:
    mensaje=num1,"y",num2, "son numeros iguales"
print(mensaje)
