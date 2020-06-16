import random
from time import sleep
import os
from os import system
import json

class DataBase:
    filename = "scores.json"

    def __init__(self):
        files = os.listdir()

        self.datas = {"players": []}
        if self.filename in files:
            with open(self.filename, 'r') as f:
                self.datas = json.load(f)

    def add_player(self, name):
        self.datas["players"].append({"name": name, "Best Score": None, "Worst Score": None})

    def find_player(self, name):
        for player in self.datas["players"]:
            if player["name"] == name:
                return True

        return False

    def add_score(self, player_name, score):
        player_datas = self.datas["players"]
        player = None

        for player_data in player_datas:
            if player_data["name"] == player_name:
                player = player_data
                break;
        if player == None:
            return

        if player["Best Score"] == None \
        or int(player["Best Score"]) > int(score):
            player["Best Score"] = score
        if player["Worst Score"] == None \
        or int(player["Worst Score"]) < int(score):
            player["Worst Score"] = score

    def store(self):
        with open(self.filename, 'w+', encoding='utf-8') as f:
            json.dump(self.datas, f, indent = 4)

    def print(self):
        print(self.datas)

    def print_player(self, player_name):
        for player in self.datas["players"]:
            if player_name == player["name"]:
                print("Voici tes scores " + player_name + ":")
                print("    Best Score: " + str(player["Best Score"]))
                print("    Worst Score: " + str(player["Worst Score"]))

def guess_me(database, player_name):
    print("génération d'un nombre entre 1 et 100 ...\n")
    sleep(1)

    n = random.randrange(0, 100, 1);
    cpt_essais = 0;

    print(n)

    while True:
        cpt_essais += 1

        while True:
            guess = int(input("Entre un nombre entre 0 et 100: "))

            if guess >= 0 and guess <= 100:
                break;
            print("Un chiffre en O et 100." \
                  " Tu ne trouveras jamais mon chiffre sinon !\n");

        if n == guess:
            print("Bravo !!! Tu as trouvé mon chiffre en " + str(cpt_essais) \
                + " essais !\n");
            database.add_score(player_name, int(cpt_essais))
            break;
        elif n < guess:
            print("Faux ! Mon chiffre est plus petit !\n");
        else:
            print("Faux ! Mon chiffre est plus grand !\n");

    end = input("Veux tu continuer à jouer ? (oui|non): ");

    return end == "oui";

# Clear l'écran avant d'aficher le jeu
_ = system("clear")

database = DataBase()
print("Salut ! Bienvenue sur 'Guess me':\n")

player_name = input("Avant de commencer quel est ton nom ? ")
print("")

if database.find_player(player_name):
    print("Bienvenue " + player_name + ", content de te revoir !")
else:
    database.add_player(player_name)

    print("Bienvenue dans Guess Me " + player_name + " !!!")
    print("Je vais générer un nombre entre 1 et 100, et tu devras le deviner.")
    print("Mais ne t'inquiète pas je vais te donner des indications ;)\n")
    print("C'est parti ! Commençons !")

while guess_me(database, player_name):
    continue;

database.print_player(player_name)
database.store()
print("\nC'était Super ! A une prochaine fois !");
