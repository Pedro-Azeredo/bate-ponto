from playwright.sync_api import sync_playwright
from loguru import logger
import time

with sync_playwright() as p:
    navegador = p.chromium.launch(headless=False)
    context = navegador.new_context()
    context.grant_permissions(["geolocation"], origin="https://app2.pontomais.com.br/")
    context.set_geolocation({"latitude": -22.912873, "longitude": -42.927942})

    pagina = context.new_page()
    pagina.goto("https://app2.pontomais.com.br/")

    pagina.fill('xpath=//*[@id="container-login"]/div[1]/div/div[4]/div[1]/login-form/pm-form/form/div/div/div[1]/pm-input/div/div/pm-text/div/input', '18153221795')
    pagina.fill('xpath=//*[@id="container-login"]/div[1]/div/div[4]/div[1]/login-form/pm-form/form/div/div/div[2]/pm-input/div/div/pm-password/div/input', 'Pedro123@')
    pagina.locator('//*[@id="container-login"]/div[1]/div/div[4]/div[1]/login-form/pm-button[1]/button').click()

    #pagina.locator('/html/body/app-root/app-side-nav-outer-toolbar/dx-drawer/div/div[2]/dx-scroll-view/div[1]/div/div[1]/div[2]/div[1]/time-card-register/div/div[2]/div[2]/pm-time-card-register/pm-card/div/div[2]/div[1]/div[2]/div/pm-button/button/span').click()
    logger.info("Ponto preenchido.")

    time.sleep(10)