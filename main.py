# main.py
import os
import sys
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from automations import trocar_cnpj

def exibir_menu(automations):
    """Exibe o menu de opções para o usuário com uma estrutura melhorada."""
    print("\n" + "="*45)
    print("---  Automação SCI Web  ---".center(45))
    print("="*45)
    print("\nEscolha a automação que deseja executar:")
    
    for key, value in automations.items():
        # Formata para que a descrição comece sempre no mesmo lugar
        print(f"  [{key}] - {value['description']}")
        
    print("-" * 45)
    print("  [0] - Sair")
    print("\n" + "="*45)
    
    return input("Digite sua escolha -> ")

def fazer_login(driver, user, password):
    """Função centralizada para realizar o login."""
    try:
        driver.get("https://www.sciweb.com.br")
        driver.maximize_window()
        wait = WebDriverWait(driver, 20)
        
        print("🔑 Realizando login...")
        input_user = wait.until(EC.visibility_of_element_located((By.ID, 'usuario')))
        input_user.send_keys(user)
        
        driver.find_element(By.ID, 'senha').send_keys(password)
        driver.find_element(By.ID, 'btLoginPrincipal').click()
        
        # Confirma que o login foi bem-sucedido esperando por um elemento da página principal
        wait.until(EC.visibility_of_element_located((By.ID, 'cnd2')))
        print("✅ Login realizado com sucesso!")
        return True
    except Exception as e:
        print(f"❌ Falha no login: {e}")
        return False

def main():
    """Função principal que gerencia o menu e a execução."""
    load_dotenv()
    LOGIN_USER = os.getenv("SCI_USER")
    LOGIN_PASS = os.getenv("SCI_PASS")
    
    # Dicionário de automações disponíveis
    # A chave é a opção do menu, o valor contém a descrição e a função a ser chamada
    automations = {
        "1": {
            "description": "Atualizar CNPJ da Empresa de Teste",
            "function": trocar_cnpj.executar
        },
        # Futuramente, adicione novas automações aqui:
        # "2": {
        #     "description": "Gerar Relatório Mensal",
        #     "function": relatorio_mensal.executar
        # },
    }

    choice = exibir_menu(automations)

    if choice == "0":
        print("👋 Saindo...")
        sys.exit(0)
    
    if choice not in automations:
        print("❌ Opção inválida!")
        sys.exit(1)
        
    driver = None
    try:
        # Inicia o navegador
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=chrome_options)
        
        # Faz o login
        if not fazer_login(driver, LOGIN_USER, LOGIN_PASS):
            # Se o login falhar, não continua
            return 
        
        # Pega a função escolhida do dicionário e a executa
        selected_automation = automations[choice]['function']
        selected_automation(driver) # Passa o driver já logado para a função

    except Exception as e:
        print(f"❌ Ocorreu um erro geral no processo: {e}")
    finally:
        # A decisão de fechar ou não o navegador fica aqui
        input("\n... Pressione Enter para fechar o navegador ...")
        if driver:
            driver.quit()

if __name__ == "__main__":
    main()