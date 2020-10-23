# Día 6: Terminando Limpieza de Datos Part 2

19 octubre 2020

[confirms.pepper.spilling](https://what3words.com/confirms.pepper.spilling)

---

## ¿Qué es esto?

Este es mi diario de trabajo para mi sexto día trabajando en mi proyecto de
portfolio. [Oprime aquí para ver un resumen de qué se trata este proyecto](https://docs.google.com/document/d/1u1YjIWu_SO1AMHZtYyueebLgWwt5T2az9wG3lOARwNY/edit?usp=sharing).


## Prioridades de Hoy

* Terminar la limpieza de datos. Finalmente.
* Empezar arquitectura del API

## El "Flow" de Hoy

**10:30 - 20:00: Re-creando versiones JSONs de las tablas**

* Ayer fue bien desalentador. Mis tablas excel todavia tiene muchos errores
de data que tendré que limpiar e irónicamente la mejor manera de lidiar con estos problemas sería si lidio con las tablas como objetos JSON, no como tablas csv.
* Fortunadamente, ya tenemos todas las tablas en versión JSON dentro de mis parsing reports. Lo que me gustaría hacer ahora es crear un nuevo archivo JSON que solo tenga las tablas y no las estadísticas de calidad de la conversión de datos. Estos nuevos archivos también tendran las tablas pre-organizadas de acuerdo a su categoría. Las categoría son:
    * Gastos
    * Ingresos
    * Deuda
    * Información Salarial
        * Empleados Asalariados
        * Empleados No Asalariados
* Finalmente, estas tablas JSON serán verdaderamente la única información que necesitaré. Mientras hago las tablas, me aseguraré de quitar filas duplicadas, columnas innecesarias, y errores de conversión.
* Okay, asi que la conversión de datos no fue perfecto. Tendré que ir manualmente añadiendo y quitando ciertos errores.
    * Creé un script que encontró la mayoría de los errores en las tablas. Lo puedes ver aquí.

## Trabajo Completado

## Metas No Cumplidas

## Lecciones de Hoy

## Notas & Prioridades Para Mañana

## Fun Facts
