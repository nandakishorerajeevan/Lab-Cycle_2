import pandas as pd

df = pd.read_csv("student_records.csv")

df = df.drop_duplicates().replace({True: 0, False: 0})
df = df[~(df.drop(columns=["Extracurricular"]) == 0).all(axis=1)]


def most_marks():

    subjects = df.iloc[:, 5:10]
    print(f"\n{'TOPPERS LIST AND MARKS':^60}")
    print(f"{'x' * 60:^60}")
    print(f"{'Subject':^20}{'Topper':^20}{'Mark':^20}")
    print("-" * 60)

    for subject in subjects:
        max_index = df[subject].idxmax()
        topper_name = df.loc[max_index, "Name"]
        toppers_mark = df[subject].max()

        print(f"{subject:^20}{topper_name:^20}{toppers_mark:^20}\n")


def avg_mark_of_gardes():
    subjects = df.iloc[:, 5:10]
    print(f"\n{'Average Mark Of Students Having Same Grades':^40}\n")

    for subject in subjects:
        grouping_by_grade = df[subject].groupby(df["Grade"]).mean(float)

        print(f"{subject :^40}")
        print(f"{'x' *40:^40}")
        print(f"{'Grade':^20}{'Average Mark':^20}")
        print(f"{'-' *40:^40}")

        for grade, average_mark in grouping_by_grade.items():
            print(f"{grade:^20}:{average_mark:^20.2f}")

        print("\n")


def menu():
    print("\n#### MENU ####")
    print("1.Toppers of subjects and their marks")
    print("2.Average Mark of Students having same grades")
    print("3.EXIT")


def main():
    while True:
        menu()
        choice = input("\nENTER YOUR CHOICE :")
        if choice == "1":
            most_marks()
        elif choice == "2":
            avg_mark_of_gardes()
        elif choice == "3":
            print("\nExiting....\n")
            break
        else:
            print("\nInvalid choice..try again")

        input("\npress ENTER to continue..\n")


if __name__ == "__main__":
    main()
