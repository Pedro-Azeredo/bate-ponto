from flask import Flask, jsonify
from playwright.sync_api import sync_playwright
from loguru import logger
import os

# Configurando o Flask
app = Flask(__name__)

# Função para realizar a automação
def preencher_ponto():
    with sync_playwright() as p:
        navegador = p.chromium.launch(headless=True)  # Headless True para rodar no Heroku
        context = navegador.new_context()
        context.grant_permissions(["geolocation"], origin="https://app2.pontomais.com.br/")
        context.set_geolocation({"latitude": -22.912873, "longitude": -42.927942})

        pagina = context.new_page()
        pagina.goto("https://app2.pontomais.com.br/")

        pagina.fill('xpath=//*[@id="container-login"]/div[1]/div/div[4]/div[1]/login-form/pm-form/form/div/div/div[1]/pm-input/div/div/pm-text/div/input', '18153221795')
        pagina.fill('xpath=//*[@id="container-login"]/div[1]/div/div[4]/div[1]/login-form/pm-form/form/div/div/div[2]/pm-input/div/div/pm-password/div/input', 'Pedro123@')
        pagina.locator('//*[@id="container-login"]/div[1]/div/div[4]/div[1]/login-form/pm-button[1]/button').click()

        logger.info("Ponto preenchido.")
        navegador.close()
    return {"status": "Ponto preenchido com sucesso!"}

# Rota principal para teste
@app.route('/')
def index():
    return "Servidor está rodando com Playwright no Heroku!"

# Rota para disparar a automação
@app.route('/preencher-ponto')
def ponto():
    resultado = preencher_ponto()
    return jsonify(resultado)

# Iniciando o servidor
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Porta configurada pelo Heroku
    app.run(host="0.0.0.0", port=port)
