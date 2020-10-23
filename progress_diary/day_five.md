# Día 5: Terminando Limpieza de Datos

18 octubre 2020
[confirms.pepper.spilling](https://what3words.com/confirms.pepper.spilling)

---

## ¿Qué es esto?

Este es mi diario de trabajo para mi _______ día trabajando en mi proyecto de
portfolio. [Oprime aquí para ver un resumen de qué se trata este proyecto](https://docs.google.com/document/d/1u1YjIWu_SO1AMHZtYyueebLgWwt5T2az9wG3lOARwNY/edit?usp=sharing).


## Prioridades de Hoy

## El "Flow" de Hoy

**17:50 - 18:45: Corrección de errores**
* Mi novia Rachel me hizo el favor de hacer un double check de todas mis tablas y encontró par de errores.
* Anticipaba esto, no hay problema. Gracias a Rachel por tu ayuda! Te amo muchísimo.
* Algunos errores interesantes:
    * El municipio de Adjuntas publicó la información de distribución de sueldos de Aguada, no la suya.
    * Dorado, Manatí, Utuado y Ponce incluyeron sus tablas dos veces.

**20:00 - 22:00: Convirtiendo CSVs a Tablas de Excel**
* No creé un script permanente para este paso porque quise trabajar directamente en la consola de python3.
* Pero, en esencia, utilicé el objecto pandas.ExcelWriter para tomar todos los CSVs de una categoría común y guardarlos bajo un solo archivo de excel.
    * Hice un archivo excel por cada municipio. Cada archivo tiene 4 worksheets:
        * Ingresos
        * Gastos
        * Deuda
        * Salarios
    * También hice un archivo "master" por cada una de esas categorías.
        * Ejemplo --> ingresos.xlsx contiene el worksheet de ingresos de cada municipio.
* Encontré muchos errores en las tablas de salarios y deudas, así que no me voy a ocupar con estos hasta que termine con lo que más me interesa: ingresos y gastos. Fortunadamente, estos salieron más o menos bien.
* Mi novia Rachel me va a dar un pequeño curso en R (este lenguaje es mejor para manejar "datasets") para limpiar estos archivos un poquito más. Todavía tengo algunas filas repetidas y también necesito convertir los hilos que dicen cosas como `"$       (123)"` a algo utilizable (ej. `-123`)
    * Utilizaremos el package `tidyverse`
    * Pichea.
* Vamos a usar el módulo `pandas` de python como hemos estado usando. Los beneficios que me daría usar R son contrarestados por el tiempo que me tomaría familiarizarme con el idioma.

## Notas & Prioridades Para Mañana

* Para mañana, tendré que seguir limpiando las tablas. Específicamente, tengo que:
    * Eliminar headers redundantes
    * Eliminar filas de montos totales, si existen.
    * Eliminar columnas innecesarias.
    * Cambiar datos que se ven así `$    \n123` a algo asá `123`
    

## Fun Facts
