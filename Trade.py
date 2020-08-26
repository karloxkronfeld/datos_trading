from Datos import VerDatos

# Tecnologia = ['MSFT', 'GOOG', 'FB', 'T', 'CSCO', 'VZ', 'INTC', 'TSM', 'ORCL', 'SAP', 'ADBE', 'IBM', 'ACN',
#               'CRM', 'TXN', 'AVGO', 'NVDA', 'QCOM', 'UBER', 'INTU', 'ADP', 'TMUS', 'VMW', 'CCI', 'NOW',
#               'WDAY', 'AMAT', 'ADI', 'FIS', 'LHX', 'EQIX', 'DELL', 'CTSH', 'ADSK', 'AMD', 'ATVI', 'SQ',
#               'TWTR']
# BienesDeConsumo = ['AAPL', 'PG', 'KO', 'TM', 'PEP', 'NKE', 'PM', 'MO', 'MDLZ', 'EL', 'CL', 'GM', 'KMB',
#                    'PHG', 'TSLA', 'STZ', 'F', 'KHC', 'JCI', 'MNST', 'VFC', 'GIS', 'HSY', 'TSN', 'PCAR']
# Financieros = ['JPM', 'BAC', 'MA', 'WFC', 'C', 'PYPL', 'AXP', 'AMT', 'USB', 'GS', 'MS', 'BLK', 'CME', 'CB',
#                'V', 'AABA', 'PNC', 'BX', 'SCHW', 'MMC']
# Salud = ['JNJ', 'UNH', 'PFE', 'NVS', 'MRK', 'ABT', 'TMO', 'AZN', 'AMGN', 'LLY', 'SNY', 'GSK',
#          'ABBV', 'NVO', 'GILD', 'SYK', 'ANTM', 'BMY', 'CVS', 'BDX', 'CI', 'ISRG', 'BSX', 'ZTS',
#          'AGN', 'TAK', 'HCA', 'BIIB', 'ILMN', 'EW', 'VRTX', 'BAX', 'HUM', 'REGN', 'IQV', 'ALC', 'ALXN']
# Industrial = ['BA', 'HON', 'UTX', 'LMT', 'DHR', 'MMM', 'GE', 'CAT', 'NOC', 'GD', 'DE', 'RTN', 'ITW', 'WM',
#               'EMR', 'ABB']

misdatos = VerDatos("MSFT","2019-01-01","2020-09-01")
misdatos.graficar(volumen=True,media_movil=[20,50,200],soportes_resistencias=False,covid=True)

# comparar=VerDatos(fecha_inicial="2010-01-01",fecha_final="2020-09-01")
# comparar.subplots(["AMZN","GOOG","AAPL","CRM","FB","JPM","NKE","KO","DIS"])