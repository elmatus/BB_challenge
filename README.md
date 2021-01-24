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

Inicialmente se revisaron las 4 plataformas y se llegó a la conclusión que la única que ofrece su catálogo completo de forma gratuita y sin tener que iniciar sesión es Acorn TV, por lo que se empezó por esta. Por medio de la biblioteca Beautiful Soup se logró obtener en un archivo CSV el título, URL, sinópsis y tipo de cada película y serie de la plataforma. Las demás variables no se indican en esta plataforma. El script en Python, correspondiente a 
