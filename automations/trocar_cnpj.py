# automations/trocar_cnpj.py
import os
import time
from random import random
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Note que não precisamos mais de 'sys' ou 'load_dotenv' aqui.
# O login e as configurações serão gerenciados pelo main.py.

def executar(driver):
    """
    Executa a automação para atualizar o CNPJ de uma empresa de teste.
    Recebe o 'driver' do Selenium já logado como argumento.
    """
    try:
        # Carrega as variáveis de ambiente necessárias para ESTA automação
        CNPJ = os.getenv("CNPJ_TESTE")
        NOME_EMPRESA = os.getenv("EMPRESA_TESTE")

        print("Iniciando automação: Atualizar CNPJ...")
        wait = WebDriverWait(driver, 20)

        print("Navegando para a área de empresas...")
        card_cnd = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="cnd2"]')))
        card_cnd.click()

        opc_empresa = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#nav > ul > li:nth-child(3)')))
        opc_empresa.click()

        print(f"Buscando pela empresa: {NOME_EMPRESA}")
        input_empresa = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="JColResizer0"]/thead/tr[2]/td[2]/input')))
        
        for char in NOME_EMPRESA:
            input_empresa.send_keys(char)
            time.sleep(random() / 5)
        input_empresa.send_keys(Keys.ENTER)

        print("Acessando informações da empresa...")
        info_empresa = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="JColResizer0"]/tbody/tr/td[10]/a[1]')))
        info_empresa.click()

        print(f"Atualizando CNPJ para: {CNPJ}")
        input_doc = wait.until(EC.visibility_of_element_located((By.ID, 'numero_documento')))
        input_doc.clear()
        input_doc.send_keys(CNPJ)

        botao_salvar = driver.find_element(By.ID, 'botao_salvar')
        driver.execute_script("arguments[0].click();", botao_salvar)

        wait.until(EC.text_to_be_present_in_element((By.TAG_NAME, 'body'), "Empresa atualizada com sucesso"))
        print("✅ Sucesso: CNPJ atualizado!")
        return True

    except Exception as e:
        print(f"❌ Erro na automação de troca de CNPJ: {e}")
        return False