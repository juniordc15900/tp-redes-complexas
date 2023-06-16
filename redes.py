import json
import pandas as pd

# Lista com os nomes dos arquivos CSV
arquivos_csv = ["datas/acid_vas_cerebral.csv", "datas/tabagismo.csv", "datas/infarto_mio.csv", "datas/renal.csv","datas/sedentarismo.csv","datas/sobrepeso.csv"]
names = ['acid_vas_cerebral', 'tabagismo', 'infarto_mio', 'renal', 'sedentarismo', 'sobrepeso']
# Lista para armazenar os dataframes
# dataframes = []

# # Loop para importar cada arquivo CSV e convertê-lo em dataframe
# for i,arquivo in enumerate(arquivos_csv):
#     # Importar o arquivo CSV em um dataframe
#     dataframe = pd.read_csv(arquivo,encoding='latin-1')
#     # Adicionar o dataframe à lista de dataframes
#     json_data = dataframe.to_json()
#     with open(f'{names[i]}.json', 'w') as file:
#         file.write(json_data)
print('Em São João del Rei\n')

for name in names:

    with open(f'jsons/{name}.json', 'r') as file:
        json_data = json.load(file)
        teste = json_data["Sistema de Cadastramento e Acompanhamento de Hipertensos e Diab\u00e9ticos - Minas Gerais"]["592"].split(';')
        print(f'Tem diabetes e {name} {teste[1]} , tem diabetes e não tem {name} {teste[2]} num total de {teste[3]}\n')