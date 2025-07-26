import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
from time import sleep

# Evitar bloqueio de ação suspeita
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36"
}

def create_driver_with_headers():
    chrome_options = Options()
    
    chrome_options.add_argument(f"user-agent={headers['User-Agent']}")

    driver = webdriver.Chrome(options=chrome_options)
    
    return driver

def extrair_dados_empresa(driver, url):
    try:
        driver.get(url)
        
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="newPerformanceCard"]'))
        )

        sleep(3)

        dados = {
            "URL": url,
            "Recebeu Reclamações": "N/A",
            "Respondeu Reclamações": "N/A",
            "Aguardando Resposta": "N/A",
            "Reclamações Avaliadas": "N/A",
            "Voltariam a Fazer Negócio": "N/A",
            "Reclamações Recebidas": "N/A",
            "Tempo Médio": "N/A"
        }

        dados['Recebeu Reclamações'] = driver.find_element(By.XPATH, '//*[@id="newPerformanceCard"]/div[2]/div[1]/span/strong').text
        dados['Respondeu Reclamações'] = driver.find_element(By.XPATH, '//*[@id="newPerformanceCard"]/div[2]/div[2]/span/strong').text
        dados['Aguardando Resposta'] = driver.find_element(By.XPATH, '//*[@id="newPerformanceCard"]/div[2]/div[3]/span/strong').text
        dados['Reclamações Avaliadas'] = driver.find_element(By.XPATH, '//*[@id="newPerformanceCard"]/div[2]/div[4]/span').text
        dados['Voltariam a Fazer Negócio'] = driver.find_element(By.XPATH, '//*[@id="newPerformanceCard"]/div[2]/div[5]/span/strong').text
        dados['Reclamações Recebidas'] = driver.find_element(By.XPATH, '//*[@id="newPerformanceCard"]/div[2]/div[6]/span/strong').text
        dados['Tempo Médio'] = driver.find_element(By.XPATH, '//*[@id="newPerformanceCard"]/div[2]/div[7]').text

        return dados

    except Exception as e:
        logging.error(f"Erro ao extrair dados da empresa {url}: {e}")
        return {
            "URL": url,
            "Recebeu Reclamações": "N/A",
            "Respondeu Reclamações": "N/A",
            "Aguardando Resposta": "N/A",
            "Reclamações Avaliadas": "N/A",
            "Voltariam a Fazer Negócio": "N/A",
            "Reclamações Recebidas": "N/A",
            "Tempo Médio": "N/A"
        }
def fechar_driver(driver):
    driver.quit()

def obter_dados_para_urls(urls):
    dados_coletados = []
    
    for url in urls:
        driver = create_driver_with_headers()
        dados_empresa = extrair_dados_empresa(driver, url)
        dados_coletados.append(dados_empresa)
        
        fechar_driver(driver)

    df = pd.DataFrame(dados_coletados)
    df.to_excel("dados_empresas.xlsx", index=False)
    print("Dados salvos em 'dados_empresas.xlsx'")

