from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time

class TestTestey():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}
  
    def teardown_method(self, method):
        self.driver.quit()
  
    def test_teste(self):
        self.driver.get("https://www.yellowpages.com/")
        self.driver.set_window_size(786, 816)
        self.driver.find_element(By.ID, "query").click()
        self.driver.find_element(By.ID, "query").send_keys("Apartments")
        time.sleep(3)
        self.driver.find_element(By.ID, "location").click()
        self.driver.find_element(By.ID, "location").clear()
        self.driver.find_element(By.ID, "location").send_keys("San Francisco, CA")
        time.sleep(2)
        self.driver.find_element(By.ID, "location").send_keys(Keys.ENTER)
        time.sleep(6)
        #Pegando o HTML da pagina e transformando em texto
        pagina = self.driver.page_source
        site = BeautifulSoup(pagina, "html.parser")
        hospedagem = site.find_all("a", attrs="business-name")
        texto = site.text
        print(texto)
        #Gerando arquivo TXT
        arquivo = open("Apartamentos.txt", "a")
        arquivo.write(f"Apartamentos: {texto}\r\n")
        arquivo.close()