# Initialiser une liste vide pour stocker les nombres
nombres = []

# Demander à l'utilisateur de saisir 10 nombres entiers
for i in range(10):
    nombre = int(input(f"Entrez le nombre {i + 1} : "))
    nombres.append(nombre)

# Afficher les éléments de la liste séparés par une tabulation
print("Nombres saisis :", "\t".join(map(str, nombres)))

# Calculer et afficher la somme et la moyenne des éléments de la liste
somme = sum(nombres)
moyenne = somme / len(nombres)
print("Somme des nombres :", somme)
print("Moyenne des nombres :", moyenne)

# Afficher les éléments supérieurs ou égaux à la moyenne
print("Nombres supérieurs ou égaux à la moyenne :")
for nombre in nombres:
    if nombre >= moyenne:
        print(nombre)
