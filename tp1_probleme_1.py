class Livre:
    def __init__(self, titre, auteur, annee, statut):
        self.titre = titre
        self.auteur = auteur
        self.annee = annee
        self.statut = statut

    def afficher_livre(self):
        print(
            f"{self.titre}, a ete ecrit en {self.annee} par {self.auteur}, il est {self.statut} maintenant"
        )

    def to_string(self):
        return f"{self.titre}, {self.statut}, {self.annee}, {self.auteur}"


class Bibliotheque:
    def __init__(self, livres: list[Livre]):
        self.livres = livres

    def ajouter_livre(self, livre: Livre):
        self.livres.append(livre)

    def emprunter_livre(self, livre: Livre):
        for liv in self.livres:
            if liv.titre == livre.titre:
                if liv.statut == "disponible":
                    livre.statut = "emprunte"
                    print(f"Le livre '{liv.titre}' a été emprunté")
                else:
                    print(f"le livre {livre.titre} n'est pas dispinible!")
                break

    def rendre_livre(self, livre: Livre):
        for liv in self.livres:
            if liv.titre == livre.titre:
                if liv.statut == "emprunte":
                    livre.statut = "disponible"
                    print(f"Le livre '{liv.titre}' a été rendue")
                else:
                    print(
                        f"Le livre '{liv.titre}' a été deja rendue, tu ne peux pas le rendre a nouveau"
                    )
                break

    def afficher_livres(self):
        for livre in self.livres:
            livre.afficher_livre()

    def supprimer_tous_livres(self):
        self.livres = []


def sauvegader_livres(livres: list[Livre]):
    with open("tp_1.txt", "w") as tp1_txt:
        for liv in livres:
            tp1_txt.write(liv.to_string() + "\n")


def rendre_livres(bibliotheque: Bibliotheque):
    with open("tp_1.txt", "r") as tp1_txt:
        for livre_str in tp1_txt:
            livre_str = livre_str.strip()  # supprimer le \n

            livre_propriete = livre_str.split(
                ", "
            )  # transformer les propriete de livre a une list

            bibliotheque.ajouter_livre(
                Livre(
                    livre_propriete[0],
                    livre_propriete[1],
                    livre_propriete[2],
                    livre_propriete[3],
                )
            )


def test_programme():
    livre1 = Livre("liv1", "auteur1", 1000, "disponible")
    livre2 = Livre("liv2", "auteur2", 2000, "emprunte")

    # ajout par le constracteur de la class Bibliotheqee
    biblio = Bibliotheque([livre1, livre2])

    # ajout par la methode ajouter_livre
    biblio.ajouter_livre(Livre("liv3", "auteur3", 3000, "emprunte"))
    biblio.ajouter_livre(Livre("liv4", "auteur4", 4000, "disponible"))

    # emprunter livre1
    biblio.emprunter_livre(livre1)

    # rendre livre2
    biblio.rendre_livre(livre2)

    biblio.afficher_livres()

    # sauvegader le ouput dans un fichier json
    sauvegader_livres(biblio.livres)

    # supprimer tous les livres qui existe dans la biblio
    biblio.supprimer_tous_livres()
    biblio.afficher_livres()

    rendre_livres(biblio)
    biblio.afficher_livres()


test_programme()
