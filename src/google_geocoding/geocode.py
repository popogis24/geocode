import requests
import pandas as pd

def geocode_address(address):
    api_key = '-dfJYn8-HT_zeiS6OApYAqXLG1zmq6oUFolqf3XJg0k'  # Substitua pelo seu próprio API Key da HERE Geocoding
    base_url = 'https://geocode.search.hereapi.com/v1/geocode'
    params = {
        'q': address,
        'apiKey': api_key
    }
    response = requests.get(base_url, params=params)
    data = response.json()
    if data['items']:
        location = data['items'][0]['position']
        return location['lat'], location['lng']
    else:
        return None, None

def geocode_dataframe(df, address_column):
    lats = []
    lngs = []
    for index, row in df.iterrows():
        address = row[address_column]
        lat, lng = geocode_address(address)
        lats.append(lat)
        lngs.append(lng)
    df['Latitude'] = lats
    df['Longitude'] = lngs
    return df

# Ler a planilha
file_path = '/Users/andersonstolfi/Documents/coding/google_geocoding/xlsx/Diretório off-line hoteis ativos _ambiente Kontik Franstur_Argo.xlsx'
sheet_name = 'Planilha4'  # Altere para o nome da sua folha
address_column = 'geocode_end'  # Altere para o nome da coluna de endereços

df = pd.read_excel(file_path, sheet_name=sheet_name)

# Geocodificar os endereços
df = geocode_dataframe(df, address_column)

# Salvar a planilha com as coordenadas geográficas adicionadas
output_file = '/Users/andersonstolfi/Documents/coding/google_geocoding/xlsx/output.xlsx'
df.to_excel(output_file, index=False)

print("Planilha geocodificada salva com sucesso!")

