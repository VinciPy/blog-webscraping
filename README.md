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

## 📦 Desenvolvimento

Adicione notas adicionais sobre como implantar isso em um sistema ativo

## 🛠️ Construído com

Mencione as ferramentas que você usou para criar seu projeto

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - O framework web usado
* [Maven](https://maven.apache.org/) - Gerente de Dependência
* [ROME](https://rometools.github.io/rome/) - Usada para gerar RSS

## 🖇️ Colaborando

## 📌 Versão

Nós usamos [SemVer](http://semver.org/) para controle de versão. Para as versões disponíveis, observe as [tags neste repositório](https://github.com/suas/tags/do/projeto). 

## ✒️ Autores

Mencione todos aqueles que ajudaram a levantar o projeto desde o seu início

* **Um desenvolvedor** - *Trabalho Inicial* - [umdesenvolvedor](https://github.com/linkParaPerfil)
* **Fulano De Tal** - *Documentação* - [fulanodetal](https://github.com/linkParaPerfil)

Você também pode ver a lista de todos os [colaboradores](https://github.com/usuario/projeto/colaboradores) que participaram deste projeto.

## 📄 Licença

Este projeto está sob a licença (sua licença) - veja o arquivo [LICENSE.md](https://github.com/usuario/projeto/licenca) para detalhes.

## 🎁 Expressões de gratidão

* Conte a outras pessoas sobre este projeto 📢
* Convide alguém da equipe para uma cerveja 🍺 
* Obrigado publicamente 🤓.
* etc.


---
⌨️ com ❤️ por [Armstrong Lohãns](https://gist.github.com/lohhans) 😊
