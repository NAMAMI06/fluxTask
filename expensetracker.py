import csv
import os
from datetime import datetime

import pandas as pd
import matplotlib.pyplot as plt



FILE_NAME = "expenses.csv"

CATEGORIES = [
    "Food",
    "Transport",
    "Utilities",
    "Shopping",
    "Education",
    "Entertainment",
    "Healthcare",
    "Other"
]



def add_expense():
    print("\n--- ADD EXPENSE ---")

    # Date validation
    while True:
        date = input("Enter date (DD-MM-YYYY): ")

        try:
            datetime.strptime(date, "%d-%m-%Y")
            break

        except ValueError:
            print("Invalid date. Please use DD-MM-YYYY.")

    # Description
    description = input("Enter description: ")

    # Amount validation
    while True:
        try:
            amount = float(input("Enter amount: "))

            if amount <= 0:
                print("Amount must be greater than 0.")
                continue

            break

        except ValueError:
            print("Please enter a valid number.")

    # Category selection
    print("\nCategories:")

    for i, category in enumerate(CATEGORIES, start=1):
        print(f"{i}. {category}")

    while True:
        try:
            category_choice = int(input("Select category (1-8): "))

            if 1 <= category_choice <= len(CATEGORIES):
                category = CATEGORIES[category_choice - 1]
                break

            print("Please select a number between 1 and 8.")

        except ValueError:
            print("Please enter a valid number.")

    # Check if file exists
    file_exists = os.path.exists("expenses.csv")

    # Save expense
    with open("expenses.csv", "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow([
                "Date",
                "Description",
                "Amount",
                "Category"
            ])

        writer.writerow([
            date,
            description,
            amount,
            category
        ])

    print("\n✓ Expense added successfully!")



def view_expenses():
    print("\n--- ALL EXPENSES ---")

    if not os.path.exists("expenses.csv"):
        print("No expenses found.")
        return

    with open("expenses.csv", "r", newline="", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)
        expenses = list(reader)

    if not expenses:
        print("No expenses found.")
        return

    print()

    print(
        f"{'Date':<15}"
        f"{'Description':<25}"
        f"{'Amount':<15}"
        f"{'Category'}"
    )

    print("-" * 75)

    for expense in expenses:
        try:
            amount = float(expense["Amount"])
        except (ValueError, TypeError):
            amount = 0

        print(
            f"{expense['Date']:<15}"
            f"{expense['Description']:<25}"
            f"₹{amount:<14.2f}"
            f"{expense['Category']}"
        )




def load_data():

    if not os.path.exists("expenses.csv"):
        return None

    try:
        df = pd.read_csv(
            "expenses.csv",
            encoding="utf-8-sig"
        )

    except Exception as error:
        print(f"Unable to read CSV file: {error}")
        return None

    # Remove unwanted spaces from column names
    df.columns = df.columns.astype(str).str.strip()

    # Make column names consistent
    column_mapping = {}

    for column in df.columns:
        column_lower = column.lower()

        if column_lower == "date":
            column_mapping[column] = "Date"

        elif column_lower == "description":
            column_mapping[column] = "Description"

        elif column_lower == "amount":
            column_mapping[column] = "Amount"

        elif column_lower == "category":
            column_mapping[column] = "Category"

    df = df.rename(columns=column_mapping)

    required_columns = [
        "Date",
        "Description",
        "Amount",
        "Category"
    ]

    # If old CSV does not have proper headers
    if not all(column in df.columns for column in required_columns):

        if len(df.columns) == 4:

            df = pd.read_csv(
                "expenses.csv",
                header=None,
                names=required_columns,
                encoding="utf-8-sig"
            )

        else:
            print("CSV file format is invalid.")
            return None

    # Convert Amount into numbers
    df["Amount"] = pd.to_numeric(
        df["Amount"],
        errors="coerce"
    )

    # Convert Date into datetime
    df["Date"] = pd.to_datetime(
        df["Date"],
        format="%d-%m-%Y",
        errors="coerce"
    )

    # Remove invalid rows
    df = df.dropna(
        subset=["Date", "Amount"]
    )

    if df.empty:
        return None

    return df


