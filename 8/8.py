import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("sales_data.csv")


def monthly_profit_linechart():

    df["month"] = df["month"].str[:3]

    plt.plot(df["month"], df["profit"])
    plt.title("Monthly Profit")
    plt.xlabel("month")
    plt.ylabel("profit")

    plt.xticks(rotation=65)

    plt.show()


def electronics_clothing_sales_barchart():
    x = np.arange(len(df))
    width = 0.4

    plt.bar(x - width / 2, df["electronics"], width, color="blue", label="ELECTRONICS")
    plt.bar(x + width / 2, df["clothing"], width, color="brown", label="CLOTHING")

    max_sales = max(df["electronics"].max(), df["clothing"].max())

    plt.xticks(x, df["month"].str[:3])
    plt.yticks(range(0, int(max_sales) + 1000, 1000))

    plt.xlabel("month")
    plt.ylabel("sales")
    plt.legend()

    plt.show()


def yearly_sale_piechart():

    sales = [
        df["clothing"].sum(),
        df["electronics"].sum(),
        df["groceries"].sum(),
        df["furniture"].sum(),
    ]
    product = ["Clothing", "Electronics", "Groceries", "Furniture"]

    plt.pie(sales, labels=product, autopct="%1.1f%%")
    plt.title("YEARLY SALES")
    plt.show()


def menu():

    print("\n#### MENU ####")
    print("show that :")
    print("  1.Monthly profit using line chart")
    print("  2.Electronics and Clothing sales in a grouped bar chart.")
    print("  3.Total yearly sales for each category as a pie chart.")
    print("  4.Exit\n")


def main():
    while True:
        menu()
        choice = input("Enter your choice :")
        if choice == "1":
            monthly_profit_linechart()
        elif choice == "2":
            electronics_clothing_sales_barchart()
        elif choice == "3":
            yearly_sale_piechart()
        elif choice == "4":
            print("\nExiting...\n")
            break
        else:
            print("\nInvalid Choice..try again\n")

        input("\n>>>> press Enter to continue \n")


if __name__ == "__main__":
    main()
