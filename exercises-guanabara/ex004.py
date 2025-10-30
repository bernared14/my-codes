# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele. 🇧🇷
# Write a program that reads something from the keyboard and displays its primitive type and all possible information about it on the screen. 🇺🇸
# Escribe un programa que lea algo del teclado y muestre su tipo primitivo y toda la información posible sobre él en la pantalla. 🇪🇸
# Écrivez un programme qui lit une valeur saisie au clavier et affiche à l'écran son type primitif ainsi que toutes les informations possibles la concernant. 🇫🇷

valor = input("Type something: ")
print(f"The primitive type of this value is {type(valor)}.")
print(f"Does this value only contain spaces?: {valor.isspace()}")
print(f"Is this value numerical?: {valor.isnumeric()}")
print(f"Is this value represented alphabetically?: {valor.isalpha()}")
print(f"Is this value alphanumeric?: {valor.isalnum()}")
print(f"Is this value entirely capitalized?: {valor.isupper()}")
print(f"Is this value entirely lowercase?: {valor.islower()}")
print(f"Is this value capitalized?: {valor.istitle()}")
