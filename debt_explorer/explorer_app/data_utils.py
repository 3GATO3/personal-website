import pandas as pd

def reshape_debt_data(file_path):
  df = pd.read_csv(file_path, header=0)
  df_melted = df.melt(id_vars=['country_name', 'indicator_name'], var_name='year', value_name='value')
  df_melted['year'] = df_melted['year'].astype(int) 
  return df_melted