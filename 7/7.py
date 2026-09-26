import pandas as pd

data = {
    "SN": [1, 2, 3, 4, 5],
    "Name": [
        "Geoffrey Hinton",
        "Yann LeCun",
        "Andrew Ng",
        "Phila Suoni",
        "Yemehi Yathi",
    ],
    "Country": ["Canada", "France", "USA", "UK", "France"],
    "Innovation": [
        "Deep Learning",
        "Convolutional Neural Nets",
        "Online ML Courses",
        "Artificial Intelligence",
        "Data Analytics",
    ],
    "Year": [1986, 1989, 2011, 2023, 2025],
}

df = pd.DataFrame(data)
df.to_csv("tech_innovators.csv", index=False)


def show_csv_file():
    print("\n>> tech_innovators.csv created successfully.\n")
    print(df)


def before_2000():
    print("\ninnovators who contributed before the year '____' ")
    year_given = int(input("Enter the Year :"))
    print(f"\ninnovators who contributed before the year {year_given}: \n")
    name_index = df["Year"] < year_given
    name_of_contributor = df.loc[name_index, ["Name", "Year"]]
    if name_of_contributor.empty:
        print(f"  >> No contributors in the list before {year_given}!")
    else:
        print(name_of_contributor.to_string(index=False))


def menu():
    print("\n#### MENU ####")
    print("1.Show tech_contributor.csv file")
    print("2.innovators who contributed before the year ....")
    print("3.EXIT")


def main():
    while True:
        menu()
        choice = input("\nEnter the Choice :")
        if choice == "1":
            show_csv_file()
        elif choice == "2":
            before_2000()
        elif choice == "3":
            print("\nExiting...\n")
            break
        else:
            print("\nInvalid Choice..Try Again\n")

        input("\npress ENTER to continue..\n")


if __name__ == "__main__":
    main()
