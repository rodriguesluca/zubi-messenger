import os
from google import genai
from dotenv import load_dotenv
from flask import Flask, render_template
from flask_socketio import SocketIO, send

# Carrega as variáveis do arquivo .env
load_dotenv()

app = Flask(__name__)
# Configura o SECRET_KEY puxando do .env
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "default-key-fallback")

# Configurando o SocketIO
socketio = SocketIO(app, cors_allowed_origins="*")

# Configurando o Gemini API
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


@app.route("/")
def index():
    # Rota que renderiza o nosso arquivo index.html
    return render_template("index.html")


@socketio.on("message")
def handle_message(msg):
    # Função do socketio responsável por verificar e retransmitir mensagens
    print(f"Mensagem recebida do usuário: {msg}")

    # 1. Envia a mensagem do usuário original para o chat
    send(f"Mensagem: {msg}", broadcast=True)

    try:
        # 2. Chama a IA do Gemini para gerar uma resposta baseada na mensagem
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=msg,
        )
        bot_reply = response.text

        # 3. Envia a resposta calculada pela IA de volta ao chat
        send(f"🤖 IA: {bot_reply}", broadcast=True)
        print(f"Bot respondeu: {bot_reply}")

    except Exception as e:
        error_msg = f"Desculpe, ocorreu um erro ao chamar a IA: {e}"
        send(f"🤖 IA: {error_msg}", broadcast=True)
        print(error_msg)


if __name__ == "__main__":
    socketio.run(app, debug=True)
