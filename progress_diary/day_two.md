# Día - Tema

Fecha aquí

[confirms.pepper.spilling](https://what3words.com/confirms.pepper.spilling)

---

## ¿Qué es esto?

Este es mi diario de trabajo para mi _______ día trabajando en mi proyecto de
portfolio. [Oprime aquí para ver un resumen de qué se trata este proyecto](https://docs.google.com/document/d/1u1YjIWu_SO1AMHZtYyueebLgWwt5T2az9wG3lOARwNY/edit?usp=sharing).


## Prioridades de Hoy


* Envíé un email anoche al dueño de ExtractTable y me dijo que está dispuesto a darme un descuento para su API. Quiero contestartle rápidamente, así que la primera prioridad de hoy será contar la cantidad de páginas totales que tienen tablas. No hay manera de automatizar ese proceso; tendré que hacerlo manualmente.

* Quiero tener una arquitectura mínima viable, así que hoy crearé un Flask
app básico que solo devuelve una sola página con un HTML simple.

* También quiero tomar tiempo para investigar Bootstrap, un servicio de
plantillas de páginas HTML que podría usarses para la página final.

## El "Flow" de Hoy


**12:00 - 12:30: Practicando como cambiar files JSON a files csv**
* El ExtractTable API me devueleve la data como un json file. Ellos tienen un módulo de Python que se encarga de cambiar todo a files csv, o incluso, de excel, inmediatamente por mí, pero lo encontré muy tedioso para usar. Así que no voy a usar ese módulo. Recibiré la información en formato JSON y más luego lo cambio a CSV.

**12:30 - 14:30: Contando páginas con tablas**
* No hay de otra, a contar manualmente. Nos vemos en par de horas...
* Okay, esto está overwhelming. Cada municipio tiene un formato distinto para presentar el presupuesto. Sería imposible poder hacer sentido de todo esto de una manera sistemática, en especial para mi deadline para este proyecto.
* Fortunadamente, cada presupuesto tiene una parte estandarizada. Todos tienen unas tablas de ingresos y egresos, todas con el mismo formato. Parece que todas esas tablas vienen de fuentes del gobierno estatal. Me enfocaré en extraer estas tablas solamente.
* La tabla de Juana Díaz no se pueden leer. Los carácteres están corrompidos:
    * Insert foto here
    * No sé que voy a hacer con esto. Lidio con esto después.
* Okay, **ya tengo las páginas que tienen tablas**

**14:30 -16:30 : Separando las páginas con tablas de las demás**
* Ahora mismo tengo un archivo TSV (tab-separated-values) donde cada línea tiene el nombre del pdf y el rango de las páginas con tablas, algo así:
    * wakanda.pdf    1-5, 9, 10-13
* Crearé un python script que cree un nuevo pdf por cada municipio, solamente con ese rango de páginas.
* Okay, creé un script que toma el rango de páginas y lo convierte a una lista de números. Esto me era necesario para crear el script de creación de PDFs.
    * Puedes ver ese script en el folder `helper_files` o [oprime aquí](https://github.com/jicruz96/portfolio_project/tree/main/helper_scripts/get_number_ranges.py)
    * Ahora lo que tengo es un JSON file con este formato:
        * `{"wakanda.pdf" : [1, 2, 3, 4, 5, 9, 10, 11, 12, 13]}
        * Subiré este file a `helper_files`
* 
* Vamos bien, pero tiempo pa' un break (14:50)
* Seguimos... (15:10)
* Super! Terminamos. Ahora tengo un bonche de PDFs solamente con las tablas de ingresos y egresos que mencioné orita.
    * El script que utilicé está en `helper_files` o [aquí](https://github.com/jicruz96/portfolio_project/tree/main/helper_scripts/make_new_pdfs.py)
* Ahora, lo que tengo es 2205 páginas totales que tendré que procesar.

# **OH MY GOD CAMELOT WORKS!!** 
* mi gente mi gente mi genteeee!!!! Qué update! Ok. El API gratis que intenté usar ayer no me funcionó para un solo pdf. Pero, esta vez, hice un arreglito al script y aprentemente sí me funciona para la mayoría de las tablas! Qué alegría. Ahora no tengo que gastar cientos de dólares en ExtractTable. Ok. Ahora qué hacemos?

**16:30 - 21:00 : From PDFs to Spreadsheets**
* Ahora que sé que Camelot funciona, voy a tomar el bonche de PDFs que creé hoy y extraer las tablas y convertir toda la data a un tabla de Excel. Qué emocionante! Llevo par de días anticipando esto.
* Tendré que crear un script pa esto. Pa'lla vamos.
* Bueno, ese script me tomó un ratito. Tuve que asegurarme que estuviese perfecto de primera. Convertir las tablas a archivos csv era lo fácil. Lo difícil era asegurarme que estuviese guardando todos esas tablas de una manera organizada.
    * En adición a los archivos csv, el script también crea un "report" para cada pdf sobre cuán preciso fue la conversión de la tabla. Esto es esencial para la corrección de errores, porque de seguro habrán pasado algunos. Estos parsing reports son diccionarios JSON con el siguiente formato:
    ```
    {
        "municipality": "wakanda",
        "pages": {
            "1": [
                {
                    "table": [table in json format],
                    "accuracy": 100,
                    "whitespace": 15.25,
                    "order": 1
                }
            ]
        }
        "expected_number_of_tables": 1,
        "number_of_tables": 1
    }
    ```
    

## Trabajo Completado

* He extraído toda la data esencial que necesito.

## Metas No Cumplidas
* Todavía no he montado mi arquitectura mínima viable ni he investigado Bootstrap.

## Notas & Prioridades Para Mañana

* Mañana es un día de trabajo, no estaré trabajando.
