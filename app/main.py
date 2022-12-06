from fastapi import FastAPI
from dataframe import amazon_prime, disney_plus, hulu, netflix

app = FastAPI()

@app.get("/")
async def index():
        return {"Hola bb":"dame dinero"}

@app.get("/get_max_duration({anio},{plataforma},{tipo})")
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
async def generos( genero:str ):

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


@app.get("/get_actor({plataforma},{anio})")
async def generos( plataforma:str, anio: int ):

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