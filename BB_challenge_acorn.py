import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup 

acorn_url = "https://acorn.tv/browse/all/"

# Abro la conexion y obtengo la pagina HTML:
uClient = uReq(acorn_url)
page_html = uClient.read()
uClient.close()

# Parseo el codigo HTML:
page_soup = soup(page_html, "html.parser")

# Obtengo cada pelicula/serie:
title_container = page_soup.findAll("div", {"class":"col-sm-6 col-md-6 col-lg-3"})

# Archivo donde se guardaran los datos:
filename = "acorn_catalogue.csv"
csv_headers = "Title, Type, URL, Synopsis\n"

# Abro de esta manera el archivo, ya que en la sinopsis de una pelicula aparecia
# un caracter que no podia imprimir, lo cual llevaba a un error. 
with open(filename, "w", encoding="utf-8") as f: 
	f.write(csv_headers)

	for title in title_container:
		# Obtengo el nombre del titulo:
		title_name = title.a.img['title']
		# Obtengo la URL:
		title_url = title.a['href']

		# Abro una conexion y obtengo el HTML de un titulo:
		uClient = uReq(title_url)
		title_html = uClient.read()
		uClient.close()

		# Obtengo la descripcion del titulo:
		title_soup = soup(title_html, "html.parser")
		title_synopsis = title_soup.find("p", {"itemprop":"description"})

		# Si el numero de episodios y temporadas es 1, lo considero como una pelicula:
		num_episodes = title_soup.find("meta", {"itemprop":"numberOfEpisodes"})
		num_seasons = title_soup.find("meta", {"itemprop":"numberOfSeasons"})
		if num_episodes['content'] == "1" and num_seasons['content'] == "1":
			title_type = "movie"
		else:
			title_type = "serie"

		# Imprimo en la terminal algunos valores:
		print("title: " + title_name + " | url: " + title_url + " | type: " + title_type)

		# Escibo los valores obtenidos en el archivo csv:
		f.write( title_name.replace(",", ".") + "," + 
				 title_type + "," + 
				 title_url + "," + 
				 title_synopsis.text.replace(",", ".") + "\n")
				 # Tuve que reemplazar las "," de los titulos y la sinopsis por ".", ya que el archivo 
				 # se separa por medio de estos caracteres
