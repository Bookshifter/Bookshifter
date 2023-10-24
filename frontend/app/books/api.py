import requests
from flask import jsonify
import json

def api_books(params):
    message = ''
    response = None
    try:
        match params['method']:
            case 'POST':
                response = requests.post(json=params['data'], url=params['url'])
            case 'GET':
                response = requests.get(url=params['url'])
            case 'PATCH':
                response = requests.patch(json=params['data'], url=params['url'])
            case 'DELETE': 
                response = requests.delete(json=params['data'], url=params['url'])
            case _:
                response = {'error': 'Método não suportado.'}
    except requests.exceptions.ConnectionError:
        return {'error': 'Erro ao conectar na API do cadastro'}
    except Exception as e:
        return {'error': str(e)}
    
    match response.status_code:
        case 403:
            message = {'error': 'Proibido de realizar a solicitação.', 'response': response.text}
            return message
        case 404:
            message = {'error': 'Não encontrado.', 'response': response.text}
            return message
        case 500:
            message = {'error': 'Erro no servidor.', 'response': response.text}
            return message
        case 200:
            message = {'success': 'OK.', 'response': response.text}
            return response.text
        case 201:
            message = {'success': 'Criado.', 'response': response.text}
            return response.text
        case 202:
            message = {'success': 'Aceito.', 'response': response.text}
            return response.text
        case _:
            message = {'error': response.text}
            return message
        

def get_api_books(url):
    try:
        response = requests.get(url
                            # headers={"Authorization": f"Token {token}"}
                            )
    except requests.exceptions.ConnectionError:
        return {'error': 'Erro ao conectar na API.'}
    except Exception as e:
        response = None
        return {'error': str(e)}
    
    return response.json() if response.status_code == 200 else {'error': response.text}