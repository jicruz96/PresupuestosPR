#!/usr/bin/python3

from datetime import date
from requests import get
from unidecode import unidecode


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
url_template = "http://ogp.pr.gov/PresupuestoMunicipal/"
url_template += "Presupuestos%20municipales%20{}%20{}/".format(year - 1, year)
url_template += "{}"
url_template += "%20{}.pdf".format(year)

failed_downloads = []
for muni in municipios:
    # Create download url. Make sure to replace spaces with %20
    url = url_template.format(unidecode(muni))  # Remove the áéíóú's and such
    url = url.replace(" ", "%20")               # Replace spaces with "%20"

    # DOWNLOAD TIME BABY
    print("Downloading {} pdf...".format(muni))

    # Use a User-Agent header to mimic a browser request
    response = get(url, headers={'User-Agent': 'Mozilla/5.0'})

    # If the download didn't work, let the user know and append the town to
    # the failed_downloads list. We will print this at the end.
    if response.status_code != 200:
        failed_downloads.append(muni)
        print("{} failed :(".format(muni))
    # If everything went okay, save the file
    else:
        # make file name
        file_name = muni.lower().replace(" ", "_") + ".pdf"
        file_name = unidecode(file_name)  # removes the áéíóú's and such
        with open(file_name, 'wb') as file:
            file.write(response.content)
        print("Successfully downloaded")

# When finished, print list of failed downloads
print(failed_downloads)
