# Ma première fonction
## Hello world:

Créer votre première fonction pour dire bonjour au monde de l'informatique.

Celle-ci doit avoir le prototype suivant:

    hello():
        "-> string"

Elle doit donc s'appeler hello, ne prendre aucun arguments et renvoyer la string "Hello World!".

N'oubliez pas de l'afficher également avant de la renvoyer.

# Manipulation de string:
## Palindrome ou pas lindrome:

Un palindrom est un séquence de caractères qui ce lisent de la même façon de gauche à droite comme de droite à gauche.

Par exemple le mot "madam" est un palindrome.

Le but de cet exercice est de coder une fonction qui renvoit True si la string en paramètres est un palindrome et False si elle ne'en ai pas un.

Voici son prototype:

    is_palindrome():
        "string -> boolean"

Attention vous ne devez prendre en compte que les caractères alphanumerques ([A-Z][a-z]). Ce qui siginifie le string suivante doit renvoyer True:

    "Rise to vote sir"

## Devenez un agent secret, le codage de césar:

Le codage de césar est méthode simple de chiffrement ce basant sur la rotation des caractères. Ici nous voulons faire du Rot13, ainsi sur chacun des caractères de nôtre string nous appliquerons une rotation de 13:
Par exemple la string suivante:

    "Bonjour, j'aime le python"

Devient:

    "Obawbhe, w'nvzr yr clguba"

Enfin pour déchiffrer rien de plus simple, il nous suffit juste d'appliquer à nouveau le chiffrement de césar.

Votre fonction de chiffrement devra avoir le prototype suivant:

    Rot13():
        "string -> string"
