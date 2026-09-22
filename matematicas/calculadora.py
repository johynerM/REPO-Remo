def sumar(num1,num2):
    return num1+num2
def restar():
    num1=int((input("ingresa el numero")))
    num2=int((input("ingresa el siguiente numero")))
    print(num1 - num2)
def multiplicar(numero1,numero2):
    print(numero1 * numero2)
def potenciacion():
    base=int(input("ingrese la base"))
    exponente=int(input("ingrese el exponente"))
    Rtapotenciacicion = base**exponente
    print(Rtapotenciacicion)
def raizcuadrada(numero):
    print(numero**0.5)
print(sumar(5,2))
multiplicar(6,7)
restar()
potenciacion()
raizcuadrada(121)
