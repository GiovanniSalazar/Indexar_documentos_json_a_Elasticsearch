# Indexar documentos json a Elasticsearch usando Python

Este simple script pretende insertar documentos json de forma dinamica ubicados en una carpeta para ser volcados a Elasticsearch.

# Probado con :

  - Ubuntu 18.04
  - Python 3
  - pip 3

# Instalando Elasticsearch (como root)

Instalación de ES.

```sh
$ wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | sudo apt-key add -
$ echo "deb https://artifacts.elastic.co/packages/6.x/apt stable main" | sudo tee -a /etc/apt/sources.list.d/elastic-6.x.list
$ apt update
$ apt install elasticsearch
```
Vamos editar el archivo elasticsearch.yml para que efectos de prueba reemplazaremos localhost por 0.0.0.0 . (no olvidar descomentar). 

```sh
$ nano /etc/elasticsearch/elasticsearch.yml
network.host: 0.0.0.0
...
cluster.initial_master_nodes: ["node-1"]
```
Luego de configurar el yml , procedemos a iniciar ES. 

```sh
$ systemctl start elasticsearch
$ systemctl enable elasticsearch
```
Ahora procedemos a validar si ES esta corriendo correctamente.(cambiar la IP por la de la máquina donde realizas la instalación)

```sh
$ curl -X GET "192,168.0.100:9200"
{
  "name" : "ubuntu1",
  "cluster_name" : "elasticsearch",
  "cluster_uuid" : "beJf9oPSTbecP7_i8pRVCw",
  "version" : {
    "number" : "6.4.2",
    "build_flavor" : "default",
    "build_type" : "deb",
    "build_hash" : "04711c2",
    "build_date" : "2019-09-26T13:34:09.098244Z",
    "build_snapshot" : false,
    "lucene_version" : "7.4.0",
    "minimum_wire_compatibility_version" : "5.6.0",
    "minimum_index_compatibility_version" : "5.0.0"
  },
  "tagline" : "You Know, for Search"
}
```
Ahora procederemos a utilizar los archivos ubicados en el repositorio y a instalar el elasticsearch client con pip3 :
```sh
$ pip3 install elasticsearch
```
Ahora procederemos a utilizar los archivos ubicados en el repositorio y a instalar el elasticsearch client con pip3 :
```sh
$ pip3 install elasticsearch
```
### Contenido

* carpeta json/ : contiene los ejemplos de documentos json a indexar a ES.
* elastic.py : clase hacia elasticsearch.
* main.py : Realiza el loop de las carpeta instaciando la clase elastic.

Ahora ejecutamos el script estando ubicados en la misma carpeta del .py :
```sh
$ python3 main.py
```
* Sugieron instalar el plugin elasticsearch-head en google chrome para efectos de vizualición y colocar http://Mi_IP:9200/ en el input de la IP.
* Para validar lo indexado podemos ejecutar un curl de la siguiente forma :
```sh
curl -X GET "MI_IP:9200/_search?pretty" -H 'Content-Type: application/json' -d'
{
    "query": {
        "match_all": {}
    }
}
'
```
