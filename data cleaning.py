import pandas

df = pandas.read_csv('Aggregated mpox case data.csv')
data_scaffolding_df = pandas.read_csv('mpox_data_scaffolding.csv')

del df['month_start']
del df['who_region']

df.rename(columns={'month_lab': 'month_start'}, inplace=True)

df_iso3_set = set(df['iso3'])
data_scaffolding_df_iso3_set = set(data_scaffolding_df['iso3'])

for iso3 in df_iso3_set:
    if iso3 in data_scaffolding_df_iso3_set:
        country_name = data_scaffolding_df.loc[(data_scaffolding_df['iso3'] == f'{iso3}'), 'country'].values[0]
        df.loc[(df['iso3'] == f'{iso3}'), ['country']] = country_name

df.to_csv('mpox_data.csv', encoding='utf-8', index=False)

print("complete")
