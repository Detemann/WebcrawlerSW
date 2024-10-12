import requests
import bs4
import os
import time

url = "https://www.pciconcursos.com.br/concursos/sudeste/#ES"

def getConcursos():
    response = requests.get(url)

    if response.status_code == 200:
        if os.path.exists("oportunidades.csv"):
            os.remove("oportunidades.csv")

        print("OK!")
        write = "Local;Descricao;Link;"
        soup = bs4.BeautifulSoup(response.text, 'html.parser')
        
        links = soup.find_all('a')
        
        for link in links:
            local = link.get_text()
            
            href = link.get('href')
            desc = link.get('title')
            if desc != None:
                write += "\n"+local+";"+desc+";"+href+";"


        f = open("oportunidades.csv", "a")
        f.write(write)
        f.close()
    else:
        print("Erro de conexão\n")


while True:
    print("Iniciado...")
    getConcursos()
    # Itera a cada 5 minutos
    time.sleep(600)