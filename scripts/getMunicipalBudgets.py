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


def getMunicipalBudgets(municipalities, year):
    """ Downloads the PDF Municipal Budgets for a given year

        Return: List of downloaded file names (List[str])
    """

    # URL template
    url_template = "http://ogp.pr.gov/PresupuestoMunicipal/"
    url_template += "Presupuestos%20municipales%20{}%20{}/"
    url_template = url_template.format(year - 1, year, year)
    url_template += "{}"
    url_template += "%20{}.pdf".format(year)

    failed_downloads = []
    files = []
    for muni in municipalities:
        # Create download url. Replace spaces with %20 and remove accents
        url = url_template.format(unidecode(muni))
        url = url.replace(" ", "%20")

        # DOWNLOAD TIME BABY
        print("Downloading {} pdf...".format(muni))

        # Use a User-Agent header to mimic a browser request
        response = get(url, headers={'User-Agent': 'Mozilla/5.0'})

        # If the download didn't work, let the user know and append
        # to failed_downloads list. We will print this at the end.
        if response.status_code != 200:
            failed_downloads.append(muni)
            print("{} failed :(".format(muni))
        # If everything went okay, save the file
        else:
            # make file name:
            #   file name format is the town name:
            #       * all lower case,
            #       * spaces replaced with underscores,
            #       * unicode characters replaced with ASCII counterparts
            #       * ends with .pdf extension
            #   Example: "Río Grande" --> "rio_grande.pdf"
            fileName = muni.lower().replace(" ", "_")
            fileName += '_' + str(year) + ".pdf"
            fileName = unidecode(fileName)
            with open(fileName, 'wb') as file:
                file.write(response.content)
            print("Successfully downloaded")
            files.append(fileName)

    # When finished, print list of failed downloads
    if len(failed_downloads):
        print(len(failed_downloads), ' files failed to download')
        print('saving failed file names into failed_files.txt...')
        with open('failed_files.txt', 'w') as failFile:
            for file in failed_downloads:
                failFile.write(file + '\n')
    else:
        print("All downloads successful!")

    return files
