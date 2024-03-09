# High Scores
# Demonstrates list methods

scores = []

choice = None

while choice != "0":
    print(
        """
        0 - Exit
        1 - Show Scores
        2 - Add a Score
        3 - Delete a Score
        """
    )

    # Getting the user choice
    choice = input()

    # Printing user choice
    print()

    # Exiting
    if choice == "0":
        print("Goodbye.")
        input("\n\nPress the enter key to exit.")

    # List High Scores
    elif choice == "1":
        print("High Scores\n")
        print("NAME\tSCORE")
        index = 0
        for entry in scores:
            score, name = entry
            print(f"{index} |", name, "\t", score)
            index = index + 1

    # Adding a Score
    elif choice == "2":
        # Get player name
        name = input("Player Name: ")
        # Get player score
        score = int(input("Enter Score: "))
        # Create an entry for the list
        entry = (score, name)
        # Append the entry to the list
        scores.append(entry)
        # Sort the scores, reverse means highest at the top, lowest at the bottom
        scores.sort(reverse=True)
        # Only get the top 5 scores
        scores = score[:5]

    # Remove a score at an index
    elif choice == "3":
        score = int(input("Remove score at what index?"))
        if score in scores:
            scores.remove(score)
        else:
            print(score, " is not in the scores list.")

    else:
        print(f"{choice} is not a valid input.")