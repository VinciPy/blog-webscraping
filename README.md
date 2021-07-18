# Blog Automatico via Web Scaping

O projeto se trata de um api de blog automatico, que ao digitar palavras-chaves, com auxilio de um bot pesquisará artigos em blogs relevantes para que insira no banco, forncecendo uma API, para que se possa utilizar, com o proposito de se entnder tanto API com o flask eweb scraping com beauty soup.

## 🚀 Começando

Para obter o código é nececessário o comando git clone https://github.com/VinciPy/blog-webscraping.git

Consulte **Implantação** para saber como implantar o projeto.

### 📋 Pré-requisitos

É necessário o docker, docker-compose, python(ultima versão), pip,  postgreSQL. **consulte a documentacação para a instalação do mesmo**


### 🔧 Instalação

Após se certificar de que a parte de Pré Requisitos está devidamente configurada, entre na pasta raiz e rode os comandos:
	
	- docker-composer build
	
	- docker-composer up -d

	- pip install -r requirements.txt

	- export FLASK_APP=app

	- flask db migrate
	
	- flask db upgrade

	- gunicorn -b 0.0.0.0:8000 app.app:app


Acesse localhost/post para ver se o retorno é nulo, e certificar que está tudo funcionando.



## 🛠️ Construído com

* [FLASK](https://flask.palletsprojects.com/en/2.0.x/) - O framework web usado
* [NGINX](https://www.nginx.com/) - Servidor Web e Proxy Reverso
* [DOCKER](https://docs.docker.com/compose) Orquestração de container

