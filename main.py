import json
from ibm_watson import AssistantV2
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

import warnings
warnings.filterwarnings('ignore')

apikey = 'hCXIFUhO3aLW-ypw-BxcR8c5BN714QzNkIyCNxi3YvUt'
url = 'https://api.us-south.assistant.watson.cloud.ibm.com'
assistantID = '993a081b-958d-4cb9-9ce8-2e4facb265ea'

authenticator = IAMAuthenticator(apikey)
assistant = AssistantV2(
    version = '2018-09-20',
    authenticator=authenticator)
assistant.set_service_url(url)
assistant.set_disable_ssl_verification(True)

session = assistant.create_session(assistantID).get_result()
session_json = json.dumps(session, indent=2)
session_dict = json.loads(session_json)
session_id = session_dict['session_id']
print(session_id)

print('******* INICIANDO CONVERSA')
message = assistant.message(
    assistantID,
    session_id,).get_result()
message_json = json.dumps(message, indent=2)
message_dict = json.loads(message_json)
for i in range(len(message_dict['output']['generic'])):
    print(message_dict['output']['generic'][i]['text'])
texto = input('resposta: ')
while texto:
    message = assistant.message(
        assistantID,
        session_id,
        input={'text': texto}).get_result()
    message_json = json.dumps(message, indent=2)
    message_dict = json.loads(message_json)
    for i in range(len(message_dict['output']['generic'])):
        print(message_dict['output']['generic'][i]['text'])
        texto = input('resposta: ')

print('*******Encerrando a sessão')
assistant.delete_session(assistantID,session_id)
print('Sessão encerrada')