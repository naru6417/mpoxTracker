import pycountry
import pandas


country = list(dict(x).get('name') for x in pycountry.countries)
iso3 = list(dict(x).get('alpha_3') for x in pycountry.countries)
month_start = ["" for x in range(len(country))]
cases = [0 for x in range(len(country))]
deaths = [0 for x in range(len(country))]
columns = ['country', 'iso3', 'month_start', 'cases', 'deaths']

df = pandas.DataFrame(list(zip(country, iso3, month_start, cases, deaths)), columns=columns)

df.to_csv('mpox_data_scaffolding.csv', encoding='utf-8', index=False)


print("complete")
