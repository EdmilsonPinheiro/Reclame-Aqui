import logging
from scraper import extrator

def main():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')

    driver = extrator.create_driver_with_headers()

    try:
        urls = [
            'https://www.reclameaqui.com.br/empresa/f12-bet/',
            'https://www.reclameaqui.com.br/empresa/luva-bet/',
            'https://www.reclameaqui.com.br/empresa/tradicional-bet/',
            'https://www.reclameaqui.com.br/empresa/cosmo-entertainment/',
            'https://www.reclameaqui.com.br/empresa/betsson/',
            'https://www.reclameaqui.com.br/empresa/p9-com/'
        ]

        extrator.obter_dados_para_urls(urls)

    except Exception as e:
        logging.error(f"Ocorreu um erro durante a execução principal: {e}")
        print(f"Ocorreu um erro: {e}")
    finally:

        driver.quit()
        logging.info("Navegador fechado.")

if __name__ == "__main__":
    main()
