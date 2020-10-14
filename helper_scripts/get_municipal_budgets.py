#!/usr/bin/python3

from datetime import date
from unidecode import unidecode
from requests import get


# List of Puerto Rico municipalities
municipios = [
    "Adjuntas",
    "Aguada",
    "Aguadilla",
    "Aguas Buenas",
    "Aibonito",
    "Arecibo",
    "Arroyo",
    "Añasco",
    "Barceloneta",
    "Barranquitas",
    "Bayamón",
    "Cabo Rojo",
    "Caguas",
    "Camuy",
    "Canóvanas",
    "Carolina",
    "Cataño",
    "Cayey",
    "Ceiba",
    "Ciales",
    "Cidra",
    "Coamo",
    "Comerío",
    "Corozal",
    "Culebra",
    "Dorado",
    "Fajardo",
    "Florida",
    "Guayama",
    "Guayanilla",
    "Guaynabo",
    "Gurabo",
    "Guánica",
    "Hatillo",
    "Hormigueros",
    "Humacao",
    "Isabela",
    "Jayuya",
    "Juana Díaz",
    "Juncos",
    "Lajas",
    "Lares",
    "Las Marías",
    "Las Piedras",
    "Loiza",
    "Luquillo",
    "Manatí",
    "Maricao",
    "Maunabo",
    "Mayagüez",
    "Moca",
    "Morovis",
    "Naguabo",
    "Naranjito",
    "Orocovis",
    "Patillas",
    "Peñuelas",
    "Ponce",
    "Quebradillas",
    "Rincón",
    "Rio Grande",
    "Sabana Grande",
    "Salinas",
    "San Germán",
    "San Juan",
    "San Lorenzo",
    "San Sebastián",
    "Santa Isabel",
    "Toa Alta",
    "Toa Baja",
    "Trujillo Alto",
    "Utuado",
    "Vega Alta",
    "Vega Baja",
    "Vieques",
    "Villalba",
    "Yabucoa",
    "Yauco",
]

# Current year
year = date.today().year

# URL template
URL = "http://ogp.pr.gov/PresupuestoMunicipal/"
URL += "Presupuestos%20municipales%20{}%20{}/".format(year - 1, year)
URL += "{}"
URL += "%20{}.pdf".format(year)

failed_munis = []
for muni in municipios:
    # Create download url. Make sure to replace spaces with %20
    url = URL.format(unidecode(muni))   # Remove the áéíóú's and such
    url = url.replace(" ", "%20")       # Replace spaces with "%20"

    # make file name
    file_name = muni.lower().replace(" ", "_") + ".pdf"
    file_name = unidecode(file_name)  # removes the áéíóú's and such

    print(url, file_name)

    # DOWNLOAD and SAVE
    # Use a User-Agent header to mimic a browser request
    print("Downloading {} pdf...".format(muni))
    response = get(url, headers={'User-Agent': 'Mozilla/5.0'})
    if response.status_code != 200:
        failed_munis.append(muni)
        print("{} failed :(".format(muni))
    else:
        file_content = response.content
        with open(file_name, 'wb') as file:
            file.write(file_content)
        print("Successfully downloaded")
print(failed_munis)
