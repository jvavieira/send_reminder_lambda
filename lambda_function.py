import boto3
import json
from botocore.exceptions import ClientError
from twilio.rest import Client

def get_secret():
    secret_name = "twilio/credentials"
    region_name = "sa-east-1"

    session = boto3.session.Session()
    client = session.client(service_name='secretsmanager', region_name=region_name)

    try:
        response = client.get_secret_value(SecretId=secret_name)
    except ClientError as e:
        raise e

    secret_dict = json.loads(response['SecretString'])
    return secret_dict

def send_whatsapp_message():
    secrets = get_secret()
    account_sid = secrets['TWILIO_ACCOUNT_SID']
    auth_token = secrets['TWILIO_AUTH_TOKEN']

    client = Client(account_sid, auth_token)

    from_whatsapp_number = 'whatsapp:+14155238886'
    to_whatsapp_number = 'whatsapp:+558181456658'

    message_body = "Oi, mo ❤️. Hora de tomar seu remédio!! ⏰"

    message = client.messages.create(
        body=message_body,
        from_=from_whatsapp_number,
        to=to_whatsapp_number
    )

    print(f'Mensagem enviada com SID: {message.sid}')

def lambda_handler(event, context):
    try:
        send_whatsapp_message()
        return {
            'statusCode': 200,
            'body': json.dumps('Mensagem enviada com sucesso!')
        }
    except Exception as e:
        print(f"Erro ao enviar mensagem: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps(f'Erro: {str(e)}')
        }

# Para testar localmente:
#send_whatsapp_message()
