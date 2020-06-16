Plus ou moins:
=============

Nous voici enfin a un exercice intéressant et surtout intéractif:
Vous avez surement déjà joué ou alors au moins entendu parler du jeux chaud ou froid, nous allons faire une version un peu différente de ce jeux appelé plus ou moins.

## Le corps du programme: GuessMe

Le but est de coder un fonction qui va générer un int aléatoire entre 0 et 100, et nous devrons le deviner en émettant des hypothèses via stdin. Notre algorithme devra nous donner des indices en nous indicant si le nombre généré est supérieur, inférieur, ou égale à celui-ci que venons de rentrer dans notre programme.

Voici le prototype de la fonction:

```python
guess_me():
        "-> boolean"
```

Une fois le bon chiffre trouver, la fonction va demander au joueurs si celui-ci veut continuer la partie ou non, et renverra False si celui-ci veut arreter et True so celui-ci veut continuer.

### Génération du nombre aléatoire:

Pour générer le nombre aléatoire vous devrez importer et utiliser la bibliothèque random.

```python
import random
```

Nous pouvons utiliser la fonction randrange(min, max, step) de cette bibliothèque, pour générer notre nombre aléatoire.

Un peu de réalisme, afin de rajouter un peu de réalisme, nous pouvons simuler en temps d'attente pendant la génération du nombre aléatoire. Car celle-ci est instanté nous allons utiliser la fonction sleep de la bibliothèque time qui va stopper l'exécution du programme pendant un nombre de seconde donné en argument.

```python
from time import sleep
```

Un temps d'attente d'une seconde suffit largement le but n'étant pas non plus d'ennuyer le joueur.

### Récupération de l'essais sur stdin:

Une fois nombre aléatoire généré et stocké, nous allons demander au joueur de le deviner en utilisant la fonction input qui permet de récupérer une entré clavier. 
Mais attention cette entré est récupéré sous la forme d'une string, vous allez donc devoir la caster en integer avant de la sauvegarder.
    Attention à ce que le nombre soit bien entre 0 et 100 sinon le joueur aura du mal à trouver votre nombre généré.

```python
n = int(input("Entrez votre essais : "))
```

### Quelques indications:

Il va falloir donner quelques indications basiques au joueur, qui sont:

1. Bravo, vous avez trouvé le nombre
2. Faux, mon nombre est plus grand
3. Faux, mon nombre est plus petit

Pour cela vous n'avez pas d'autre moyens que d'utiliser des conditions.

### Veux-tu continuer à jouer avec moi ?

Une fois le nombre trouvé par le joueur vous devrez lui demander si il veut continuer à jouer ou arrêter. Pour cela la fonction input fera totalement l'affaire.
Si le joueur repond oui, la fonction guess\_me renverra True, sinon False.

### En combien d'essais ?

Une petite features sympas et très simple, un compteur d'essais que vous devrez afficher une fois le nombre trouvé par le joueur afin que celui-ci connaisse son score.

### Et la politesse alors ...

Un petit message de bienvenue et d'au revoir, grace à print serait également le bienvenue.

## Une DataBase pour retenir les scores:

### JSON

Afin de stocker les scores, même une fois le programme arrêté nous allons devoir, les mettre dans un fichier. Plusieurs formats peuvent être utilisés pour cela, comme le JSON, le CSV, le YAML. Mais pour ce sujet vous devrez utiliser du JSON.

```python
import JSON
```

Vous aurez besoin des fonctions suivantes pour recupérer et stocké un dictionnaire en JSON:


1. Pour récupérer les donnés présente dans le fichier:
```python
with open(filename, 'r') as f:
    data = json.load(f)
```

2. Pour écrire les donnés dans le fichier:
```python
with open(filename, 'w+', encoding = utf-8) as f:
    data = json.dump(data, f, indent = 4)
```

Attention à bien vérifier que la donné soit valide et que le fichier voulu existe avant de la charger.
Dans le cas où le fichier n'existe pas encore, la variable data sera initialisé avec les valeurs suivantes:
Pour cela vous pourrez utiliser la fonction suivante qui renvoie une liste des
fichiers présent dans le dossier courant.

```python
import os

files = os.listdir()
```

```json
{
    "players": []
}
```

Le JSON doit contenir un objet players contenant une liste d'objets avec dedans:

1. Le nom du joueur
2. Son meilleur score
3. Som pire score

Voici un exemple d'un fichier valide voulu :

```json
{
    "players": [
        {
            "name": "Alexandre",
            "Best Score": 3,
            "Worst Score": 9
        }, {
            "name": "Léa",
            "Best Score": 4,
            "Worst Score": 5
        }
    ]
}
```

### Une petit scoreboard:

Le but ici est de stocker sous forme de json, une liste contenant le nom des joueurs avec leurs pires et meilleures scores.

Pour cela nous allons créer une classe appelé DataBase. Celle-ci doit contenir un
attribut filename contenant le path relatif du fichiers où sont stocké les données.Ainsi qu'un dictionnaire **Datas** qui va contenir les donnés JSON chargés en mémoire.

Il doit également contenir les fonctions suivantes:

1. la fonction d'init:

Celle-ci va essayer de charger les données contenus dans le fichier et les stockés dans une variable.

```python
__init___(self)
```

2. Ajout d'un joueur:

Cette fonction va ajouter un joueur dans la liste des joueurs, en mettant les champs "Best Scores" et "Worst Scores" à None.

```python
add_player(self, name)
```

3. Trouver un joueur:

Cette fonction va parcourir la liste de joueurs et va retourner True si le joueur demandé est présent dans celle-ci et False dans l'autre cas.

```python
find_player(self,name)
```

4. Ajoute un score:

Cette fonction va rajouter un score pour un joueur donné. Celui-ci doit remplacer le best score actuel si il est plus petit et remplacer le worst score si il est plusgrand.

```python
add_score(self, player_name, score)
```

Attention pendant les comparaisons, les deux variables doivent être de même types (casts explicites).

5. Sauvegarde les données:

Cette fonction sera appelé avant de quitter votre programme et à pour but d'écrire les données dans le fichiers JSON comme indiqué plus haut dans le sujet.

```python
store(self)
```

6. Affichage des scores:

Cette fonction va servir à afficher les scores d'un joueur de la façon suivante:

```
Voici tes scores [Nom du Joueur]:
    Best Score: 1
    Worst Score: 38
```

Elle a le prototype suivant:

```python
print_player(self, player_name)
```

### Un peu d'intéractivité:

Maitenant que la classe DataBase est prête nous allons pouvoir l'utiliser.
Pour cela, vous devrez créer un objet de type DataBase de la façon suivante:

```python
database = DataBase()
```

Une fois ceci fais vous pouvez demander au joueur d'entré son nom et de vérifier si celui-ci est déjà dans la base de donné.
Si c'est le cas, dites lui bonjour avec un petit message personnalisé.
Sinon, dites lui quand même bonjour, et expliquez lui les règles du jeu.

Attention, n'oubliez pas d'afficher les scores de votre joueur avant de quitter le programme !

### Bonus, un écran un peu plus clair:

En dernier, et histoire de faire un petit bonus. Je vais vous demander de trouver un moyen d'effacer tout ce qu'il y a sur vôtre écran avant de commencer le jeu, afin de ne plus avoir le shell présent par exemple.

Un petit indice, vous devez utilisez une fonction présente dans la bibliothèque **os**.

Vous pouvez également effacer le texte avant chaque récriture dans la console afin de donné un peu plus de sérieux à votre jeu.

# BONNE CHANCE !!!
