import pandas as pd
import matplotlib.pyplot as plt
import calendar
import numpy as np


def create_contribution_table():
    data = {
        "SN": [1, 2, 3],
        "Name": ["Linus Torvalds", "Tim Berners-Lee", "Guido van Rossum"],
        "Country": ["Finland", "England", "Netherlands"],
        "Contribution": ["Linux Kernel", "World Wide Web", "Python"],
        "Year": [1991, 1990, 1991],
    }

    df = pd.DataFrame(data)
    df.to_csv("contributors_table.csv", index=False)


def toothpaste_sales_scatter_plot():
    df = pd.read_csv("company.csv")
    plt.scatter(df["month_number"], df["toothpaste"])
    plt.title("Monthly Toothpaste Sales")
    plt.xlabel("Month")
    plt.ylabel("Toothpaste Sales")
    plt.xticks(
        range(1, len(df) + 1),
        [calendar.month_abbr[i] for i in range(1, len(df) + 1)],
        rotation=90,
    )
    plt.yticks(range(0, int(df["toothpaste"].max()) + 1000, 500))
    plt.show()


def facecream_facewash_sales_barchart():
    df = pd.read_csv("company.csv")
    x = np.arange(len(df))
    width = 0.4

    plt.bar(x - width / 2, df["facecream"], width, color="green", label="Face Cream")

    plt.bar(x + width / 2, df["facewash"], width, color="red", label="Face Wash")

    plt.xticks(
        x,
        [calendar.month_abbr[i] for i in range(1, len(df) + 1)],
        rotation=90,
    )
    max_sales = max(df["facecream"].max(), df["facewash"].max())
    plt.yticks(range(0, int(max_sales) + 1000, 500))
    plt.xlabel("Month")
    plt.ylabel("Sales")
    plt.title("Monthly Product Sales")
    plt.legend()
    plt.show()


def year_sales_piechart():
    df = pd.read_csv("company.csv")
    sales = [
        df["facecream"].sum(),
        df["facewash"].sum(),
        df["toothpaste"].sum(),
        df["bathingsoap"].sum(),
        df["shampoo"].sum(),
        df["moisturizer"].sum(),
    ]
    products = [
        "Face Cream",
        "Face Wash",
        "Toothpaste",
        "Bathing Soap",
        "Shampoo",
        "Moisturizer",
    ]
    plt.pie(sales, labels=products, autopct="%1.1f%%")
    plt.title("Yearly Sales Distribution")
    plt.show()


def menu():
    print("\n##### Menu #####:")
    print("1. Create Contribution Table")
    print("2. Toothpaste sales data of each month using scatter plot")
    print("3. Face cream and face wash product sales data using the bar chart")
    print("4. Total sale data for last year for each product using a Pie chart")
    print("5. Exit")


def main():
    while True:
        menu()
        choice = input("\nEnter your choice: ")

        if choice == "1":
            create_contribution_table()
        elif choice == "2":
            toothpaste_sales_scatter_plot()
        elif choice == "3":
            facecream_facewash_sales_barchart()
        elif choice == "4":
            year_sales_piechart()
        elif choice == "5":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")
        input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()
