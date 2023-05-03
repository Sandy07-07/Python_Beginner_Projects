from translate import Translator

# To get the input
user_input = input("Enter the text: ")

# List of all the available languages for translation
languages = {1: "en", 2: "es", 3: "pt", 4: "zh"}

# To select the Choice of language
while True:
    selected_lang = int(
        input("Translate in 1) English  2) Spanish 3) Portuguese 4) Chinese : ")
    )
    if selected_lang in languages:
        translator = Translator(to_lang=languages[selected_lang])
        break
    else:
        print("Please select a valid option!")
        continue

# To translate the text according to the user selected language choice
translation = translator.translate(user_input)

print(" Your translated text is :- " + translation)
