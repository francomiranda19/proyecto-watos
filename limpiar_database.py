import pandas as pd

pokemon_original = pd.read_csv("pokemon_database_original.csv", encoding="UTF-8") # Se importa la base de datos original
nombres = pokemon_original.columns.values # Nombres de las columnas
nulos = pokemon_original.isnull().sum() # Nulos por columnas

columnas_a_borrar = []
for i in range(pokemon_original.shape[1]):
    if nulos[i] > 0: # Si hay nulos en cierta columna, se elimina esa columna
        columnas_a_borrar.append(nombres[i])
pokemon = pokemon_original.drop(columnas_a_borrar, axis=1) # Nueva base de datos sin nulos

nombres = pokemon.columns.values
nuevas_columnas = {}
for i in range(len(nombres)):
    nuevo_nombre = nombres[i].replace(" ", "") # Se quitan los espacios de todos los nombres de columnas
    nuevo_nombre = nuevo_nombre.replace("(s)", "") # Particular para la columna llamada "Game(s)ofOrigin"
    nuevas_columnas[nombres[i]] = nuevo_nombre
pokemon.rename(columns=nuevas_columnas, inplace=True)

nombres_pokemon = list(pokemon["PokemonName"])
nuevos_nombres_pokemon = {}
for i in range(len(nombres_pokemon)): # Si un nombre contiene uno de los siguientes caracteres, se eliminará ese caracter
    nuevo_nombre = nombres_pokemon[i].replace(" ", "")
    nuevo_nombre = nuevo_nombre.replace(".", "")
    nuevo_nombre = nuevo_nombre.replace("'", "")
    nuevo_nombre = nuevo_nombre.replace("-", "")
    nuevo_nombre = nuevo_nombre.replace("(", "")
    nuevo_nombre = nuevo_nombre.replace(")", "")
    nuevos_nombres_pokemon[nombres_pokemon[i]] = nuevo_nombre
pokemon["PokemonName"] = pokemon["PokemonName"].map(nuevos_nombres_pokemon) # Se asigna la nueva columna con los nombres sin caracteres especiales

# Se elimina un pokemon inválido
tipo_nulo = pokemon[pokemon["PokemonName"] == "Type:Null"].index
pokemon = pokemon.drop(tipo_nulo)

RUTA = "tarql-1.2/bin"
pokemon.to_csv(f"{RUTA}/pokemon_database.csv", sep=',') # Se exporta la nueva base de datos como csv