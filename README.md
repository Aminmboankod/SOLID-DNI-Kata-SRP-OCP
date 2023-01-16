# SOLID-DNI-Kata-SRP-OCP
# Índice

+   [Introducción](#introducción)

+   [Instrucciones del kata](#instrucciones-del-kata)
    +   [Solid DNI Kata - SRP y OCP](#solid-dni-kata---srp-y-ocp)
    +   [Tabla de asignación](#tabla-de-asignación)

+   [Manual](#manual)
    +   [Requisitos previos](#requisitos-previos)
    +   [Instalación](#instalación)
    +   [Uso](#uso)

+   [Documentación para DDD](#documentación-para-el-domain-drive-design)
    +   [Cálculo del dígito de control del NIF/NIE](#cálculo-del-dígito-de-control-del-nifnie)

+   [Arquitectura de la aplicación](#arquitectura-de-la-aplicación)
    +   [Modelo DDD](#modelo-ddd)
    +   [Diagrama UML](#diagrama-uml)
    +   [Capa Lógica](#capa-lógica)
    +   [Capa de acceso a datos](#capa-de-acceso-a-datos)

+   Pruebas
    +   Test
    +   Coverage

+   Conclusiones


# Introducción

Los ficheros que encontrarás en este repositorio son el resultado del kata "SOLID DNI KATA - SRP y OCP" propuesto en la clase de programación de Grado Superior de desarrollo Web Intensivo(2022).
El reto es crear un programa que en base a unos números de identificación fiscal compruebe si tiene la extructura correcta y lo complete con el dígito control.
El objetivo es desarrollarlo a partir de test (TDD) previo DDD y aplicar los principios SOLID en todo el código.

# Instrucciones del kata

### SOLID DNI KATA - SRP y OCP 

![DNI](/docs/images/dni.jpg)

Escribe un programa que dado un número de DNI obtenga la letra del NIF. La letra correspondiente a un DNI se calcula mediante el siguiente algoritmo: 

Se obtiene el resto de dividir el número de DNI entre 23. 
El número resultante indica la posición de la letra correspondiente a ese DNI en la siguiente cadena:

## Tabla de asignación
---

| RESTO | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| LETRA | T | R | W | A | G | M | Y | F | P | D | X | B | N |J | Z | S | Q | V | H | L | C | K | E |
	 	 	
No se utilizan las letras: I, Ñ, O, U.
La “I” y la “O” se evitan para evitar confusiones con otros caracteres, como “1”, “l” ó “0”.

Construir el programa utilizando un vector para almacenar cada una de las letras de la tabla anterior. Luego utiliza un diccionario para almacenar la tabla de asignación. Divide el código mediante una capa de lógica y una capa de acceso a datos para que los cambios en la estructura de datos utilizada (vector o diccionario) no supongan modificaciones en el código correspondiente a la lógica.

## Documentación para el Domain Drive Design:
----

[Ministerio del Interior](https://www.interior.gob.es/opencms/ca/servicios-al-ciudadano/tramites-y-gestiones/dni/calculo-del-digito-de-control-del-nif-nie/)

#### Cálculo del dígito de control del NIF/NIE

'''El artículo 11 del Real Decreto 1553/2005, de 23 de  diciembre, establece que el Documento Nacional de Identidad recogerá el número personal del DNI y carácter de verificación correspondiente al número de Identificación Fiscal. Para verificar el NIF de españoles residentes mayores de edad, el algoritmo de cálculo del dígito de control es el siguiente: 

Se divide el número entre 23 y el resto se sustituye por una letra que se determina por inspección mediante la siguiente tabla:


| RESTO | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| LETRA | T | R | W | A | G | M | Y | F | P | D | X | B | N |J | Z | S | Q | V | H | L | C | K | E |

 
Por ejemplo, si el número del DNI es 12345678, dividido entre 23 da de resto 14, luego la letra sería la Z: 12345678Z.
 
Los NIE's de extranjeros residentes en España tienen una letra (X, Y, Z), 7 números y dígito de control. Para el cálculo del dígito de control se sustituye
(y se aplica el mismo algoritmo que para el NIF ):

X → 0

Y → 1

Z → 2


# Manual

## Requisitos previos
| Paquete | Versión |
|:----:|:----:|
|attrs | 22.2.0
| exceptiongroup | 1.1.0 
| iniconfig | 1.1.1 |
| packaging | 22.0 | 
| pluggy | 1.0.0 |
| pytest | 7.2.0 |
| tomli | 2.0.1

## Instalación

Se recomienda utilizar en 'virtualenv' para instalar todas las dependencias utilizadas por el programa. En [Windows](https://docs.python.org/es/3.8/library/venv.html) lo puedes instalar siguiendo su guía. En **Linux** ejecuta la siguiente instrucción. 
```
$ sudo apt-get install python3-venv
```
Crea el directorio donde vas a clonar el repositorio  y clonalo usando el siguiente comando:
```
$ mkdir ./CalculadoraDNI
$ cd CalculadoraDNI
$ git clone https://github.com/Aminmboankod/SOLID-DNI-Kata-SRP-OCP.git
```
Ejecuta el archivo de configuración:
```
$ ./setup.sh
```
## Uso



## Arquitectura de la aplicación
---
![Arquitectura aplicacion](/docs/images/ArquitecturaAPP.drawio.png)
### Diseño de componentes:
![Diseño de componentes](/docs/images/Dise%C3%B1oComponentes.drawio.png)

## Modelo DDD
---
![Modelo DDD](/docs/images/DDD.drawio.png)
Tenemos un **DNI** que necesita de una tabla de asignación para establecer correctamente un **digito control** para asociarlo al **número de identificación fiscal (NIF)**. 

El **DNI** va a contener el **NIF**, el **Digito control** y otros datos personales del propietario.
Ejemplo: 45301872Z
| NIF | D. Control |
|----|----|
45301872 | Z

## Diagrama UML
---
![Diagrama UML](/docs/images/DNI_UML.drawio.png)

## Capa Lógica
---

+ logic/
    - calculadoraDNI.py

## Capa de acceso a datos
---
+ accesoDatos/
    - Dni.py

## Pruebas
---
## Test
---
## Coverage
---
## Conclusiones
---