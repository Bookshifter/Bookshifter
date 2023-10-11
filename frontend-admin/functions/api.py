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
    
    match response.status_code:
        case 403:
            message = {'error': 'Proibido de realizar a solicitação.', 'response': response.text}
        case 404:
            message = {'error': 'Não encontrado.', 'response': response.text}
        case 500:
            message = {'error': 'Erro no servidor.', 'response': response.text}
        case 200:
            message = {'success': 'OK.', 'response': response.text}
        case 201:
            message = {'success': 'Criado.', 'response': response.text}
        case 202:
            message = {'success': 'Aceito.', 'response': response.text}
        case _:
            message = {'error': response.text}
    
    return response.text, message