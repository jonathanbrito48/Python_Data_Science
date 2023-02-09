import pandas as pd

def transformador_arquivo(arquivo_origem_path, novo_destino_arquivo_path):
    with open(arquivo_origem_path,'r', encoding = 'UTF-8') as txt:
        dados = txt.read()
    json = pd.read_json(dados)
    dataframe = []
    dataframe.append(json.values)
    lista = []
    while len(lista) <= (len(dataframe[0])-1):
        for produto in dataframe:
            lista.append(dataframe[0][((len(dataframe[0])-1)-len(lista))][0])
    print(len(lista), 'itens adicionados')
    print('Transformando os dados...')
    arquivo_final = pd.DataFrame(lista)
    arquivo_final.to_excel(novo_arquivo_destino_path, index = False)
    print('Finalizado!')
