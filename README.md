<div id="top"></div>

<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/Tipologia-y-Ciclo-de-Vida-de-los-Datos/Practica1-Web_Scraping">
    <img src="https://user-images.githubusercontent.com/57969201/232225800-5c7ecb7a-3f55-47cc-bd46-a94e17dfe6e2.png" alt="Logo" width="390" height="120">
  </a>
  

<h1 align="center">Práctica 1 - Web Scraping</h3>

  <p align="center">
    En esta práctica se ha llevado a cabo un caso práctico de Web Scraping, orientado a identificar y extraer datos relevantes del dominio <a href="https://www.expatistan.com/cost-of-living">Expatistan</a>. Esta <i>webpage</i> nos muestra los costes de vida por <b>países</b> y <b>ciudades</b> en un formato de <i>Ranking</i>, es decir, del que mayor costes prensenta hasta el país o ciudad donde vivir es más barato.
    </br></br>
    Partiendo de la premisa del <i>webpage</i> y que cada país/ciudad tiene sus gastos divididos en categorías y elementos, esta página nos abre un mundo entero para realizar análisis estadístico de los costes de vida y concluir  
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>ÍNDICE</summary>
  <ol>
    <li>
      <a href="#sobre-el-proyecto">Sobre el proyecto</a>
      <ul>
        <li><a href="#herramientas-utilizadas">Herramientas utilizadas</a></li>
      </ul>
    </li>
    <li>
      <a href="#inicio-del-proyecto">Incio del proyecto</a>
      <ul>
        <li><a href="#requisitos-previos">Requisitos previos</a></li>
        <li><a href="#instalaciones">Instalaciones</a></li>
      </ul>
    </li>
    <li><a href="#licencia">Licencia del Dataset</a></li>
    <li><a href="#contactos">Contactos</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## Sobre el proyecto
<div align="center">
<a href="https://www.expatistan.com/cost-of-living/index?ranking=1">
    <img src="https://user-images.githubusercontent.com/57969201/232224215-296bb7d1-10bb-4db9-b3b8-bdf1da25453c.png" alt="Page" width="670" height="580">
  </a>
</div>
Expatistan es un <i>webpage</i> que nos ofrece una forma sencilla, intiutiva y eficaz de visualizar el coste de vida por ciudades y países. Además, también se pueden hacer comparativas entre ellos y cálcular tu salarios aproximado por ciudad actual y ciudad de destino. </br></br>

Par este proyecto nos centraremos en extraer los datos que hacer referencia a cada ciudad y país explicados por la página web. De ahí que en el repositorio hayan dos datasets extraídos: `cost_of_living_cities.csv` y `cost_of_living_countries.csv`. Como dicen sus nombres, cada uno corresponde al tipo de Web Scraping realizado en la página web y contendrán los siguinetes valores. 

| cost_of_living_cities.csv  | cost_of_living_countries.csv | Explicación                                                                                      |
| -------------------------- | ---------------------------- | ------------------------------------------------------------------------------------------------ |
| Ranking position           | Ranking position             | Posición numérica del país o ciudad en el Raking de la web                                       |
| Country                    | Country                      | Nombre del país de originen de la ciudad o país al que se le hace el Web Scraping respectivamente|
| City                       | (No presenta esta columna)   | Nombre de la ciudad a la que se le está aplicando el Web Scraping                                |
| State                      | (No presenta esta columna)   | Nombre del estado, si lo presenta, de la ciudad a la que se le está aplicando el Web Scraping    |
| Category                   | Category                     | Nombre de la clasificación genérica que se le ha otorgado a un conjunto de `items`               |
| Items                      | Items                        | Objetos o servicioscuyos precios nos sirven para estimar el coste de vida por país o ciudad      |
| Original Currency          | Original Currency            | Nombre de la moneda usada por el país o ciudad a los que se ha aplicado el Web Scraping          |
| Original Currency Value    | Original Currency Value      | Valor de la moneda usada por el país o ciudad a los que se ha aplicado el Web Scraping           |
| Exchanged Currency         | Exchanged Currency           | Nombre de la moneda usada para el cambio de divisa                                               |
| Exchanged Currency Value   | Exchanged Currency Value     | Valor de la moneda usada para el cambio de divisa                                                |

</br></br>
Estos CSV se consiguen a partir del código explicado en el Jupyter notebook `Scraping-notebook.ipynb`, que contiene una pequeña introducción a la página web y el Web Scraping de Ciudades (clase `ExpatistanCityScraper()`) y de Países (clase `ExpatistanCountryScraper()`).

