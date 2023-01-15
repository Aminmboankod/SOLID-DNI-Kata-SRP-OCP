# SOLID-DNI-Kata-SRP-OCP
# Índice

+   Introducción

+   Instrucciones del kata
    +   Solid DNI Kata - SRP y OCP
    +   Tabla de asignación

+   Manual
    +   Requisitos previos
    +   Instalación
    +   Uso

+   Documentación para DDD
    +   Cálculo del dígito de control del NIF/NIE

+   Arquitectura de la aplicación
    +   Modelo DDD
    +   Diagrama UML
    +   Capas Lógica
    +   Capa de acceso a datos

+   Pruebas
    +   Test
    +   Coverage

+   Conclusiones


# Introducción

Los ficheros que encontrarás en este repositorio son el resultado del kata "SOLID DNI KATA - SRP y OCP" propuesto en la clase de programación de Grado Superior de desarrollo Web Intensivo(2022).
El reto es crear un programa que en base a unos números de identificación fiscal compruebe si tiene la extructura correcta y lo complete con el dígito control.
El objetivo es desarrollarlo a partir de test (TDD) previo DDD y aplicar los principios SOLID en todo el código.

### Instrucciones del kata

#### SOLID DNI KATA - SRP y OCP 

![DNI](/images/dni.jpg)

Escribe un programa que dado un número de DNI obtenga la letra del NIF. La letra correspondiente a un DNI se calcula mediante el siguiente algoritmo: 

Se obtiene el resto de dividir el número de DNI entre 23. 
El número resultante indica la posición de la letra correspondiente a ese DNI en la siguiente cadena:

#### Tabla de asignación

0:T, 1:R, 2:W, 3:A, 4:G, 5:M, 6:Y, 7:F, 8:P, 9:D, 10:X, 11:B, 12:N, 13:J, 14:Z, 15:S, 16:Q, 17:V, 18:H, 19:L, 20:C, 21:K, 22:E.
	 	 	
No se utilizan las letras: I, Ñ, O, U.
La “I” y la “O” se evitan para evitar confusiones con otros caracteres, como “1”, “l” ó “0”.

Construir el programa utilizando un vector para almacenar cada una de las letras de la tabla anterior. Luego utiliza un diccionario para almacenar la tabla de asignación. Divide el código mediante una capa de lógica y una capa de acceso a datos para que los cambios en la estructura de datos utilizada (vector o diccionario) no supongan modificaciones en el código correspondiente a la lógica.

### Documentación para el Domain Drive Design:

[Ministerio del Interior](https://www.interior.gob.es/opencms/ca/servicios-al-ciudadano/tramites-y-gestiones/dni/calculo-del-digito-de-control-del-nif-nie/)

#### Cálculo del dígito de control del NIF/NIE

> El artículo 11 del Real Decreto 1553/2005, de 23 de  diciembre, establece que el Documento Nacional de Identidad recogerá el número personal del DNI y carácter de verificación correspondiente al número de Identificación Fiscal.

> Para verificar el NIF de españoles residentes mayores de edad, el algoritmo de cálculo del dígito de control es el siguiente:
> Se divide el número entre 23 y el resto se sustituye por una letra que se determina por inspección mediante la siguiente tabla:

>RESTO	0	1	2	3	4	5	6	7	8	9	10	11
>LETRA	T	R	W	A	G	M	Y	F	P	D	X	B
 

>RESTO	12	13	14	15	16	17	18	19	20	21	22
>LETRA	N	J	Z	S	Q	V	H	L	C	K	E
 

>Por ejemplo, si el número del DNI es 12345678, dividido entre 23 >da de resto 14, luego la letra sería la Z: 12345678Z.
 
>Los NIE's de extranjeros residentes en España tienen una letra (X, Y, Z), 7 números y dígito de control.
>Para el cálculo del dígito de control se sustituye:

>X → 0
>Y → 1
>Z → 2
>y se aplica el mismo algoritmo que para el NIF.

