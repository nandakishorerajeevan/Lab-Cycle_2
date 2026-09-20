def repetation_of_word_count():
    word = str(input("\nEnter the word to search from the text file : ")).lower()
    with open("5.txt", "r") as file:
        text_file = file.read()

    count = text_file.count(word)
    print(f"\n>> The word '{word}' is repeated '{count}' times in the text file.\n")


def repeat_word_in_dictionary():
    word = input("\nEnter the word to search from the text file: ").lower()
    with open("5.txt", "r") as file:
        text_file = file.read()

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


def menu():
    print("\n### MENU ###")
    print("1. Count the repetition of a word in the text file")
    print("2. Find the index of a word in each sentence of the text file")
    print("3. Exit")


def main():
    while True:
        menu()
        choice = input("\nEnter your choice : ")

        if choice == "1":
            repetation_of_word_count()
        elif choice == "2":
            repeat_word_in_dictionary()
        elif choice == "3":
            print("\nExiting the program.\n")
            break
        else:
            print("\nInvalid choice. Please try again.\n")

        input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()
