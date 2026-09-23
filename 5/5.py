def repetation_of_word_count():
    word = (
        str(input("\nEnter the word to search from the text file : ")).lower().strip()
    )

    with open("5.txt", "r") as file:
        text_file = file.read().lower()

    for symbol in ".,!?;:'\"()[]{}":
        text_file = text_file.replace(symbol, "")

    words = text_file.split()

    counts = words.count(word)
    print(f"\n>> The word '{word}' is repeated '{counts}' times in the text file.\n")


def repeat_word_in_dictionary():
    word = input("\nEnter the word to search from the text file: ").lower().strip()

    with open("5.txt", "r") as file:
        text_file = file.read().lower()

    for symbol in ".,!?;:'\"()[]{}":
        text_file = text_file.replace(symbol, "")

    sentences = text_file.splitlines()

    word_dictionary = {}

    for i in range(len(sentences)):
        words = sentences[i].lower().split()

        if word in words:
            indx = words.index(word)
            word_dictionary[i] = indx
        else:
            word_dictionary[i] = -1

    print("\n", word_dictionary)


def repeting_words():
    with open("5.txt", "r") as file:
        text_file = file.read().lower().split()

    word_counts = {}

    for word in text_file:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    sorted_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)

    print("\nRepeating words are:\n######################\n")

    for word, count in sorted_words:
        if count > 1:
            print(f"{word:<10} : {count:>3}")


def menu():
    print("\n### MENU ###")
    print("1. Count the repetition of a word in the text file")
    print("2. Find the index of a word in each sentence of the text file")
    print("3. All the Repeating Words")
    print("4. Exit")


def main():
    while True:
        menu()
        choice = input("\nEnter your choice : ")

        if choice == "1":
            repetation_of_word_count()
        elif choice == "2":
            repeat_word_in_dictionary()
        elif choice == "3":
            repeting_words()
        elif choice == "4":
            print("\nExiting the program.\n")
            break
        else:
            print("\nInvalid choice. Please try again.\n")

        input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()
