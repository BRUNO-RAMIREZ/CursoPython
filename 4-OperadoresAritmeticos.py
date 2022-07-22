#Operacion de suma
num1 = 15;
num2 = 5;
suma = num1 + num2;
print("La suma es",suma);

#Operacion de resta
resta = num1 - num2;
print("La resta es",resta);

#Operacion de multiplicacion
multiplicacion = num1 * num2;
print("La multiplicacion es",multiplicacion);

#Operacion de division
division = num1 / num2;
print("La division es",division);

#Operacion de division tomando solo la parte entera
division = 15 / 6;
print("La division es",division);
division = 15 // 6;
print("La division es",division);

#Operacion del modulo
modulo = num1 % num2;
print("El residuo es",modulo);

#Operacion potencia
base = 2;
exponente = 5;
potencia = base ** exponente;
print(base,"elevado a la",exponente,"es",potencia);

#Prioridad de Operadores
'''
1 ---> Parentesis ()
2 ---> Exponenciacion **
3 ---> Multiplicacion * , Division / y Modulo %
4 ---> Suma +, Resta -
'''

#Ejemplo obtener el resultado de la expresion: 2 x (5 + (15/3 - 2)) + 6
division = 15/3;
resta = division - 2;
suma = 5 + resta;
multiplicacion = 2 * suma;
sumaFinal = multiplicacion + 6;
print("El resultado es",sumaFinal);

resultado = 2 * (5 + (15/3 - 2)) + 6;
print("El resultado es",resultado);

