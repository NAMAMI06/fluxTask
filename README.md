# Automated Expense Tracker CLI

## Project Overview

Automated Expense Tracker is a Python-based command-line application designed to record, manage, analyze, and visualize daily expenses.

The application stores expense data permanently in a CSV file and uses Pandas for data processing and Matplotlib for generating expense graphs.

---

## Features

- Add daily expenses
- Categorize expenses
- Store expenses permanently in CSV format
- View all recorded expenses
- Calculate total expenses
- Generate category-wise expense summary
- Generate monthly expense summary
- Calculate average, highest, and lowest expenses
- Generate automated spending insights
- Generate category-wise expense graph
- Generate monthly expense graph
- Export a detailed expense report
- Validate date, amount, and category inputs

---

## Technologies Used

- Python
- CSV
- Pandas
- Matplotlib
- DateTime

---

## Requirements

- Python 3.x
- Pandas
- Matplotlib

Install the required libraries using:

```bash
pip install pandas matplotlib
Project Structure
Automated Expense Tracker/
│
├── expense_tracker.py
├── expenses.csv
├── expense_report.txt
├── category_expenses.png
├── monthly_expenses.png
└── README.md
How to Run
Open the project folder in VS Code or terminal.
Make sure Python is installed.
Install the required libraries:
pip install pandas matplotlib
Run the application:
python expense_tracker.py
The application will display the main menu.
Select an option by entering its corresponding number.
Menu Options
[1] Add Expense
[2] View Expenses
[3] Category Summary

[4] Total Expense
[5] Monthly Summary
[6] Generate Report

[7] Statistics
[8] Insights
[9] Generate Graphs

[10] Exit
Expense Categories

The application supports the following expense categories:

Food
Transport
Utilities
Shopping
Education
Entertainment
Healthcare
Other
Data Storage

All expense records are stored in:

expenses.csv

Each expense record contains:

Date
Description
Amount
Category

The CSV file allows expense data to remain saved even after the program is closed.

Application Functions
1. Add Expense

Allows the user to enter:

Date
Description
Amount
Category

The entered expense is automatically stored in the CSV file.

2. View Expenses

Displays all recorded expenses in a structured table containing:

Date
Description
Amount
Category
3. Category Summary

Calculates the total amount spent in each category and displays the categories in descending order of spending.

4. Total Expense

Calculates and displays the total amount spent across all recorded expenses.

5. Monthly Summary

Groups expenses by month and calculates the total spending for each month.

6. Generate Report

Creates a detailed text report:

expense_report.txt

The report contains:

Total number of expenses
Total amount spent
Average expense
Highest expense
Lowest expense
Category-wise spending
Highest spending category
Highest single expense
7. Statistics

Provides basic expense statistics including:

Number of expenses
Total expense
Average expense
Highest expense
Lowest expense
Details of the highest expense
Details of the lowest expense
8. Insights

Generates automated spending insights such as:

Number of recorded expenses
Total spending
Average expense
Highest spending category
Highest single expense
9. Generate Graphs

Generates two graphs using Matplotlib:

category_expenses.png
monthly_expenses.png

The category-wise graph shows the amount spent in different expense categories.

The monthly graph shows the total amount spent in each month.

Data Processing

Pandas is used to process and analyze the stored expense data.

The application uses operations such as:

Grouping data by category
Grouping data by month
Calculating totals
Calculating averages
Finding maximum and minimum expenses
Sorting expense data
Converting and validating dates
Handling invalid numerical values
Input Validation

The application validates user input to prevent invalid data.

Examples:

Invalid dates are rejected.
Negative or zero expense amounts are rejected.
Invalid category numbers are rejected.
Non-numeric amount inputs are handled safely.
Invalid menu choices are rejected.
Generated Outputs

The application can generate the following files:

Expense Data

expenses.csv

Stores all expense records.

Expense Report

expense_report.txt

Contains a detailed summary and spending insights.

Category Graph

category_expenses.png

Visualizes category-wise spending.

Monthly Graph

monthly_expenses.png

Visualizes monthly spending.

Purpose of the Project

The main purpose of this project is to demonstrate the practical use of Python for:

File handling
CSV data storage
Data processing
Data analysis
Automation
Data visualization
Input validation
Command-line application development
Key Concepts Demonstrated

This project demonstrates practical implementation of:

Functions
Loops
Conditional statements
Exception handling
File handling
CSV handling
Date and time processing
Pandas DataFrames
Data grouping and aggregation
Matplotlib visualization
Command-line interface development
Future Improvements

Possible future improvements include:

Budget tracking
Budget limit alerts
Expense editing and deletion
Search and filtering
Export reports to PDF
More advanced spending analysis
Yearly expense comparison
Interactive dashboards
Conclusion

Automated Expense Tracker CLI provides a simple and practical way to record and analyze personal expenses.

The project combines Python, CSV file handling, Pandas, and Matplotlib to create an automated expense management and data analysis system through a command-line interface.

It demonstrates how Python can be used for data processing, automation, file management, statistical analysis, and data visualization in a practical real-world application.