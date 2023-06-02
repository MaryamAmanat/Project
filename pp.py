import os
import streamlit as st
import pandas as pd

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
            f.write("Date,Income Type,Expense Type,Comments\n")
            st.success(f"New file created: {filename}")

    # Take income details
    st.subheader("Income Details")
    salary = st.number_input("Salary (USD)", min_value=0.0, step=0.01)
    blog = st.number_input("Blog Income (USD)", min_value=0.0, step=0.01)
    other_income = st.number_input("Other Income (USD)", min_value=0.0, step=0.01)

    # Take expense details
    st.subheader("Expense Details")
    rent = st.number_input("Rent (USD)", min_value=0.0, step=0.01)
    car = st.number_input("Car Expense (USD)", min_value=0.0, step=0.01)
    grocery = st.number_input("Grocery Expense (USD)", min_value=0.0, step=0.01)
    other_expense = st.number_input("Other Expense (USD)", min_value=0.0, step=0.01)

    comments = st.text_area("Comments")

    # Append data to the file
    with open(filename, "a") as f:
        f.write(f"{date},{salary},{blog},{other_income},{rent},{car},{grocery},{other_expense},{comments}\n")
    st.success("Data entry added successfully!")

def display_report():
    st.subheader("Data Report")

    # Read all the CSV files in the 'data' directory
    csv_files = [file for file in os.listdir("data") if file.endswith(".csv")]

    if csv_files:
        # Combine all the CSV data into a single DataFrame
        df = pd.concat([pd.read_csv(os.path.join("data", file)) for file in csv_files])

        # Display the report
        st.dataframe(df)
    else:
        st.warning("No data files found.")

def main():
    st.title("Income and Expense Tracker")
    st.write("Welcome to the Income and Expense Tracker!")

    option = st.sidebar.selectbox("Select Option", ["Data Entry", "Display Report"])

    if option == "Data Entry":
        data_entry()
    elif option == "Display Report":
        display_report()

if __name__ == '__main__':
    main()
