def find_name_occurrences(wordlist, name):
    count = 0
    indices = []
    for word in wordlist:
        indx = word.find(name)
        if indx != -1:
            count += 1
            indices.append(indx + 1)
        else:
            indices.append(0)
    return (count, indices)


name = input("\nEnter the name to search for (in this txt file, it is only 'ver'): ")

with open("wordlist.txt", "r") as file:
    wordlist = [word.strip() for word in file]

result = find_name_occurrences(wordlist, name)
print(f"\nResult : {result}\n")
