# 🤝 Micro-CRM para ONGs com Bot de Telegram

Um mini sistema de Customer Relationship Management (CRM) construído em Python, desenhado especificamente para Organizações Não Governamentais (ONGs). O sistema integra um painel administrativo web e um assistente virtual de triagem via Telegram.

Este projeto foi desenvolvido como para a matéria de projeto de extensão 4° semestre com o objetivo de otimizar o atendimento e a gestão de contatos de instituições do terceiro setor, aplicando conceitos de arquitetura modular, integração de backend com banco de dados relacional e exposição de webhooks locais para comunicação com a API do Telegram.

## ⚙️ Arquitetura e Tecnologias

- **Backend:** Python com framework Web (Flask).
- **Banco de Dados:** SQLite.
- **Frontend Web:** HTML5, CSS3 e JavaScript.
- **Integração Telegram:** Webhooks locais expostos através do **Ngrok**.

## ✨ Funcionalidades Detalhadas

### Módulo Web Administrativo
- **Autenticação:** Sistema de login seguro para administradores e voluntários.
- **Dashboard:** Painel central para visualização do fluxo de atendimentos e métricas da ONG.
- **Gestão de Cadastros:** Interface CRUD (Criar, Ler, Atualizar e Apagar) para gerenciar os dados das pessoas assistidas.

### Módulo Chatbot Telegram
- Recebimento de mensagens em tempo real através de rotas do tipo Webhook integradas à API do Telegram.
- Lógica de resposta automatizada para triagem de contatos antes de encaminhar para o Dashboard.

## 🚀 Como Configurar e Executar

1. **Clone o repositório:**
   git clone github.com/lipenobrem/Micro-crm-chatbot.git
   cd Micro-crm-chatbot

2. **Crie e ative o ambiente virtual:**
   python -m venv venv
   .\venv\Scripts\activate

3. **Instale as dependências:**
   pip install -r requirements.txt

4. **Inicie a Aplicação Web:**
   python main.py

5. **Inicie o Túnel Webhook (Ngrok):**
   Em um novo terminal, exponha a porta local do servidor (ex: 5000):
   ngrok http 5000

## 👨‍💻 Desenvolvedor
**Felipe Nobre**
Desenvolvido unindo conhecimentos de análise de sistemas, automação, backend e interfaces web.