Por otro lado, tenemos un archivo `utils.py` que contiene todas las funciones comunes a ambos Web Scrapings. Este fichero nos ahorrará tener código duplicado o con minimos cambios en ambas clases `ExpatistanCountryScraper()` y `ExpatistanCityScraper()`, haciendo que el notebook esté mejor optimizado y limpio.



<p align="right">(<a href="#top">back to top</a>)</p>



### Herramientas y Librerías utilizadas

* [Jupyter Notebook](https://jupyter.org/)
* [Requests](https://pypi.org/project/requests/)
* [Buildwith](https://pypi.org/project/builtwith/)
* [BeautifulSoup4](https://pypi.org/project/beautifulsoup4/)
* [Python-whois](https://pypi.org/project/python-whois/)
* Re
* [Pandas](https://pypi.org/project/pandas/)
* [Session-info](https://pypi.org/project/session-info/)

<p align="right">(<a href="#top">back to top</a>)</p>


### Requisitos previos

1. Tener instalado Jupyter Notebook en local o una cuenta de alguna plataforma de servicio Cloud con python notebooks habilitados (Google Colab, Kaggle, etc.)
2. Tener python instalado en la máquina si se quiere usar el notebook en local.
3. Tener las siguientes librerías instaladas (ver siguiente apartado).

### Instalaciones

1. Descargar la version gratis del IDE [Jupyter Notebook](https://jupyter.org/install)
2. Descarga el repositorio en tu máquina o clonalo
   ```sh
   git clone https://github.com/Tipologia-y-Ciclo-de-Vida-de-los-Datos/Practica1-Web_Scraping
   ```
   <div align="center">
    <a href="https://github.com/Tipologia-y-Ciclo-de-Vida-de-los-Datos/Practica1-Web_Scraping">
      <img src="https://user-images.githubusercontent.com/57969201/232225560-96300869-907b-4e7a-8077-ee8165909db4.png" alt="download" width="380" height="390">
    </a>
   </div>
3. Instala `python`, si no lo tienes en tu máquina, desde Microsoft Store y comprueba su instalación en PowerShell 
   ```sh
   Python --version
   ```
4. Abre el IDE Jupyter Notebook y navega entre los directorios hasta donde tengas guardado el notebook
5. Abre el notebook `Scraping-notebook`
6. Recomendamos ejecutar el apartado `1.1 Installations`auque se crea que la máquina tiene todas las librerías
```sh
!pip install requests
!pip install builtwith
!pip install beautifulsoup4
!pip install python-whois
```
7. Importar las librerías y el archivo `utils.py`
8. Notebook preparado para realizar el scraping.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- LICENSE -->
## Licencia

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTACT -->
## Contactos
Este proyecto ha sido llevado a cabo por:
1. José Luis Santos Durango
2. María Isabel González Sánchez
Contáctanos: [Miembros del equipo](https://github.com/Tipologia-y-Ciclo-de-Vida-de-los-Datos/Practica1-Web_Scraping/graphs/contributors)]


<p align="right">(<a href="#top">back to top</a>)</p>





<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/Tipologia-y-Ciclo-de-Vida-de-los-Datos/Practica1-Web_Scraping.svg?style=for-the-badge
[contributors-url]: https://github.com/Tipologia-y-Ciclo-de-Vida-de-los-Datos/Practica1-Web_Scraping/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Tipologia-y-Ciclo-de-Vida-de-los-Datos/Practica1-Web_Scraping.svg?style=for-the-badge
[forks-url]: https://github.com/Tipologia-y-Ciclo-de-Vida-de-los-Datos/Practica1-Web_Scraping/network/members
[stars-shield]: https://img.shields.io/github/stars/Tipologia-y-Ciclo-de-Vida-de-los-Datos/Practica1-Web_Scraping.svg?style=for-the-badge
[stars-url]: https://github.com/Tipologia-y-Ciclo-de-Vida-de-los-Datos/Practica1-Web_Scraping/stargazers
[issues-shield]: https://img.shields.io/github/issues/Tipologia-y-Ciclo-de-Vida-de-los-Datos/Practica1-Web_Scraping.svg?style=for-the-badge
[issues-url]: https://github.com/Tipologia-y-Ciclo-de-Vida-de-los-Datos/Practica1-Web_Scraping/issues
[license-shield]: https://img.shields.io/github/license/Tipologia-y-Ciclo-de-Vida-de-los-Datos/Practica1-Web_Scraping.svg?style=for-the-badge
[license-url]: https://github.com/Tipologia-y-Ciclo-de-Vida-de-los-Datos/Practica1-Web_Scraping/blob/master/LICENSE.txt
