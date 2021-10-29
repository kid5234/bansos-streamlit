import pandas as pd  #pip install pandas openpyxl


df = pd.read_excel(
	io='bansos_clean.xlsx',
	engine='openpyxl',
	sheet_name='Sheet1',
	skiprows=0,
	usecols='A:S',
	nrows=24924,
)

print(df)
