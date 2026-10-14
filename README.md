# 🤝 Micro-CRM para ONGs com Bot de Telegram

> Um sistema completo de Customer Relationship Management (CRM) construído em Python, desenhado especificamente para Organizações Não Governamentais (ONGs). O sistema integra um painel administrativo web e um assistente virtual de triagem via **Telegram**.

Este projeto foi desenvolvido com o objetivo de otimizar o atendimento e a gestão de contatos de instituições do terceiro setor, aplicando conceitos de arquitetura modular, integração de backend com banco de dados relacional e exposição de webhooks locais para comunicação em tempo real com a API do Telegram.

---

## 🛠️ Tecnologias Utilizadas

<p align="left">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white" alt="Flask" />
  <img src="https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white" alt="SQLite" />
  <img src="https://img.shields.io/badge/Telegram_API-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white" alt="Telegram API" />
  <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white" alt="HTML5" />
  <img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white" alt="CSS3" />
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" alt="JavaScript" />
  <img src="https://img.shields.io/badge/Ngrok-1F1E37?style=for-the-badge&logo=ngrok&logoColor=white" alt="Ngrok" />
</p>

---

## ✨ Funcionalidades Detalhadas

<table>
  <tr>
    <td width="50%" valign="top">
      <h3>🖥️ Módulo Web Administrativo</h3>
      <ul>
        <li><b>Autenticação:</b> Sistema de login seguro para administradores e voluntários.</li>
        <li><b>Dashboard:</b> Painel central para visualização do fluxo de atendimentos e métricas da ONG.</li>
        <li><b>Gestão de Cadastros:</b> Interface CRUD (Criar, Ler, Atualizar e Apagar) para gerenciar os dados das pessoas assistidas.</li>
      </ul>
    </td>
    <td width="50%" valign="top">
      <h3>🤖 Módulo Chatbot Telegram</h3>
      <ul>
        <li><b>Webhook em Tempo Real:</b> Recebimento instantâneo de mensagens integrado à API do Telegram.</li>
        <li><b>Triagem Automatizada:</b> Lógica de resposta automática para qualificar e organizar os contatos antes de encaminhar para o Dashboard.</li>
        <li><b>Túnel Local:</b> Exposição segura de rotas locais via Ngrok para testes e operação.</li>
      </ul>
    </td>
  </tr>
</table>

---

## 🚀 Como Configurar e Executar
> 💡 **Pré-requisito:** Certifique-se de criar um arquivo `.env` na raiz do projeto contendo o seu token do BotFather (Telegram) e chaves de configuração antes de iniciar.

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
