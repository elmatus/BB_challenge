import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup 

netflix_url = "https://www.netflix.com/ar/watch-free"

# Abro la conexion y obtengo la pagina HTML:
uClient = uReq(netflix_url)
page_html = uClient.read()
uClient.close()

# Parseo el codigo HTML:
page_soup = soup(page_html, "html.parser")

# Obtengo cada pelicula/serie:
title_container = page_soup.findAll("div", {"class":"multi-title-card-item-content"})

filename = "netflix_watch_free_catalogue.csv"
csv_headers = "Title, Year, Director, Cast, URL, Synopsis, Genre, Type, Age rating, Number of seasons, Duration\n"

with open(filename, "w", encoding="utf-8") as f: 
	f.write(csv_headers)

	for title in title_container:
		# Obtengo el nombre del titulo:
		title_name = title.a.picture.img['alt']
		# URL para mirar el titulo:
		title_url_watch = title.a['href']
		title_url_watch = "netflix.com" + title_url_watch
		# URL para ver detalles del titulo:
		title_url_more = title.div.p.a['href']
		title_url_more = "https://www.netflix.com/ar-en" + title_url_more 

		# Abro una conexion y obtengo el HTML de un titulo:
		uClient = uReq(title_url_more)
		title_html = uClient.read()
		uClient.close()

		# Obtengo la descripcion del titulo:
		details_soup = soup(title_html, "html.parser")
		title_details = details_soup.find("div", {"class":"details-container"})

		# Año:
		year = details_soup.find("span", {"class":"title-info-metadata-item item-year"}).text
		
		# Director:
		if (details_soup.find("span", {"data-uia":"info-creators"}) != None):
			director = details_soup.find("span", {"data-uia":"info-creators"}).text
		else:
			director = "No data available"

		# Actores:
		cast = details_soup.find("span", {"data-uia":"info-starring"}).text

		# Sinopsis:
		synopsis = details_soup.find("div", {"class":"title-info-synopsis"}).text

		# Generos:
		genre = details_soup.find("a", {"data-uia":"item-genre"}).text
		if genre.find("Movie") == -1:
			title_type = "serie"
			seasons = details_soup.find("span", {"class":"test_dur_str"}).text
			duration = "-"
		else:
			title_type = "movie"
			seasons = "-"
			duration = details_soup.find("span", {"class":"duration"}).text

		# Clasificacion de edad:
		age_rating = details_soup.find("span", {"class":"maturity-number"}).text


		# Imprimo en la terminal algunos valores:
		print("title: " + title_name + " | year: " + year + " | director: " + director)

		# Escibo los valores obtenidos en el archivo csv:
		f.write(title_name.replace(",", ".") + "," + 
				year + "," + 
				director.replace(",", " | ") + "," + 
				cast.replace(",", " | ") + "," + 
				title_url_watch + "," + 
				synopsis.replace(",", ".") + "," + 
				genre.replace(",", " | ") + "," + 
				title_type + "," + 
				age_rating + "," +
				seasons + "," +
				duration + "\n")
