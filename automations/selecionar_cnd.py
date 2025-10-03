import os
import time
from random import random
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def executar(driver):
    """
    Executa a automação para selecionar CND e salvar.
    Recebe o 'driver' do Selenium já logado como argumento.
    """

    try:
        CND_SALVAR = os.getenv("CND_VINCULAR")

        print("Iniciando automação: Selecionar CND...")
        wait = WebDriverWait(driver, 20)

        print("Navegando para a área de CNDS...")
        card_cnd = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="cnd2"]')))
        card_cnd.click()

        opc_cnd = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#nav > ul > li:nth-child(5)')))
        opc_cnd.click()

        print(f"Buscando pela empresa: {CND_SALVAR}")
        input_cnd = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="JColResizer0"]/thead/tr[2]/td[2]/input')))
        
        for char in CND_SALVAR:
            input_cnd.send_keys(char)
            time.sleep(random() / 5)
        input_cnd.send_keys(Keys.ENTER)

        
        check = driver.find_element(By.XPATH, '//*[@id="JColResizer0"]/tbody/tr/td[1]/input')
        check.click()

        botao_salvar = driver.find_element(By.XPATH, '//*[@id="formSalvar"]/div/button')
        driver.execute_script("arguments[0].click();", botao_salvar)

        wait.until(EC.text_to_be_present_in_element((By.TAG_NAME, 'body'), "CND's selecionadas com sucesso!"))
        print("✅ Sucesso: CND selecionada!")
        return True

    except Exception as e:
        print(f"❌ Erro na automação vincular CND: {e}")
        return False