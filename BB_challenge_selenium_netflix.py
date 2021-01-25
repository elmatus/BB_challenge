from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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

	    # Scroll down to the bottom.
	    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

	    # Wait to load the page.
	    time.sleep(2)

	    # Calculate new scroll height and compare with last scroll height.
	    new_height = driver.execute_script("return document.body.scrollHeight")

	    if new_height == last_height:

	        break

	    last_height = new_height
	return
#################################################################################
# Funcion para obtener los titulos de peliculas/series:
def get_title(title_type, titles_list):

	titles = driver.find_elements_by_class_name("fallback-text")

	for title in titles:

		# Imprimo en la terminal algunos valores:
		print("Title: " + title.text + " | Type: " + title_type)

		# Escibo los valores obtenidos en una lista:
		title = [title.text.replace(",", "."), title_type]
		titles_list.append(title)
	return
#################################################################################

PATH = "C:\Program Files (x86)\chromedriver.exe"
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
#print("Ingrese su contraseña:")
password_str = getpass.getpass(prompt="Ingrese su contraseña:")
#password_str = input()
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
