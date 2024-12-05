from selenium import webdriver  
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import requests
import time

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

# Navigate to the website
driver.get("https://bug-free-space-engine-p454g5pvv672v5x-5500.app.github.dev/testing_automatizado/selenium/mi_app/")
#'https://bug-free-space-engine-p454g5pvv672v5x-5500.app.github.dev/testing_automatizado/selenium/mi_app/'


btnVerde = driver.find_element(By.CSS_SELECTOR, "button")
btnVerde.click()
# barraBusqueda.send_keys('gatitos')

input1 = driver.find_element(By.CSS_SELECTOR, "input[name=input1]")
input2 = driver.find_element(By.CSS_SELECTOR, "input[name=input2]")
input3 = driver.find_element(By.CSS_SELECTOR, "input[name=input3]")
btnSend = driver.find_element(By.CSS_SELECTOR, "button")

input1.send_keys('prueba')
input2.send_keys('desde')
input3.send_keys('selenium')

btnSend.click()
time.sleep(5)


URL = "https://script.googleusercontent.com/a/macros/bue.edu.ar/echo?user_content_key=gSJq4NM5YTCNg6X_vA9EsP3gF91Eh_MVHIHuYcnKlAvpqSBxCbRNMTX6GFo49boe44TuLtjbttgkkikkEtgO5DDyPOKop15Tm5_BxDlH2jW0nuo2oDemN9CCS2h10ox_nRPgeZU6HP-l9kxtB6Zv6Rg5HV17pdFHIXwdiqqDuQ6uOM6-w0ekJm5zl5rj3IOcmRpJ-z-NwVg17aSgdyI6I57PwO6HsbhVSC6q_IG2qOYs-gmwK503QntQxHsjENiWXMuqa_jo9BU&lib=Me3sC7WyOdonTC16vylGQfnz7im5tOETb"
r = requests.get(url = URL)
data = r.json()
print(data)

valores = data[-1]
assert valores[0] == 'prueba'
assert valores[1] == 'desde'
assert valores[2] == 'selenium'


# barraBusqueda.send_keys('gatitos', Keys.ENTER)
# driver.find_element(By.ID, "submit").click()

input('')  # frena el programa hasta que se ingrese algún texto en la consola
        #evita que se cierre el navegador

driver.quit()   # cierra el navegador