import streamlit as st
import plotly.graph_objects as go

def generate_expense_report(expenses):
    total_expenses = sum(expenses)
    average_expense = total_expenses / len(expenses)

    st.write("Expense Report")
    st.write("--------------------")
    st.write("Total Expenses: $", total_expenses)
    st.write("Average Expense: $", average_expense)
    st.write("--------------------")
    st.write("Individual Expenses:")
    for index, expense in enumerate(expenses, start=1):
        st.write(f"Expense {index}: $", expense)

def generate_expense_chart(expenses):
    expense_labels = [f"Expense {i+1}" for i in range(len(expenses))]

    fig = go.Figure(data=[go.Bar(x=expense_labels, y=expenses)])
    fig.update_layout(title="Expense Distribution", xaxis_title="Expenses", yaxis_title="Amount")
    st.plotly_chart(fig)

def main():
    st.title("Expense Report Generator")
    st.write("Enter your expenses below:")

    
    expense_list = []

    while True:
        expense = st.number_input("Expense:", value=0.0, step=0.01)
        expense_list.append(expense)

        add_more = st.button("Add More Expenses")
        if not add_more:
            break

    if expense_list:
        generate_expense_report(expense_list)
        generate_expense_chart(expense_list)
    else:
        st.write("No expenses entered.")

if __name__ == '__main__':
    main()
