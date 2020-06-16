# Plus ou moins:

Nous voici enfin a un exercice intéressant et surtout intéractif:
Vous avez surement déjà joué ou alors au moins entendu parler du jeux chaud ou froid, nous allons faire une version un peu différente de ce jeux appelé plus ou moins.
## Le corps du programme: GuessMe

Le but est de coder un fonction qui va générer un int aléatoire entre 0 et 100, et nous devrons le deviner en émettant des hypothèses via stdin. Notre algorithme devra nous donner des indices en nous indicant si le nombre généré est supérieur, inférieur, ou égale à celui-ci que venons de rentrer dans notre programme.

Voici le prototype de la fonction:

```guess_me():
        "-> boolean"
```

Une fois le bon chiffre trouver, la fonction va demander au joueurs si celui-ci veut continuer la partie ou non, et renverra False si celui-ci veut arreter et True so celui-ci veut continuer.

### Génération du nombre aléatoire:

Pour générer le nombre aléatoire vous devrez importer et utiliser la bibliothèque random.

```import random```

Nous pouvons utiliser la fonction randrange(min, max, step) de cette bibliothèque, pour générer notre nombre aléatoire.

Un peu de réalisme, afin de rajouter un peu de réalisme, nous pouvons simuler en temps d'attente pendant la génération du nombre aléatoire. Car celle-ci est instanté nous allons utiliser la fonction sleep de la bibliothèque time qui va stopper l'exécution du programme pendant un nombre de seconde donné en argument.

```from time import sleep```

Un temps d'attente d'une seconde suffit largement le but n'étant pas non plus d'ennuyer le joueur.

### Récupération de l'essais sur stdin:

Une fois nombre aléatoire généré et stocké, nous allons demander au joueur de le deviner en utilisant la fonction input qui permet de récupérer une entré clavier. 
Mais attention cette entré est récupéré sous la forme d'une string, vous allez donc devoir la caster en integer avant de la sauvegarder.
    Attention à ce que le nombre soit bien entre 0 et 100 sinon le joueur aura du mal à trouver votre nombre généré.

```n = int(input("Entrz votre essais : "))```

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
