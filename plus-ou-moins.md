# Plus ou moins:

Nous voici enfin a un exercice intéressant et surtout intéractif:
Vous avez surement déjà joué ou alors au moins entendu parler du jeux chaud ou froid, nous allons faire une version un peu différente de ce jeux appelé plus ou moins.

Le but est de coder un fonction qui va générer un int aléatoire entre 0 et 100, et nous devrons le deviner en émettant des hypothèses via stdin. Notre algorithme devra nous donner des indices en nous indicant si le nombre généré est supérieur, inférieur, ou égale à celui-ci que venons de rentrer dans notre programme.

Voici le prototype de la fonction:

    guess_me():
        "-> boolean"

Notre fonction devra renvoyer True si nous arrivons à devinez le nombre généré, et False si nous n'avons échoué après nos 7 essais.

Pour générer le nombre aléatoire vous devrez importer et utiliser la bibliothèque random.

    import random
