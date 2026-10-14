🤝 Micro-CRM para ONGs com Bot de WhatsApp

Um sistema completo de Customer Relationship Management (CRM) construído em Python, desenhado especificamente para Organizações Não Governamentais (ONGs). O sistema integra um painel administrativo web e um assistente virtual de triagem via WhatsApp.

Este projeto demonstra a construção de uma arquitetura modular, integrando o backend com uma base de dados relacional e a exposição de webhooks locais para comunicação com APIs externas.

⚙️ Arquitetura e Tecnologias

Backend: Python com framework Web (Flask).

Base de Dados: SQLite (com modelagem de dados).

Frontend Web: HTML5, CSS3, JavaScript (Renderização de templates do lado do servidor).

Integração WhatsApp: Webhooks locais expostos através do Ngrok.

✨ Funcionalidades Detalhadas

Módulo Web Administrativo

Autenticação: Sistema de login seguro para administradores e voluntários.

Dashboard: Painel central para visualização do fluxo de atendimentos e métricas da ONG.

Gestão de Cadastros: Interface CRUD (Criar, Ler, Atualizar e Apagar) para gerir os dados das pessoas assistidas.

Módulo Chatbot WhatsApp

Receção de mensagens em tempo real através de rotas do tipo Webhook.

Lógica de resposta automatizada para triagem de contatos antes de encaminhar para o Dashboard.

🚀 Como Configurar e Executar

Clone o repositório:

git clone https://github.com/lipenobrem/micro-crm-ong.git
cd micro-crm-ong


Crie e ative o ambiente virtual:

python -m venv venv
.\venv\Scripts\activate


Instale as dependências:
Certifique-se de instalar as bibliotecas necessárias (ex: Flask, python-dotenv, etc):

pip install -r requirements.txt


Inicie a Aplicação Web:

python main.py


Inicie o Túnel Webhook (Ngrok):
Para que o WhatsApp consiga comunicar com a sua máquina local, abra um novo terminal e execute o Ngrok na mesma porta do seu servidor Python (normalmente 5000):

ngrok http 5000


Nota: Copie o endereço https fornecido pelo Ngrok e configure-o no seu provedor da API do WhatsApp apontando para a rota correspondente (ex: /api/bot).

👨‍💻 Desenvolvedor

Felipe Nobre
Desenvolvido no âmbito do projeto de extensão universitária do 4º semestre de Análise e Desenvolvimento de Sistemas.
