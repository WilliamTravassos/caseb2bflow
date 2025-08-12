import os
import requests
from dotenv import load_dotenv
from supabase import create_client, Client

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Lê as variáveis de ambiente
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
SUPABASE_URL = os.getenv("SUPABASE_URL")
ZAPI_TOKEN = os.getenv("ZAPI_TOKEN")
ZAPI_CLIENT_ID = os.getenv("ZAPI_CLIENT_ID")
ZAPI_ACESS_TOKEN = os.getenv("ZAPI_ACESS_TOKEN")

# Cria a conexão com o Supabase usando as variáveis lidas
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def get_contacts():
    # Substitua 'contatos' pelo nome da sua tabela no Supabase
    try:
        response = supabase.from_('contatos').select("*").execute()
        print (response.data)
        return response.data
        
    except Exception as e:
        print(f"Erro ao buscar contatos do Supabase: {e}")
        return []

def send_whatsapp_message(phone_number, contact_name):
    url = f"https://api.z-api.io/instances/{ZAPI_CLIENT_ID}/token/{ZAPI_TOKEN}/send-text"
    
    # Formata o número para incluir o código do país, se necessário (ex: 55 para o Brasil)
    # Ex: 5511999999999
    formatted_phone = f"55{phone_number}" 
    
    message_text = f"Olá {contact_name}, tudo bem com você?"
    
    payload = {
        "phone": formatted_phone,
        "message": message_text
    }
    
    headers = {
        "Content-Type": "application/json",
        "client-token": "F29ec721d7f1740549aa2eb5ab60e5c94S"  # Novo cabeçalho
    }

    try:
        response = requests.post(url, json=payload, headers=headers)
        if response.status_code == 200:
            print (response.json())
            print(f"Mensagem enviada com sucesso para {contact_name} ({phone_number})!")
        else:
            print(f"Erro ao enviar mensagem para {contact_name} ({phone_number}): {response.text}")
    except Exception as e:
        print(f"Erro na requisição para a Z-API: {e}")

if __name__ == "__main__":
    contacts = get_contacts()

    if contacts:
        for contact in contacts:
            # Assume que a tabela tem as colunas 'nome' e 'numero_telefone'
            send_whatsapp_message(contact['telefone'], contact['nome'])
    else:
        print("Nenhum contato encontrado no Supabase.")