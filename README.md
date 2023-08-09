# presupuestospr.com - A Puerto Rico Municipal Budget API

This was my final project for my Full-Stack Software Engineer certification from Holberton School.

It consists of:

* Many, many hours of work scraping, cleaning, and organizing the municipal budget data for all 78 municipalities in Puerto Rico, using an assortment of python scripts and helper libraries, such as `pyPDF`.
* A Flask API to serve the cleaned data.

## The API

**The API is straightforward. Just write the name of a municipality.**
```
# Replace <municipality> with a municipality name
presupuestospr.com/api/<municipality>/
```

This request returns a JSON-formatted dictionary of the following information:
```
{
    'municipio': # municipality name,
    'gastos': # expenses,
    'ingresos': # revenue,
    'deudas': # debt
    'departamentos': # municipal departments
}
```

The values of this dictionary are explained further below:

| Key             | Key Description       | Value                                                                                                  |
|-----------------|-----------------------|--------------------------------------------------------------------------------------------------------|
| `municipio`     | Municipality name     | string |
| `gastos`        | Expenses              | `{"monto" (dollar amount): float, "departamento": string, "gasto" (expense description): string }`   |
| `ingresos`      | Revenue               | `{"monto" (dollar amount): float, "departamento": string, "ingreso" (revenue description): string }`) |
| `deudas`        | Public debt           | `{"monto" (dollar amount): float, "departamento": string, "deuda" (debt description): string }`     |
| `departamentos` | Municipal departments | Dictionary of departments: `{ {'departamento': string, 'id': int, 'palabra clave' (keyword): string}, ... }` |


You can also choose to receive only one of these keys:
```
presupuestospr.com/api/<municipality>/ingresos # Returns revenue only
presupuestospr.com/api/<municipality>/gastos # Returns expenses only
presupuestospr.com/api/<municipality>/departamentos # Returns departments only

# Note: filtering for debt unavaiable as of 10-30-2020
```


You can also receive **a department's specific expenses** by using the following route:
```
# Replace <municipality> with a municipality and <departamentos> with a department name
presupuestospr.com/api/<municipality>/<departament>
```


Don't know your municipalities or city departments? Use the following endpoints:
```
presupuestospr.com/api/municipios   # Returns list of ALL municipalities
presupuestospr.com/api/departamentos # Returns list of ALL departments
```
