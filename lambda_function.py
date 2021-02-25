import requests
import json
import time

def lambda_handler():
    data = time.strftime('%Y-%m-%d', time.localtime())
    hora = time.strftime('%H', time.localtime())
    request = requests.get('https://apitempo.inmet.gov.br/estacao/dados/'+data+'/'+hora+'00')

    pe = []
    obj = json.loads(request.text)
    for i in obj:
        if i['UF']=='PE':
            pe.append(i)

    info = ''
    lista_info = []
    for i in pe:
        #print(i)
        uf = i['UF']
        cidade = i['DC_NOME']
        tem_ins = i['TEM_INS']
        umd_max = i['UMD_INS']
        #info = (uf, cidade, tem_ins, umd_max)
        lista_info.append((uf, cidade, tem_ins, umd_max))
    return lista_info


print(lambda_handler())
