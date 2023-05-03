import colorama
# Back is for Background and Fore is for Text colour
from colorama import Back, Fore

# This line is to make sure that the colour style resets once the execution of the program is complete
colorama.init(autoreset=True)

text = input("Enter the Text to be printed in colour :- ")

# Colorama has limited colour options
print(Fore.BLACK + Back.WHITE + text)
print()
print(Fore.RED + Back.CYAN + text)
print()
print(Fore.GREEN + Back.MAGENTA + text)
print()
print(Fore.YELLOW + Back.BLUE + text)
print()
print(Fore.BLUE + Back.YELLOW + text)
print()
print(Fore.MAGENTA + Back.GREEN + text)
print()
print(Fore.CYAN + Back.RED + text)
print()
print(Fore.WHITE + Back.BLACK + text)
