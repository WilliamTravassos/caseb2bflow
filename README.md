# Projeto de Integração Supabase + Z-API

Este projeto conecta-se ao Supabase para buscar contatos e envia mensagens de WhatsApp utilizando a Z-API.

Pré-requisitos

Python 3.13.5
- Conta no [Supabase](https://supabase.com/)
- Conta e credenciais da [Z-API](https://z-api.io/)
- Arquivo `.env` configurado

---

Passos de Setup

1. Criar a tabela no Supabase
Crie uma tabela chamada `contatos` com as seguintes colunas:

| Coluna         | Tipo    | Descrição                            |
|----------------|---------|--------------------------------------|
| id             | int8    | ID do contato (Primary Key)          |
| nome           | text    | Nome do contato                      |
| telefone       | int8    | Telefone no formato DDD+Número (sem +55) |

---

2. Configurar variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto com:

env
## SUPABASE ##
SUPABASE_URL=sua_url_supabase
SUPABASE_KEY=sua_chave_supabase

## Z-API ##
ZAPI_TOKEN=sua_chave_zapi
ZAPI_CLIENT_ID=seu_client_id
ZAPI_ACESS_TOKEN=seu_access_token

---

3. Instalar dependências

pip install -r requirements.txt

---

4. Como rodar

python main.py

O script irá:
Buscar contatos no Supabase.
Enviar mensagem de WhatsApp para cada contato encontrado.

Observações
Os números de telefone devem estar sem código do país no banco (ex: 83999999999), pois o código 55 será adicionado automaticamente.
Certifique-se de que a Z-API está com a instância conectada ao WhatsApp.



