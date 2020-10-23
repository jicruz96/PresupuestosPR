# Día 1 - Investigando APIs para Extracción de Data de los PDFs

jueves 14 octubre 2020

[confirms.pepper.spilling](https://what3words.com/confirms.pepper.spilling)

---

## ¿Qué es esto?

Este es mi diario de trabajo para mi segundo día trabajando en mi proyecto de
portfolio. [Oprime aquí para ver un resumen de qué se trata este proyecto](https://docs.google.com/document/d/1u1YjIWu_SO1AMHZtYyueebLgWwt5T2az9wG3lOARwNY/edit?usp=sharing).


## Prioridades de Hoy

* Todavía necesito esclarecer cuánto trabajo tomará extraer todas las tablas
de los PDFs. Haré un pequeño análisis de los PDFs y me pondré a leer la
documentación de algunos APIs que pienso usar:
    * ExtractTable API
    * Camelot API

## El "Flow" de Hoy

* **13:30 - 13:40:** Vamos a crear una plantilla para estos diarios rapidito
pa' no tener que volver a hacerlo desde zero
* **13:40 - 14:00:** Leyendo documentación de API -- pero me distraí por
mensajes de Slack.
* **16:45 - 17:30: Contando cantidad total de páginas que tengo**
    * Quiero un sentido de cuántas páginas totales tengo. Haré un pequeño
    script que utiliza el módulo PyPDF2 para verificar...
    * Aprendiendo mucho acerca del módulo `os` porque aparentemente hay
    mucho que desconocía, jajaja. Necesito aprender como accesar una lista de
    los PDFs en el directorio actual.
    * Yyyyyy, terminé! Y otra vez más, como ayer, me ocupé mucho más de lo que
    debía haciendo un script suplementario disque "para aprender". Y sí,
    aprendí más de par de módulos y ahora tengo un script cañón-- pero es un
    script cañón que utilizaré una vez nada más y gasté demasiado de rato
    creándolo.
    * *Tendré que crear algún tipo de penalidad por ocuparme en side-tasks*
    * Ah, y tenemos **8,653 páginas totales**
        * Mi script también me creó un archivo CSV con la cuenta de página
        de cada pdf individual
* **18:00 - 20:00:** Bueno, ahora que tengo la cantidad de páginas de cada PDF, 
usaré los más pequeños para hacer pruebas con los APIs.

    * Camelot API
        * Okay, me estoy dejando llevar por [este tutorial que encontré](https://medium.com/@marizu_makozi/extracting-tables-in-pdf-using-python-d520b6d8a66)
        * Okay, como anticipé, Camelot sólo podrá extraer las tablas que estén
        en versión de texto. Así que el Camelot API lo usaré con los PDFs que no son
    *scans* y ExtractTable API lo usaré para aquellos que sí son *scans*. Why?
    **ExtractTable cuesta dinero-- 4 chavos la página, así que mientras
    menos lo uso, mejor salgo.**
        * Voy a hacer un script que asume que todos son PDFs de texto a ver
        qué pasa. No me cuesta nada.
            * **NOOOOOOOOOOOOOO**
                * **TODAS FRACASARON**
    * Bueno, Camelot API no me servirá para nada. Tendré que usar ExtractTable
    exclusivamente.... Damn it.

    * ExtractTable API
        * Okay, veamos como funciona el API de ExtractTable entonces.
        * El API de ExtractTable es exactamente lo que necesito. Funciona de
        maravilla. **El problema es que me costaría sobre $200 utilizar el API 
        para procesar todo mi contenido.**
        * Okay, tengo un free trial para la conversión de 15 páginas. Intentémoslo
        con nuestro PDF más pequeño, el de Yauco.

## Trabajo Completado

* Ahora tenemos un mejor entendimiento de las herramientas que podré utilizar para extraer las tablas. He jugado un poco con el API de ExtractTable, así que ya me siento un poquito más capaz de usarlo.

## Metas No Cumplidas

* Debí haber hecho más hoy, pero tenía que asegurarme que entendía los APIs. Pero sí, mañana debo diversificar mis metas y áreas de trabajo.

## Lecciones de Hoy

* Es difícil trabajar en este proyecto cuando tengo trabajo en otras áreas. Me fui muy difícil entrar en un flow hoy debido a mis otras obligaciones de trabajo.

* No puedo perder demasiado tiempo escribiendo este blog. Creo que de ahora en adelante haré los bullet points menos detalladamente.

## Notas & Prioridades Para Mañana


* Mañana trabajaré exclusivamente en este portfolio. Tengo que entrar en un "Flow" real. 

* Quiero tener una arquitectura mínima viable, así que crearé un Flask
app básico que solo devuelve una sola página con un HTML simple.

* También quiero tomar tiempo para investigar Bootstrap, un servicio de
plantillas de páginas HTML que podría usarses para la página final.

## Fun Facts

None today.
