import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("iris.csv")
df = df.drop_duplicates()
df = df.dropna()

# >> if the cleaned csv wanted to save.
# df.to_csv("cleaned_data.csv", index=False)

train_data = df.sample(frac=0.8, random_state=10)
test_data = df.drop(train_data.index)


def num_of_samples_species():

    number_of_samples_of_each_species = df["species"].value_counts()
    print(f"\n{'SPECIES AND COUNTS':^30}")
    print("x" * 31)
    print(f"{'Species':<15}{'Counts':>15}")
    print("-" * 31)
    for species, counts in number_of_samples_of_each_species.items():
        print(f"{species:<15}:{counts:>15}\n")


def sepallength_petallength_histogram():

    plt.hist(df["sepal_length"], bins=10, alpha=0.5, color="red", label="Sepal Length")
    plt.hist(df["petal_length"], bins=10, alpha=0.5, color="blue", label="petal Length")

    plt.xlabel("Values")
    plt.ylabel("Frequency")

    # max_length = max(df["sepal_length"].max(), df["petal_length"].max())

    # plt.yticks(range(0, float(max_length) + 1, 0.5))
    plt.title("Sepal Length and Sepal Width")
    plt.legend()

    plt.show()


def distribution_species_barchart():

    width = 0.7
    species_count = df["species"].value_counts()

    plt.bar(
        species_count.index, species_count.values, width, color="red", label="Species"
    )

    plt.xlabel("Species")
    plt.yticks(range(0, 60, 5))
    plt.ylabel("Number of Samples")
    plt.title("Distribution of Species")

    plt.show()


def menu():
    print("\n#### MENU ####")
    print("Show that :")
    print("   1.training set")
    print("   2.testing set")
    print("   3.number of samples for each species in data set")
    print("   4.histograms of sepal length and petal length")
    print("   5.distribution of species using a bar chart.")
    print("   6.Exit")


def main():
    while True:
        menu()
        choice = input("\nEnter Your choice : ")
        if choice == "1":
            print("\nTraining set is :\n", train_data)
        elif choice == "2":
            print("\nTesting set is :\n", test_data)
        elif choice == "3":
            num_of_samples_species()
        elif choice == "4":
            sepallength_petallength_histogram()
        elif choice == "5":
            distribution_species_barchart()
        elif choice == "6":
            print("\nExitng...")
            break
        else:
            print("\nInvalid Choice...try again\n")

        input("\n>> press ENTER to continue..")


if __name__ == "__main__":
    main()
