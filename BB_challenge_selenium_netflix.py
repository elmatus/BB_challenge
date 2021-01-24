from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup 

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.netflix.com/ar/login")

login_user = driver.find_element_by_name("userLoginId")
password = driver.find_element_by_name("password")

print("Ingrese su usuario de Netflix:")
user_str = input()
login_user.send_keys(user_str)

time.sleep(1) # Espera 1 segundo

print("Ingrese su contraseña:")
password_str = input()
password.send_keys(password_str)

time.sleep(2) 

sign_in = driver.find_element_by_css_selector(".btn.login-button.btn-submit.btn-small")
sign_in.click()
time.sleep(2) 

print("Ingrese quien esta mirando:")
user_watching = input()

user_button = driver.find_element_by_link_text(user_watching)
user_button.click()
time.sleep(2)

'''
movie_button = driver.find_element_by_link_text("Movies")
movie_button.click()
time.sleep(1)

order_movies = driver.find_element_by_class_name("aro-grid-toggle")
sign_in.click()
time.sleep(1)

order_movies = driver.find_element_by_link_text("SUGGESTIONS FOR YOU")
order_movies.click()
time.sleep(1)

order_movies_a_z = driver.find_element_by_link_text("A-Z")
order_movies_a_z.click()
time.sleep(1)
'''

# Me muevo al catalogo completo de peliculas:
driver.get("https://www.netflix.com/browse/genre/34399?so=az")

movie_titles = driver.find_elements_by_class_name("ptrack-content")
print(movie_titles)

#for movie_title in movie_titles:
#	movie = movie_title.a['aria-label']
#	print(movie)
'''
for m in range(movie_titles):
	movie = movie_titles.get(m).getAttribute("value"))
'''




'''
netflix_movies_url = "https://www.netflix.com/browse/genre/34399?so=az"

# Abro la conexion y obtengo la pagina HTML:
uClient = uReq(netflix_movies_url)
page_html = uClient.read()
uClient.close()

# Parseo el codigo HTML:
page_soup = soup(page_html, "html.parser")



# Obtengo cada pelicula/serie:
#title_container = page_soup.findAll("div", {"class":"title-card-container"})
title_container = page_soup.findAll("div", {"class":"ptrack-content"})

print("----------------------------------------------------")
print(title_container)
print("----------------------------------------------------")



filename = "netflix_catalogue.csv"

csv_headers = "Title, URL\n"
#csv_headers = "Title, Year, Director, Cast, URL, Synopsis, Genre, Type, Age rating, Number of seasons, Duration\n"

with open(filename, "w", encoding="utf-8") as f: 
	f.write(csv_headers)

	for title in title_container:
		# Obtengo el nombre del titulo:
		title_name = title.a['aria-label']
		# Obtengo la URL:
		title_url_watch = title.a['href']

		# Imprimo en la terminal algunos valores:
		print("Title: " + title_name + " | URL:" + title_url_watch)

		# Escibo los valores obtenidos en el archivo csv:
		f.write(title_name.replace(",", ".") + "," + title_url_watch + "\n")
'''

#driver.quit()