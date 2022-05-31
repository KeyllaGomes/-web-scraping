from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
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

        ap1 = self.driver.find_element(By.XPATH, '//*[@id="lid-15819326"]/div/div/div[2]/div[1]').text
        ap2 = self.driver.find_element(By.XPATH, '//*[@id="lid-30834104"]/div/div/div[2]/div[1]').text
        ap3 = self.driver.find_element(By.XPATH, '//*[@id="lid-16576264"]/div/div/div[2]/div[1]').text
        ap4 = self.driver.find_element(By.XPATH, '//*[@id="lid-3634539"]/div/div/div[2]/div[1]').text
        ap5 = self.driver.find_element(By.XPATH, '//*[@id="lid-1794071"]/div/div/div[2]/div[1]').text
        ap6 = self.driver.find_element(By.XPATH, '//*[@id="lid-4740434"]/div/div/div[2]/div[1]').text
        ap7 = self.driver.find_element(By.XPATH, '//*[@id="lid-2992351"]/div/div/div[2]/div[1]').text
        ap8 = self.driver.find_element(By.XPATH, '//*[@id="lid-7138423"]/div/div/div[2]/div[1]').text
        ap9 = self.driver.find_element(By.XPATH, '//*[@id="lid-7929629"]/div/div/div[2]/div[1]').text
        ap10 = self.driver.find_element(By.XPATH, '//*[@id="lid-30960290"]/div/div/div[2]/div[1]').text

        print("ap1: " + ap1)
        print("ap2: " + ap2)
        print("ap3: " + ap3)
        print("ap4: " + ap4)
        print("ap5: " + ap5)
        print("ap6: " + ap6)
        print("ap7: " + ap7)
        print("ap8: " + ap8)
        print("ap9: " + ap9)
        print("ap10: " + ap10)

        time.sleep(4)

        dados = ap1 + ';' + ap2 + ';' + ap3 + ';' + ap4 + ';' + ap5 + ';' + ap6 + ';' + ap7 + ';' + ap8 + ';' + ap9 + ';' + ap10

        arquivo = open("Apartamentos.txt", "a")
        arquivo.write(f"Apartamentos: {dados}\r\n")
        arquivo.close()