import requests

# Obtener las tasas de cambio más recientes de la API de Open Exchange Rates
response = requests.get('https://openexchangerates.org/api/latest.json?app_id=TU-API')
rates = response.json()['rates']


# Definir las tasas de conversión
MXN_TO_USD = rates['USD'] / rates['MXN']

#Pedir la cantidad en pesos 
mxn = float(input("Ingrese la cantidad en pesos mexicanos: "))

#Hacer la conversion 
usd = mxn * MXN_TO_USD

#Salida de informacion
print(f'\n[{mxn:.2f} pesos mexicanos son equivalentes a]:')
print(f'--> {usd:.2f} dólares estadounidenses')