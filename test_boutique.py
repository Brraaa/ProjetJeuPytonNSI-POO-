class Boutique:
    def __init__(self):
        self.boutique_items = [
    {"name": "Épée en fer", "description": "Une épée en fer de qualité supérieure.", "prix": 50, "dégâts": 10},
    {"name": "Armure en cuir", "description": "Une armure légère en cuir.", "prix": 30, "défense": 5}
]
        
    def acheter_objet(self, joueur, boutique, objet):
        if joueur["argent"] >= objet["prix"]:
            joueur["argent"] -= objet["prix"]
            joueur["inventaire"].append(objet)
            print(f"Vous avez acheté {objet['name']}!")
        else:
            print("Vous n'avez pas assez d'argent pour acheter cet objet.")