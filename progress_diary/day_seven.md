# Día 7 - Creando el API

20 octubre 2020

[confirms.pepper.spilling](https://what3words.com/confirms.pepper.spilling)

---

## ¿Qué es esto?

Este es mi diario de trabajo para mi séptimo día trabajando en mi proyecto de
portfolio. [Oprime aquí para ver un resumen de qué se trata este proyecto](https://docs.google.com/document/d/1u1YjIWu_SO1AMHZtYyueebLgWwt5T2az9wG3lOARwNY/edit?usp=sharing).


## Prioridades de Hoy

* Es tiempo de construir el API!
* Voy a añadir a cada JSON una lista de los departamentos mencionados en el presupuesto

## El "Flow" de Hoy

**12:00-13:00: Montando el Flask app básico**
* Hoy es un día de trabajo para mi en Holberton (soy un tutor suplente para Holberton San Juan) así que no tengo mucho tiempo para trabajar hoy. Pero empezemos por donde hay que empezar.

**23:00-00:00: Extrayendo departamentos / Quitando caracteres especiales**
* Uno de los API urls que quiero crear devuelve la información financiera para un solo departamento de un municipio. (Y otro devolvería la información de un tipo de departamento para todos los municipios, por motivos comparativos). Me saldría bien tener una lista de departamentos conocidos para cada tabla, así que voy a crear un script para eso.

* Okay, mientras hacía ese script, me percaté que los json files se ven medios feos porque todas las letras con acentos, tildes o diacríticos han sido convertidos a un "escape sequence" de carácteres que representan el código Unicode de esas letras. Haré otro script rapidito que me quita toda esas letras y me las convierte por el carácter regular más similar.
    * El módulo python `unidecode` (pronunciado uni-DI-code) fue súper útil para este script.

* También me ocupé de crear un archivo que me muestra una lista de todos los municipios que mencionan un departamento específico.

**00:30-1:00: Encontrando y corrigiendo más errores**

* En el proceso de extraer departamentos encontré más errores.
* Algunos de estos errores tendré que procesar manualmente.
* El error más común es que a veces aparece el contenido de dos columnas bajo una misma columna, dejando así la otra columna vacía. Fortunadamente, estos errores los puedo arreglar con un script. Busco todas las células vacías, verifico si la columna previa muestra evidencia de que contiene dos cosas distintas, y si lo hay, pues reparto el contenido entre las dos columnas.
    * Aquí el script que hice.


## Trabajo Completado

## Metas No Cumplidas

## Lecciones de Hoy

## Notas & Prioridades Para Mañana

## Fun Facts
