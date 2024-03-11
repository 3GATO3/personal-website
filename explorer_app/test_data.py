from .data_utils import reshape_debt_data

sample_data_path = 'data/general_government_debt.csv'

transformed_data = reshape_debt_data(sample_data_path)
print(transformed_data.tail())  
