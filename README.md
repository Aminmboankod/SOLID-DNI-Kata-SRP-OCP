# SOLID-DNI-Kata-SRP-OCP

# Introducción
-----
Los ficheros que encontrarás en este repositorio son el resultado del kata "SOLID DNI KATA - SRP y OCP" propuesto en la clase de programación de Grado Superior de desarrollo Web Intensivo(2022).
El reto es crear un programa que en base a unos números compruebe si tiene la extructura de un número de DNI y lo complete con la letra.
El objetivo es desarrollarlo a partir de test (TDD) y aplicar los principios SOLID.

### Estas son las instrucciones formales:

#### SOLID DNI KATA - SRP y OCP 

Escribe un programa que dado un número de DNI obtenga la letra del NIF. La letra correspondiente a un DNI se calcula mediante el siguiente algoritmo: 
Se obtiene el resto de dividir el número de DNI entre 23. 
El número resultante indica la posición de la letra correspondiente a ese DNI en la siguiente cadena:

#### Tabla de asignación

0:T, 1:R, 2:W, 3:A, 4:G, 5:M, 6:Y, 7:F, 8:P, 9:D, 10:X, 11:B, 12:N, 13:J, 14:Z, 15:S, 16:Q, 17:V, 18:H, 19:L, 20:C, 21:K, 22:E.
	 	 	
No se utilizan las letras: I, Ñ, O, U.
La “I” y la “O” se evitan para evitar confusiones con otros caracteres, como “1”, “l” ó “0”.

Construir el programa utilizando un vector para almacenar cada una de las letras de la tabla anterior. Luego utiliza un diccionario para almacenar la tabla de asignación. Divide el código mediante una capa de lógica y una capa de acceso a datos para que los cambios en la estructura de datos utilizada (vector o diccionario) no supongan modificaciones en el código correspondiente a la lógica.

