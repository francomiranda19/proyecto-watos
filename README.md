# proyecto-watos
Proyecto del curso CC7220

La base de datos se obtuvo desde https://www.kaggle.com/mrdew25/pokemon-database , y se encuentra en pokemon_database_original.csv .

Para limpiarla, ejecutar el script limpiar_database.py .

Para transformar la base de datos a RDF y guardarlo en un archivo TTL, en la carpeta **tarql-1.2/bin** ejecutar (en Ubuntu):
```
sh tarql --ntriples pokemon.sparql pokemon_database.csv > pokemon_rdf_original.ttl
```

El archivo generado se puede limpiar a mano para dejarlo en el formato deseado. En este caso el archivo limpio está en pokemon_rdf.ttl .

Luego, en la página de <a href="https://cc7220.dcc.uchile.cl:8900/sparql">Virtuoso</a> se pueden ejecutar las consultas SPARQL del archivo consultas.txt, utilizando el link http://anakena.dcc.uchile.cl/~famirand/pokemon_rdf.ttl