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
    elif choice == "2":
        term = input("What term do you want me to add? ")
        if term not in geek:
            definition = input("What is the definition?")
            geek[term] = definition
            print(f"\n {term} has been added.")
        else:
            print(f"Term: {term} already exists. Try redefining it.")
    elif choice == "3":
        term = input("What term do you want me to redefine? ")
        if term in geek:
            definition = input("What is the definition?")
            geek[term] = definition
            print(f"\n {term} has been redefined.")
        else:
            print(f"Term: {term} can't be found. Try adding it.")
    elif choice == "4":
        term = input("What term do you want me to delete? ")
        if term in geek:
            del geek[term]
            print(f"\n Okay, {term} has been deleted.")
        else:
            print(f"Term: {term} can't be found.")
    else:
        print(f"\nSorry but {choice} is not a valid choice.")