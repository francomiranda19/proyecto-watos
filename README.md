# proyecto-watos
Proyecto del curso CC7220

Para transformar la base de datos a RDF:

En la carpeta **tarql-1.2/bin** ejecutar (en Ubuntu):
```
sh tarql --ntriples pokemon.sparql pokemon_database.csv
```

Si se quiere guardar en un archivo de texto:
```
sh tarql --ntriples pokemon.sparql pokemon_database.csv > pokemon_rdf.ttl
```
