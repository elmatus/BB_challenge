from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# Pasos para usar selenium:
# 1) pip install selenium
# 2) Descargar el driver para chrome e incluirlo en la misma carpeta que este archivo 
#	 https://sites.google.com/a/chromium.org/chromedriver/downloads

import time
import csv 
import getpass

import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup 

#################################################################################
# Funcion para ir al final de la pagina:
def scroll_down_to_end ():

	# Get scroll height.
	last_height = driver.execute_script("return document.body.scrollHeight")

	while True:

	    # Desplazarse hacia abajo al final de la pagina:
	    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
	    time.sleep(2)

	    # Calculo la altura del nuevo "scroll" y lo comparo con el anterior:
	    new_height = driver.execute_script("return document.body.scrollHeight")

	    if new_height == last_height:
	        break
	    # Actualizo altura:
	    last_height = new_height
	return
#################################################################################

# Funcion para obtener los titulos de peliculas/series:
def get_title(title_type, titles_list):
	# Obtengo todos los titulos:
	titles = driver.find_elements_by_class_name("fallback-text")

	for title in titles:

		# Imprimo en la terminal el titulo y el tipo:
		print("Title: " + title.text + " | Type: " + title_type)

		# Escibo los valores obtenidos en una lista:
		title = [title.text.replace(",", "."), title_type]
		titles_list.append(title)
	return
#################################################################################

PATH = ".\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.netflix.com/ar/login")

# Tomo los datos de usuario:
login_user = driver.find_element_by_name("userLoginId")
print("Ingrese su usuario de Netflix:")
user_str = input()
login_user.send_keys(user_str)

time.sleep(1) # Espera 1 segundo

# Tomo los datos de la contraseña:
password = driver.find_element_by_name("password")
password_str = getpass.getpass(prompt="Ingrese su contraseña:")
password.send_keys(password_str)

time.sleep(2) 

# Iniciar sesion:
sign_in = driver.find_element_by_css_selector(".btn.login-button.btn-submit.btn-small")
sign_in.click()
time.sleep(2) 

# Usuario que esta mirando:
print("Ingrese quien esta mirando:")
user_watching = input()
user_button = driver.find_element_by_link_text(user_watching)
user_button.click()
time.sleep(2)

titles = []

# Me muevo al catalogo completo de peliculas:
driver.get("https://www.netflix.com/browse/genre/34399?so=az")
scroll_down_to_end()
get_title("movie", titles)
 
# Me muevo al catalogo completo de series:
driver.get("https://www.netflix.com/browse/genre/83?so=az")
scroll_down_to_end()
get_title("serie", titles)

filename = "netflix_catalogue.csv"
csv_headers = ["Title", "Type"]

# Escibo los valores obtenidos en el archivo csv:
with open(filename, "w", encoding="utf-8", newline='') as f: 
	#f.write(csv_headers)
	write = csv.writer(f) 
	write.writerow(csv_headers) 
	write.writerows(titles) 

driver.quit()
