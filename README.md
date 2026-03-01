# Zubi Messenger 💬

> **Aviso:** Este projeto é resultado de um **desafio prático** do curso de Formação Python da [Rocketseat](https://www.rocketseat.com.br/). Ele foi desenvolvido com fins exclusivamente educacionais e de aprendizado.

Um aplicativo de chat em tempo real simples e moderno, desenvolvido para consolidar os conhecimentos em comunicação via WebSockets utilizando Python.

## 🚀 Tecnologias Utilizadas

- **Python 3**
- **Flask** (Microframework web)
- **Flask-SocketIO** (Comunicação em tempo real / WebSockets)
- **HTML/CSS** (Interface do usuário com design moderno)
- **Google Generative AI** (Respostas automatizadas integradas com a API Gemini)

## 📋 Funcionalidades

- Interface de chat em tempo real.
- Design responsivo e moderno (Glassmorphism, Dark Mode).
- Integração de Inteligência Artificial usando a API do **Google Gemini** para reponder automaticamente.
- Envio e recebimento instantâneo de mensagens sem recarregar a página.

## 🛠️ Como Executar o Projeto

1. Clone o repositório:

   ```bash
   git clone <url-do-seu-repositorio>
   cd zubi-messenger
   ```

2. Crie e ative um ambiente virtual (recomendado):

   ```bash
   python -m venv venv
   # No Windows:
   .\venv\Scripts\activate
   # No Linux/Mac:
   source venv/bin/activate
   ```

3. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

4. Configure as variáveis de ambiente:
   - Renomeie o arquivo `.env.example` para `.env`
   - Abra o arquivo `.env` e preencha com a sua chave da API do Google Gemini.

5. Execute a aplicação:

   ```bash
   python app.py
   ```

6. Acesse no seu navegador através do endereço:
   `http://127.0.0.1:5000`

---

_Desenvolvido durante o Módulo 03 da Formação Python._
