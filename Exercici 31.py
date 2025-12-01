any_actual = int(input("Introdueix l'any actual: "))

persones = []

for i in range(4):
    print(f"\nPersona {i+1}:")
    nom = input("Nom: ")
    any_naixement = int(input("Any de naixement: "))
    edat = any_actual - any_naixement
    persones.append((nom, any_naixement, edat))

# Llistat
print()
print(f"{'Nom':<10}{'Data naixement':<15}{'Anys que farà aquest any':<25}")
for nom, any_naix, edat in persones:
    print(f"{nom:<10}{any_naix:<15}{edat:<25}")
