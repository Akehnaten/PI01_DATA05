from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from dataframe import amazon_prime, disney_plus, hulu, netflix

app = FastAPI()

@app.get('/', response_class=HTMLResponse)
async def mensaje():

        bienvenida = """<html lang="en">
<head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Data Science - PI laboratorio número 1</title>
        <script type="text/javascript">
                function max_duration(){
                        url = 'http://pi01-data05-prod-akenahten-lub9dl.mo4.mogenius.io:80/get_max_duration(' + document.getElementById("anio").value + ', ' + document.getElementById("plataforma").value + ', ' + document.getElementById("unidad").value + ')'
                window.open(url, '_blank');}

                function count_plataform(){
                        url = 'http://pi01-data05-prod-akenahten-lub9dl.mo4.mogenius.io:80/get_count_plataform(' + document.getElementById("plataforma2").value + ')'
                window.open(url, '_blank');}

                function listedin(){
                        url = 'http://pi01-data05-prod-akenahten-lub9dl.mo4.mogenius.io:80/get_listedin(' + document.getElementById("genero").value + ')'
                window.open(url, '_blank');}

                function actor(){
                        url = 'http://pi01-data05-prod-akenahten-lub9dl.mo4.mogenius.io:80/get_actor(' + document.getElementById("plataforma4").value + ', ' + document.getElementById("anio4").value + ')'
                window.open(url, '_blank');}
        </script>

        <style>
        body {  background-color: #22272e;
                font-family: verdana;
                font-size: 75%;}
        h1   {  color: #cdd9e5;
                font-family: verdana;
                font-size: 250%;}
        h3   {  color: #539bf5;
                font-family: verdana;
                font-size: 100%;}
        p    {  color: #cdd9e5;
                font-family: verdana;
                font-size: 100%;}
        a    {  display: block;
                width: 130px;
                font-family: verdana
                font-weight: 700;
                background-color: #AD0306;
                border-radius:10px;
                color: #cdd9e5;
                text-decoration: none;
                margin: 15px 20px}
        a:hover {background-color: transparent;
                border: 2px solid #539bf5
                color: #539bf5}
        </style>
</head>
<body>  
        <h1><center>Data Science - PI laboratorio número 1 </center></h1>
        <br>
        <br>
        <br>
        <br>
        
        <p>Bienvenido a mi proyecto individual, mi nombre es ronal cabrera y aquí te enseñaré a navegar dentro del sitio:</p>
        <br>
        <p>• Para buscar la película/serie de mayor duración dentro de la plataforma correspondiente:</p>
        <form>
        <p>Año: <input type="text" name="año" id="anio" size="2" maxlength="4">
        Plataforma:     <select name="plataforma" id="plataforma">
                        <option>amazon_prime</option>
                        <option>disney_plus</option>
                        <option>hulu</option>
                        <option>netflix</option>
                        </select>
        Medida de duración:     <select name="unidad" id="unidad">
                                <option>min</option>
                                <option>season</option>
                                </select>
        </p>
        </form>
        <a href="" onclick="max_duration()" target="_blank"> <center> Get_max_duration </center> </a>
        <h3>/get_max_duration(año, plataforma, [min/season según corresponda película/serie])</h3>
        <h3> IMPORTANTE: usar espacio luego de cada coma!!!</h3>
        <br>
        <br>
        
        <p>• Para averiguar la cantidad de películas/series a disposición en cada plataforma:</p>
        <form>
        <p>Plataforma:  <select name="plataforma" id="plataforma2">
                                <option>amazon_prime</option>
                                <option>disney_plus</option>
                                <option>hulu</option>
                                <option>netflix</option>
                        </select>
        </p>
        </form>
        <a href="" onclick="count_plataform()" target="_blank"> <center> Get_count_plataform </center> </a>
        <h3>/get_count_plataform(plataforma)</h3>
        <br>
        <br>

        <p>• Para ver cuantas veces se repite cierto género en los catálogos, y ver dentro de que plataforma hay mas variedad:</p>
        <form>
        <p>Género: <input type="text" name="genero" id="genero" size="10">
        </p>
        </form>
        <a href="" onclick="listedin()" target="_blank"> <center>Get_listedin</center> </a>
        <h3>/get_listedin(genero)</h3>
        <h3>IMPORTANTE: recuerde que dentro de netflix el género comedia se encuentra como Comedies!!!</h3>
        <br>
        <br>
        
        <p>• Para ver cual es el actor que mas podes encontrar dentro de la plataforma en cierto año:</p>
        <form>
        <p>Año: <input type="text" name="año" id="anio4" size="2" maxlength="4">
        Plataforma:     <select name="plataforma" id="plataforma4">
                                <option>amazon_prime</option>
                                <option>disney_plus</option>
                                <option>hulu</option>
                                <option>netflix</option>
                        </select>
        </p>
        </form>
        <a href="" onclick="actor()" target="_blank"> <center>Get_actor</center> </a>
        <h3>/get_actor(plataforma, año)</h3>
        <h3>IMPORTANTE: usar espacio luego de cada coma!!!</h3>

        """
        return bienvenida

