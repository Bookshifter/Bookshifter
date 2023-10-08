import requests

def api_register(params):
    message = ''
    response = None
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
            message = 'Método não suportado.'
            return None, message
        
    if response.status_code == 403:
        message = {'error': 'Proibido de realizar a solicitação.', 'response': response}
    elif response.status_code == 404:
        message = {'error': 'Não encontrado.', 'response': response}
    elif response.status_code == 500:
        message = {'error': 'Erro de servidor.', 'response': response}
    elif response.status_code == 200:
        message = {'success': 'OK.', 'response': response}
    elif response.status_code == 201:
        message = {'success': 'Criado.', 'response': response}
    elif response.status_code == 202:
        message = {'success': 'Aceito.', 'response': response}
    else:
        message = {'error': response}
        
    
    return response, message