titre = input()
auteur = input()

for caractere in titre:
    if (caractere != ' ' 
        and caractere != 'A'
        and caractere != 'E'
        and caractere != 'I'
        and caractere != 'O'
        and caractere != 'U'
        and caractere != 'Y'):
        print(caractere, end="")

print()

for caractere in auteur:
    if (caractere != ' ' 
        and caractere != 'A'
        and caractere != 'E'
        and caractere != 'I'
        and caractere != 'O'
        and caractere != 'U'
        and caractere != 'Y'):
        print(caractere, end="")