@app.get("/get_max_duration({anio}, {plataforma}, {tipo})")
async def duracion(anio:int, plataforma:str, tipo:str):
        
        # Normalizo las variables por se se ingresó en mayúscula
        plataforma = plataforma.lower().strip()
        tipo = tipo.lower().strip()
        
        if (tipo == 'season'):
                unidad = 'temporada/s'
                if plataforma == 'amazon_prime':
                        resultado = amazon_prime[(amazon_prime['type'] == 'TV Show') & (amazon_prime['release_year'] == anio)]['duration'].max()
                elif plataforma == 'disney_plus':
                        resultado = disney_plus[(disney_plus['type'] == 'TV Show') & (disney_plus['release_year'] == anio)]['duration'].max()
                elif plataforma == 'hulu':
                        resultado = hulu[(hulu['type'] == 'TV Show') & (hulu['release_year'] == anio)]['duration'].max()
                elif plataforma == 'netflix':
                        resultado = netflix[(netflix['type'] == 'TV Show') & (netflix['release_year'] == anio)]['duration'].max()
                    
        elif (tipo == 'min'):
                unidad = 'minutos'
                if plataforma == 'amazon_prime':
                        resultado = amazon_prime[(amazon_prime['type'] == 'Movie') & (amazon_prime['release_year'] == anio)]['duration'].max()
                elif plataforma == 'disney_plus':
                        resultado = disney_plus[(disney_plus['type'] == 'Movie') & (disney_plus['release_year'] == anio)]['duration'].max()
                elif plataforma == 'hulu':
                        resultado = hulu[(hulu['type'] == 'Movie') & (hulu['release_year'] == anio)]['duration'].max()
                elif plataforma == 'netflix':
                        resultado = netflix[(netflix['type'] == 'Movie') & (netflix['release_year'] == anio)]['duration'].max()                   


        return f"La duración máxima fue de {resultado} {unidad}, en el año {anio} mediante la plataforma {plataforma}."

@app.get("/get_count_plataform({plataforma})")
async def inventario(plataforma:str):

        # Normalizo las variables por se se ingresó en mayúscula
        plataforma = plataforma.lower().strip()

        if (plataforma == 'amazon_prime'):
                peliculas = amazon_prime[amazon_prime['type'] == 'Movie']['title'].count()
                series = amazon_prime[amazon_prime['type'] == 'TV Show']['title'].count()
        elif (plataforma == 'disney_plus'):
                peliculas = disney_plus[disney_plus['type'] == 'Movie']['title'].count()
                series = disney_plus[disney_plus['type'] == 'TV Show']['title'].count()
        elif (plataforma == 'hulu'):
                peliculas = hulu[hulu['type'] == 'Movie']['title'].count()
                series = hulu[hulu['type'] == 'TV Show']['title'].count()
        elif (plataforma == 'netflix'):
                peliculas = netflix[netflix['type'] == 'Movie']['title'].count()
                series = netflix[netflix['type'] == 'TV Show']['title'].count()

        return f"La plataforma {plataforma} posee un inventario de {peliculas} películas y {series} series."


@app.get("/get_listedin({genero})")
async def generos(genero:str):

        # Normalizo las variables por se se ingresó en mayúscula
        genero = genero.lower().strip()

        g_amazon = amazon_prime[amazon_prime['listed_in'].str.contains(genero, case=False)]['title'].count()
        g_disney = disney_plus[disney_plus['listed_in'].str.contains(genero, case=False)]['title'].count()
        g_hulu = hulu[hulu['listed_in'].str.contains(genero, case=False)]['title'].count()
        g_netflix = netflix[netflix['listed_in'].str.contains(genero, case=False)]['title'].count()

        total = g_amazon + g_disney + g_hulu + g_netflix

        mayor_frecuencia = ''
        max_repeticiones =0
        if g_amazon > max_repeticiones:
                max_repeticiones = g_amazon
                mayor_frecuencia = 'amazon_prime'
        if g_disney > max_repeticiones:
                max_repeticiones = g_disney
                mayor_frecuencia = 'disney_plus'
        if g_hulu > max_repeticiones:
                max_repeticiones = g_hulu
                mayor_frecuencia = 'hulu'
        if g_netflix > max_repeticiones:
                max_repeticiones = g_netflix
                mayor_frecuencia = 'netflix'


        return f"El género {genero} se repite unas {total} veces. La plataforma {mayor_frecuencia} es donde se presentan con mas frecuencia ({max_repeticiones} veces)"


@app.get("/get_actor({plataforma}, {anio})")
async def generos(plataforma:str, anio:int):

        # Normalizo las variables por se se ingresó en mayúscula
        plataforma = plataforma.lower().strip()

        # paso a lista la serie correspondiente
        if plataforma == 'amazon_prime':
                list = amazon_prime[amazon_prime['release_year'] == anio]['cast'].tolist()
        elif plataforma == 'disney_plus':
                list = disney_plus[disney_plus['release_year'] == anio]['cast'].tolist()
        elif plataforma == 'hulu':
                list = hulu[hulu['release_year'] == anio]['cast'].tolist()
        elif plataforma == 'netflix':
                list = netflix[netflix['release_year'] == anio]['cast'].tolist()        
        
        # Separo los actores de la lista en la que estaban, no cuento los null!!
        list_final = []

        for i in range(len(list)):
                aux = list[i].split(',')
                for z in range(len(aux)):
                        if (aux[z] != 'Sin datos'):
                                list_final.append(aux[z])

        resultado = max(set(list_final), key = list_final.count)

        return f"El actor/actriz que más aparece en {anio} es {resultado}, dentro de la plataforma {plataforma}"                        