def category_summary():
    print("\n--- CATEGORY-WISE SUMMARY ---")

    df = load_data()

    if df is None:
        print("No expenses found.")
        return

    category_totals = (
        df.groupby("Category")["Amount"]
        .sum()
        .sort_values(ascending=False)
    )

    print()

    for category, total in category_totals.items():
        print(f"{category:<20} ₹{total:.2f}")



def total_expense():
    print("\n--- TOTAL EXPENSE ---")

    df = load_data()

    if df is None:
        print("No expenses found.")
        return

    total = df["Amount"].sum()

    print(f"\nTotal Expense: ₹{total:.2f}")



def expense_statistics():
    print("\n--- EXPENSE STATISTICS ---")

    df = load_data()

    if df is None:
        print("No expenses found.")
        return

    total = df["Amount"].sum()
    count = len(df)
    average = df["Amount"].mean()
    highest = df["Amount"].max()
    lowest = df["Amount"].min()

    highest_expense = df.loc[
        df["Amount"].idxmax()
    ]

    lowest_expense = df.loc[
        df["Amount"].idxmin()
    ]

    print()
    print(f"Number of Expenses : {count}")
    print(f"Total Expense      : ₹{total:.2f}")
    print(f"Average Expense    : ₹{average:.2f}")
    print(f"Highest Expense    : ₹{highest:.2f}")
    print(f"Lowest Expense     : ₹{lowest:.2f}")

    print("\nHighest Expense Details:")
    print(
        f"Date        : "
        f"{highest_expense['Date'].strftime('%d-%m-%Y')}"
    )
    print(
        f"Description : "
        f"{highest_expense['Description']}"
    )
    print(
        f"Category    : "
        f"{highest_expense['Category']}"
    )

    print("\nLowest Expense Details:")
    print(
        f"Date        : "
        f"{lowest_expense['Date'].strftime('%d-%m-%Y')}"
    )
    print(
        f"Description : "
        f"{lowest_expense['Description']}"
    )
    print(
        f"Category    : "
        f"{lowest_expense['Category']}"
    )




def monthly_summary():
    print("\n--- MONTHLY SUMMARY ---")

    df = load_data()

    if df is None:
        print("No expenses found.")
        return

    df["Month"] = df["Date"].dt.to_period("M")

    monthly_totals = (
        df.groupby("Month")["Amount"]
        .sum()
        .sort_index()
    )

    print()

    for month, total in monthly_totals.items():

        month_name = month.strftime("%B %Y")

        print(
            f"{month_name:<20} ₹{total:.2f}"
        )




def automated_insights():
    print("\n--- AUTOMATED INSIGHTS ---")

    df = load_data()

    if df is None:
        print("No expenses found.")
        return

    total = df["Amount"].sum()
    average = df["Amount"].mean()

    category_totals = (
        df.groupby("Category")["Amount"]
        .sum()
    )

    highest_category = category_totals.idxmax()
    highest_category_amount = category_totals.max()

    highest_expense = df.loc[
        df["Amount"].idxmax()
    ]

    print()

    print(
        f"• You have recorded {len(df)} expenses."
    )

    print(
        f"• Your total spending is ₹{total:.2f}."
    )

    print(
        f"• Your average expense is ₹{average:.2f}."
    )

    print(
        f"• You spent the most on "
        f"{highest_category} "
        f"(₹{highest_category_amount:.2f})."
    )

    print(
        f"• Your highest single expense was "
        f"₹{highest_expense['Amount']:.2f} "
        f"for {highest_expense['Description']}."
    )



