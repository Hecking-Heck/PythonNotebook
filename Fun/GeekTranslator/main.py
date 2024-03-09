# Geek Translator
# Demonstrates using dictionaries

geek = {"404": "Clueless. From the web error message 404, meaning page not found.",
        "Googling": "Searching the Internet for background information on a person.",
        "Keyboard Plaque": "The collection of debris found in computer keyboards.",
        "Link Rot": "The process by which web page links become obsolete.",
        "Percussive Maintenance": "The act of striking an electronic device to make it work.",
        "Uninstalled": "Being fired. Especially popular during the dot-bomb era."
        }

choice = None

while choice != "0":
    print(
        """
        Geek Translator

        0 - Quit
        1 - Look Up a Geek Term
        2 - Add a Geek Term
        3 - Redefine a Geek Term
        4 - Delete a Geek Term
        """
    )

    choice = input("Choice: ")
    print()

    # Exit
    if choice == "0":
        print("Goodbye.")
        print("\n\nPress the enter key to exit.")

    elif choice == "1":
        term = input("What term do you want me to translate? ")
        if term in geek:
            definition = geek[term]
            print(f"\n {term} means {definition}")
        else:
            print(f"Sorry I do not know {term}.")