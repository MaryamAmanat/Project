import os
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Create data directory if it doesn't exist
if not os.path.exists("data"):
    os.makedirs("data")

def data_entry():
    st.subheader("Data Entry")

    # Select month and date
    month = st.selectbox("Select Month", ["January", "February", "March", "April", "May", "June", "July",
                                          "August", "September", "October", "November", "December"])
    date = st.date_input("Select Date")

    # Create filename based on month and date
    filename = f"data/{month}_{date.day}.csv"

    # Check if file already exists, create new file if not
    if not os.path.isfile(filename):
        with open(filename, "w") as f:
            f.write("Income,Type,Expense,Comments\n")
            st.success(f"New file created: {filename}")

    # Take income details
    st.subheader("Income Details")
    income = st.number_input("Income Amount (USD)", min_value=0.0, step=0.01)
    income_type = st.selectbox("Income Type", ["Salary", "Blog", "Other Income"])

    # Take expense details
    st.subheader("Expense Details")
    expense = st.number_input("Expense Amount (USD)", min_value=0.0, step=0.01)
    expense_type = st.selectbox("Expense Type", ["Grocery", "Utility", "Car", "Rent", "Other"])
    comments = st.text_area("Comments")

    # Append data to the file
    with open(filename, "a") as f:
        f.write(f"{income},{income_type},{expense},{expense_type},{comments}\n")
    st.success("Data entry added successfully!")

def data_visualization():
    st.subheader("Data Visualization")

    # Read all the CSV files in the 'data' directory
    csv_files = [file for file in os.listdir("data") if file.endswith(".csv")]

    if csv_files:
        # Combine all the CSV data into a single DataFrame
        df = pd.concat([pd.read_csv(os.path.join("data", file)) for file in csv_files])

        # Group the data by income type and calculate the total income
        grouped_income = df.groupby("Type").sum().reset_index()

        # Create a bar chart for income
        plt.figure(figsize=(10, 6))
        plt.bar(grouped_income["Type"], grouped_income["Income"])
        plt.xlabel("Income Type")
        plt.ylabel("Total Income (USD)")
        plt.title("Income by Type")
        st.pyplot(plt)

        # Group the data by expense type and calculate the total expense
        grouped_expense = df.groupby("Expense").sum().reset_index()

        # Create a bar chart for expense
        plt.figure(figsize=(10, 6))
        plt.bar(grouped_expense["Expense"], grouped_expense["Expense"])
        plt.xlabel("Expense Type")
        plt.ylabel("Total Expense (USD)")
        plt.title("Expense by Type")
        st.pyplot(plt)

        # Show the raw data table
        st.subheader("Raw Data")
        st.dataframe(df)
    else:
        st.warning("No data files found.")

def main():
    st.title("Expense Tracker App")
    st.write("Welcome to the Expense Tracker App!")

    option = st.sidebar.selectbox("Select Option", ["Data Entry", "Data Visualization"])

    if option == "Data Entry":
        data_entry()
    elif option == "Data Visualization":
        data_visualization()

if __name__ == '__main__':
    main()