def generate_graphs():
    print("\n--- GENERATING GRAPHS ---")

    df = load_data()

    if df is None:
        print("No expenses found.")
        return

   

    category_totals = (
        df.groupby("Category")["Amount"]
        .sum()
        .sort_values(ascending=False)
    )

    plt.figure(figsize=(9, 5))

    category_totals.plot(
        kind="bar"
    )

    plt.title("Category-wise Expenses")
    plt.xlabel("Category")
    plt.ylabel("Amount (₹)")
    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.savefig(
        "category_expenses.png"
    )

    plt.close()

    

    df["Month"] = df["Date"].dt.to_period("M")

    monthly_totals = (
        df.groupby("Month")["Amount"]
        .sum()
        .sort_index()
    )

    monthly_labels = [
        month.strftime("%B %Y")
        for month in monthly_totals.index
    ]

    plt.figure(figsize=(9, 5))

    plt.bar(
        monthly_labels,
        monthly_totals.values
    )

    plt.title("Monthly Expenses")
    plt.xlabel("Month")
    plt.ylabel("Amount (₹)")
    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.savefig(
        "monthly_expenses.png"
    )

    plt.close()

    print("\n✓ Graphs generated successfully!")



def generate_report():
    print("\n--- GENERATE REPORT ---")

    df = load_data()

    if df is None:
        print("No expenses found.")
        return

    total = df["Amount"].sum()
    count = len(df)
    average = df["Amount"].mean()
    highest = df["Amount"].max()
    lowest = df["Amount"].min()

    category_totals = (
        df.groupby("Category")["Amount"]
        .sum()
        .sort_values(ascending=False)
    )

    highest_category = category_totals.idxmax()
    highest_category_amount = category_totals.max()

    highest_expense = df.loc[
        df["Amount"].idxmax()
    ]

    with open(
        "expense_report.txt",
        "w",
        encoding="utf-8"
    ) as file:

        file.write("=" * 60 + "\n")
        file.write(
            "              EXPENSE TRACKER REPORT\n"
        )
        file.write("=" * 60 + "\n\n")

        # General Summary
        file.write("GENERAL SUMMARY\n")
        file.write("-" * 60 + "\n")

        file.write(
            f"Total Expenses   : {count}\n"
        )

        file.write(
            f"Total Amount     : ₹{total:.2f}\n"
        )

        file.write(
            f"Average Expense  : ₹{average:.2f}\n"
        )

        file.write(
            f"Highest Expense  : ₹{highest:.2f}\n"
        )

        file.write(
            f"Lowest Expense   : ₹{lowest:.2f}\n"
        )

        # Category Summary
        file.write("\nCATEGORY SUMMARY\n")
        file.write("-" * 60 + "\n")

        for category, amount in category_totals.items():

            file.write(
                f"{category:<20} ₹{amount:.2f}\n"
            )

        # Insights
        file.write("\nINSIGHTS\n")
        file.write("-" * 60 + "\n")

        file.write(
            f"Highest spending category: "
            f"{highest_category} "
            f"(₹{highest_category_amount:.2f})\n"
        )

        file.write(
            f"Highest single expense: "
            f"₹{highest_expense['Amount']:.2f} "
            f"for {highest_expense['Description']}\n"
        )

        file.write("\n")
        file.write("=" * 60 + "\n")

        file.write(
            "Report generated successfully.\n"
        )

    print("\n✓ Report generated successfully!")
    print("✓ File created: expense_report.txt")



def show_menu():

    print()
    print("=" * 75)
    print("                        EXPENSE TRACKER")
    print("=" * 75)

    print(
        "[1] Add Expense          "
        "[2] View Expenses          "
        "[3] Category Summary"
    )

    print()

    print(
        "[4] Total Expense        "
        "[5] Monthly Summary        "
        "[6] Generate Report"
    )

    print()

    print(
        "[7] Statistics           "
        "[8] Insights               "
        "[9] Generate Graphs"
    )

    print()

    print(
        "                              [10] Exit"
    )

    print("=" * 75)




def main():

    print("=" * 60)
    print("          AUTOMATED EXPENSE TRACKER")
    print("       Data Processing & Automation")
    print("=" * 60)

    while True:

        show_menu()

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            category_summary()

        elif choice == "4":
            total_expense()

        elif choice == "5":
            monthly_summary()

        elif choice == "6":
            generate_report()

        elif choice == "7":
            expense_statistics()

        elif choice == "8":
            automated_insights()

        elif choice == "9":
            generate_graphs()

        elif choice == "10":
            print(
                "\nThank you for using Expense Tracker!"
            )
            break

        else:
            print(
                "\nInvalid choice. Please select 1-10."
            )




if __name__ == "__main__":
    main()