import pandas as pd

df = pd.read_csv("auto-mpg.csv")
df1 = df.copy()
df["model year"] = 1900 + df["model year"]
df[["company", "model_name"]] = df["car name"].str.split(n=1, expand=True)
df.drop("car name", axis=1, inplace=True)


def menu():
    print("\n#### MENU #####\n")
    print("Show that...")
    print("  1.Raw Dataframe")
    print("  2.Cleaned Dataframe")
    print("  3.Cars Of Companies")
    print("  4.Average Mileage Of Companies")
    print("  5.Exit")


def cars_of_companies():
    companies_car = df.groupby("company")["model_name"]

    for company, models in companies_car:
        print(f"\n== {company} ==")
        print("----------------")

        for model in models.dropna():
            print(f"- {model}")

    print(companies_car)


def show_average_mileage_of_companies():
    companies_car = df.groupby("company")["mileage"]

    for company, mileage in companies_car:
        average_mileage = mileage.mean()
        print(f"\n== {company} ==")
        print("----------------")
        print(f"Average Mileage: {average_mileage:.2f}")


def main():
    while True:
        menu()
        choice = input("\nEnter your choice: ")

        if choice == "1":
            print(df1)

        elif choice == "2":
            print(df)

        elif choice == "3":
            cars_of_companies()

        elif choice == "4":
            show_average_mileage_of_companies()

        elif choice == "5":
            print("\nExiting...")
            break

        else:
            print("Invalid choice. Please try again.")

        input("\nPress Enter to continue...\n")


if __name__ == "__main__":
    main()
