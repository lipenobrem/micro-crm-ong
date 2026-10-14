from flask import Blueprint, request, jsonify
import requests
import os
import re
from app import db
from app.models import Voluntario, Doacao 

bot = Blueprint('bot', __name__)
NOME_BOT = "Boti"

@bot.route('/webhook', methods=['POST'])
def webhook():
    dados = request.get_json()
    
    if "message" in dados and "text" in dados["message"]:
        chat_id = str(dados["message"]["chat"]["id"])
        texto_recebido = dados["message"]["text"].strip()
        primeiro_nome = dados["message"]["from"]["first_name"]
        
        voluntario = Voluntario.query.filter_by(telegram_id=chat_id).first()
        texto_min = texto_recebido.lower() 
        
        if not voluntario:
            novo_voluntario = Voluntario(nome=primeiro_nome, telegram_id=chat_id)
            db.session.add(novo_voluntario)
            db.session.commit()
            
            texto_resposta = (f"Olá, {primeiro_nome}! \n Bem-vindo à nossa ONG.\n\n"
                              f"Eu sou o {NOME_BOT}, o seu assistente virtual. Como posso te ajudar hoje?\n"
                              "Digite 1 - Quero ser voluntário\n"
                              "Digite 2 - Quero fazer uma doação\n"
                              "Digite 'Sobre' para saber mais sobre nós.")
        else:
            if texto_recebido == "1":
                texto_resposta = "Que excelente notícia! Para avançarmos, por favor, digite o seu melhor e-mail:"
            elif texto_recebido == "2" or any(palavra in texto_min for palavra in ["doar", "doação", "contribuir"]):
                texto_resposta = ("Obrigado pela doação! Aceitamos três tipos de doação. Qual tipo de doação quer fazer?\n\n"
                                  "Digite 'Dinheiro'\n"
                                  "Digite 'Alimentos'\n"
                                  "Digite 'Roupas'")
                
            elif any(palavra in texto_min for palavra in ["dinheiro", "pix", "financeira", "valor"]):
                nova_doacao = Doacao(tipo='Financeira', descricao=f'Intenção de doação via Telegram ({voluntario.nome})')
                db.session.add(nova_doacao)
                db.session.commit()
                texto_resposta = ("Doação financeira selecionada! \n"
                                  "Por favor, envie o valor desejado para a nossa chave PIX:\n"
                                  "Chave: xxxx@ong-exemplo.org\n\n"
                                  "A sua intenção de doação foi registada. Muito obrigado!")

            elif any(palavra in texto_min for palavra in ["alimento", "alimentos", "comida", "cesta"]):
                nova_doacao = Doacao(tipo='Alimentos', descricao=f'Intenção de doação via Telegram ({voluntario.nome})')
                db.session.add(nova_doacao)
                db.session.commit()
                texto_resposta = ("Doação de alimentos selecionada! \n"
                                  "Pode entregar os alimentos não perecíveis na nossa sede:\n"
                                  "Rua xxxx, xxx - Segunda a Sexta, das 9h às 17h.\n"
                                  "Registamos a sua intenção. Muito obrigado!")

            elif any(palavra in texto_min for palavra in ["roupa", "roupas", "agasalho", "agasalhos", "vestuario"]):
                nova_doacao = Doacao(tipo='Roupas', descricao=f'Intenção de doação via Telegram ({voluntario.nome})')
                db.session.add(nova_doacao)
                db.session.commit()
                texto_resposta = ("Doação de roupas selecionada! \n"
                                  "Aceitamos roupas em bom estado. Pode deixá-las na nossa sede:\n"
                                  "Rua xxxx, xxx - Segunda a Sexta, das 9h às 17h.\n"
                                  "Registamos a sua intenção. Muito obrigado!")
                
            elif re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', texto_recebido):
                voluntario.email = texto_recebido
                db.session.commit()
                texto_resposta = f"Feito! O seu e-mail foi registado/atualizado para: {texto_recebido} "
                
            elif texto_recebido.count("@") > 0:
                texto_resposta = "Hmm, esse formato de e-mail parece inválido. Por favor, digite um e-mail correto."
                
            else:
                if any(palavra in texto_min for palavra in ["oi", "olá", "ola", "bom dia", "boa tarde", "boa noite"]):
                    texto_resposta = (f"Olá de novo, {voluntario.nome}! Aqui é o {NOME_BOT} \n\n"
                                      "Como posso te ajudar hoje?\n"
                                      "Digite 1 - Quero ser voluntário\n"
                                      "Digite 2 - Quero fazer uma doação\n"
                                      "Digite 'Sobre' para saber mais")

                elif any(palavra in texto_min for palavra in ["sobre", "o que", "faz", "objetivo", "missão"]):
                    texto_resposta = ("Nossa ONG atua na educação e desenvolvimento comunitário. \n\n"
                                      "Toda doação é revertida 100% para os nossos projetos.\n\n"
                                      "Digite 1 - Quero ser voluntário\n"
                                      "Digite 2 - Quero fazer uma doação")
                
                elif any(palavra in texto_min for palavra in ["voluntário", "ajudar", "trabalhar", "vaga"]):
                    texto_resposta = "Parece que você quer colaborar conosco! \n Digite 1 para iniciar o seu registro."
                
                else:
                    texto_resposta = (f"Desculpe, não entendi muito bem. \n\n"
                                      "Consigo te ajudar com estas opções:\n"
                                      "1 - Quero ser voluntário\n"
                                      "2 - Quero fazer uma doação")
        
        token = os.getenv("TELEGRAM_BOT_TOKEN")
        url_telegram = f"https://api.telegram.org/bot{token}/sendMessage"
        payload = {"chat_id": chat_id, "text": texto_resposta}
        requests.post(url_telegram, json=payload)

    return jsonify({"status": "ok"}), 200