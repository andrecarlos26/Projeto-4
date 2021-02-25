import requests
import json
import base64 #formatar arquivo

def lambda_handler(event,context):
    envia(event['Records'])
    return 'foi'

def envia(stream):
    token_TH = 'ZRFz0UyXakdCO1EjIAgw'
    for i in stream:
        info_cidade = i['kinesis']['data']
        info_cidade = base64.b64decode(info_cidade).decode('iso-8859-1')
        requests.post(
                'https://thingsboard.cloud/api/v1/' + token_TH + '/telemetry',
                data=info_cidade
            )
