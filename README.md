
# Access
$ cd projet12

# environnement virtuel
$ python -m venv env 

# activation environnement 
$ env\Scripts\activate

#installation depedance
$ pip install -r requirements.txt

#faire les migrations 
$ python manage.py makemigrations

#migrer les données
$ python manage.py migrate

#demarrer le serveur
$ python manage.py runserver 

Le projet est une api rest utilisant le framework django c'est un projet CRM pour voir le suivi des clients . L'API propose des filtre pour les clients les evenements et les contrats.
L'application peut etre gere à la fois sur postman et sur le django Admin . 

Vous noterez que vous devrez faire une base de donnees postgresql ce tuto m'a permis de l'implementer : https://www.youtube.com/watch?v=unFGJhIvHU4

Voici la documentation postman : https://documenter.getpostman.com/view/19745824/2s8Z6saFFk
