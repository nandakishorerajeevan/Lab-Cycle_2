import pandas as pd

df = pd.read_csv("student_records.csv")

df = df.drop_duplicates().replace({True: 0, False: 0})
df = df[~(df.drop(columns=["Extracurricular"]) == 0).all(axis=1)]


def most_marks():

    subjects = df.iloc[:, 5:10]
    print("\nTOPPERS LIST AND MARKS :\n")
    print(f"\n{'Subject':^20}{'Topper':^20}{'Mark':^20}")
    print("-" * 60)

    for subject in subjects:
        max_index = df[subject].idxmax()
        topper_name = df.loc[max_index, "Name"]
        toppers_mark = df[subject].max()

        print(f"{subject:^20}{topper_name:^20}{toppers_mark:^20}\n")


most_marks()
