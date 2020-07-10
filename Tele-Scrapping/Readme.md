# Télé réalité Scrapping

## But

Le but de script de créer un graphe des relations
entre les personnes ayant participé à des téléréalités
françaises.

Pour cela je me base sur le wiki fandom de la téléréalité:
[link](https://tele-realite.fandom.com/fr/wiki/Wiki_T%C3%A9l%C3%A9_R%C3%A9alit%C3%A9)

## Usage:

Le script va vous afficher le graphe sous format Dot. Pour le transformer en image vous
pouvez utilise le programme dot du package 'graphviz'. Mais bien sûr cela va dépendre de
votre disbution et de votre OS.

Vous devrez également avoir installé le module python 'requests'.
Pour cela:

```bash
$ pip install requests
```

oui j'ai eu la flemme de faire un requirements.txt ou un piplock ...

Pour créer votre graphe vous pouvez utilisez le script de la façon suivante:

```bash
python3 main.py [pseudo] [depth] > graphe.dot
dot -T jpg -o monImage.jpg graphe.dot
```

Ce qui donne par exemple:

```bash
python3 main.py Kim_Glow 2 > graphe.dot
dot -T jpg -o monImage.jpg graphe.dot
```

Exemple:

Pour Kim Glow avec un profondeur de 4.

![image](Exemple.jpg)
