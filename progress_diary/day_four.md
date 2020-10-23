# Día 4 - Limpiando Datos

17 octubre 2020

[confirms.pepper.spilling](https://what3words.com/confirms.pepper.spilling)

---

## ¿Qué es esto?

Este es mi diario de trabajo para mi cuarto día trabajando en mi proyecto de
portfolio. [Oprime aquí para ver un resumen de qué se trata este proyecto](https://docs.google.com/document/d/1u1YjIWu_SO1AMHZtYyueebLgWwt5T2az9wG3lOARwNY/edit?usp=sharing).


## El "Flow" de Hoy

**12:20 - 12:40: Juntar parsing reports**
* Mi script de ayer creó un parsing report por cada pdf, pero para poder analizarlos me sirve mucho mejor tener toda esa data en un solo archivo. Creemos un script que lo haga.
    * No usé un método super eficiente, pero eso no importa. El punto es terminar la tarea.
    * El script que usé está [aquí](https://google.com/)
* Super, ya. El formato final del parsing report full se ve así:
```
{ "municipio" : {parsing report original}, "municipio" : {parsing report original}}
```
etc, etc...

**12:40 - 1:00: Analizando los pdfs un poco más**

* Tengo algunos pdfs donde, por error humano, incluí páginas de más que no quise. Déjame hacer una lista de archivos que potencialmente tengan este error.
* Pues, ahora tengo todas estas tablas en csv. Ahora tengo que compilarlas de una manera organizada.
* Analizando los PDFs, hay tres tipos de tablas:
    * Gastos
    * Ingresos
    * Información de Sueldos
* Podemos crear un solo documento excel por cada municipio.
    * Cada documento excel tendrá tres spreadsheets: gastos, ingresos, información de sueldos
* Para esto tendremos que juntar todas las tablas de la misma categoría bajo una sola tabla.
* Después tendré que averiguar cómo hacer "spreadsheets" distintos bajo un solo archivo de excel.

**13:00 - 13:20: Editar el parsing report final**

* Mi parsing report final es tan grande que mi computadora no puede formatearlo bien. Wow.
* Cada parsing report tiene una copia de su tabla correspondiente en versión JSON. Vamos a quitárselo.
* Cool.

**21:00 - 00:00: Juntando tablas**

* Creé un script para crear mis tablas finales. Ya estamos a la vuelta de la esquina de terminar con la limpieza de datos.
