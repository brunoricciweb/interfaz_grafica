from selenium import webdriver, Keys

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

# Navigate to the website
driver.get("https://www.google.com")
#'https://bug-free-space-engine-p454g5pvv672v5x-5500.app.github.dev/testing_automatizado/selenium/mi_app/'


barraBusqueda = driver.find_element(By.CSS_SELECTOR, "textarea")
barraBusqueda.send_keys('gatitos')

# barraBusqueda.send_keys('gatitos', Keys.ENTER)
# driver.find_element(By.ID, "submit").click()

input('')  // frena el programa hasta que se ingrese algún texto en la consola
            //evita que se cierre el navegador

driver.quit()   // cierra el navegador