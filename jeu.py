from random import randint

x = 5
y = x

tableau = [[randint(0, 1) for k in range(x)] for i in range(y)]

def afficher(tab):
    for i in range(len(tab)):
        print(tab[i])

def cell(x, y, tab):
    return tab[y][x]

def mise_a_jour(tableau):
    nouveau_tableau = [[0 for k in range(len(tableau[0]))] for i in range(len(tableau))]
    for y in range(len(tableau)):
        for x in range(len(tableau[0])):
            n = 0
            for i in range(y - 1, y + 2):
                for j in range(x - 1, x + 2):
                    if i == y and j == x:
                        continue
                    if i >= 0 and i < len(tableau) and j >= 0 and j < len(tableau[0]):
                        n += cell(j, i, tableau)

while True:
    afficher(tableau)
    tableau = mise_a_jour(tableau)
    user_input = input("Press enter to continue or 'q' to quit... ")
    if user_input == 'q':
        break