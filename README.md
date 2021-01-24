# BB Challenge

Desafío: Obtener el catálogo completo de películas y series por medio de web scraping de alguna de las siguientes plataformas:

* [Amazon Prime Video](https://www.primevideo.com/)
* [Netflix](https://www.netflix.com/ar-en/)
* [Clarovideo](https://www.clarovideo.com/argentina/homeuser)
* [Acorn TV](https://acorn.tv/)

Las variables a obtener de cada título son las siguientes:

* Título
* Año
* Directores
* Actores
* Link
* Descripción
* Géneros
* Rating
* Tipo (serie/película)

Inicialmente se revisaron las 4 plataformas y se llegó a la conclusión que la única que ofrece su catálogo completo de forma gratuita y sin tener que iniciar sesión es [Acorn TV](https://acorn.tv/), por lo que se empezó por esta. Por medio de la biblioteca Beautiful Soup se logró obtener en un archivo CSV el título, URL, sinópsis y tipo de cada película y serie de la plataforma. Las demás variables no se indican en esta plataforma. El script en Python, correspondiente a esta plataforma es [BB_challenge_acorn.py](https://github.com/elmatus/BB_challenge/BB_challenge_acorn.py). Además el CSV obtenido luego de ejecutar dicho script es [acorn_catalogue.csv](https://github.com/elmatus/BB_challenge/acorn_catalogue.csv).

Luego se optó por seguir con la plataforma [Netflix](https://www.netflix.com/ar-en/). Se intentó aplicar el mismo procedimiento que para la plataforma anterior, pero al querer obtener los datos de su [catálogo completo de películas](https://www.netflix.com/browse/genre/34399?so=az), el resultado era vació, ya que es necesario iniciar sesión para poder visualizarlo. Entonces, para realizar unas pruebas iniciales se realizó el web scraping de los [títulos gratuitos de Netflix](https://www.netflix.com/ar/watch-free). Si bien cuenta únicamente con 7 títulos para visualizar sin iniciar sesión, esto luego se podría extender al momento de obtener el catálogo completo. Es código correspondiente a esta prueba es [BB_challenge_netflix_watch_free.py](https://github.com/elmatus/BB_challenge/BB_challenge_netflix_watch_free.py) y su CSV correspondiente es [netflix_watch_free_catalogue.csv](https://github.com/elmatus/BB_challenge/netflix_watch_free_catalogue.csv).

Finalmente, se buscó información sobre el entorno Selenium, para poder iniciar sesión en [Netflix](https://www.netflix.com/ar-en/) y de esta manera obtener su catálogo completo. La idea sería iniciar sesión desde una terminal, para poder visualizar el catálogo completo de series y películas y luego guardar estos datos en un archivo CSV.  Hasta el momento se logró iniciar sesión desde una terminal y redirigirse al catálogo completo de películas (https://www.netflix.com/browse/genre/34399?so=az) utilizando Selenium, pero no se pudieron obtener los datos requeridos. 
