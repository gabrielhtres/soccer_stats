from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

url = 'https://www.sofascore.com/pt/jogador/everton-ribeiro/145063'

chrome_options = Options()
chrome_options.add_argument("--headless")  # Modo headless: sem interface gráfica
chrome_options.add_argument("--window-size=1200,800")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get(url)
stats_box = driver.find_element('xpath', '/html/body/div[1]/main/div[2]/div/div[2]/div[1]/div[3]/div[2]/div[2]/div/div[2]/div[1]/div[1]')

print(driver.title)
driver.quit()