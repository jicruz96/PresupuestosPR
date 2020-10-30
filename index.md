<p align="center">
  <img src="https://raw.githubusercontent.com/jicruz96/PresupuestosPR.com/gh-pages/prespuestos_pr_placeholder.png" />
 </p>

## Coming Soon!
* Data for city government salaries.
* Data for publict debt.
* English version of API
* Automatic exports to CSV, Google Sheets, Excel

## The Site

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
---
You can also receive **expenses** for a specific department by using the following route:
```
presupuestospr.com/api/<municipality>/<departamento>

# Replace <municipality> with a municipality 
# Replace <departamentos> with a department name
```


Don't know your municipalities or city departments? Use the following endpoints:
```
presupuestospr.com/api/municipios   # Returns list of ALL municipalities
presupuestospr.com/api/departamentos # Returns list of ALL departments
```


## About

### The Mission: Transparency

**The Puerto Rican public sector has a transparency problem.** Corruption in the political realm is rampant, government services are hard to navigate, and public data is hard to locate.

**Part of the solution is to change how the government interfaces with its constituents and its own data** 

**This project aims to be:**
* a tool used by journalists and activists to quickly find key data points on government spending
* an API used by developers and data scientists to build data visualizations
* a **proof of concept** to inspire local municipal governments to make their data and internal work more transparent.

### The Team

![J.I. Cruz headshot](https://media-exp1.licdn.com/dms/image/C4E03AQEk2JMYFPtrLQ/profile-displayphoto-shrink_200_200/0?e=1609372800&v=beta&t=nVmKkSJZ4lLY1bGMj803nOQB7kvoLcj9EqQ5T6-VIpg)

#### J.I. Cruz - Founder and Project Lead
* J.I. Cruz is a 23 year-old wannabe social entrepreneur from Bayamón, Puerto Rico. He is passionate about building systems that make communities stronger, healthier, and in harmony with their environment. 
