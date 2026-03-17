import streamlit as st

from finance_analysis import savings_ratio, debt_ratio, emergency_fund, monthly_goal_saving
from ai_advisor import get_financial_advice, chatbot_response
from visualization import income_expense_chart, savings_chart
from utils import format_advice


st.set_page_config(page_title="AI Financial Advisor", layout="wide")

st.title("AI Financial Advisor")


# Sidebar Inputs
st.sidebar.header("Financial Inputs")

income = st.sidebar.number_input("Monthly Income", min_value=0)

expenses = st.sidebar.number_input("Monthly Expenses", min_value=0)

savings = st.sidebar.number_input("Current Savings", min_value=0)

debt = st.sidebar.number_input("Current Debt", min_value=0)

goal = st.sidebar.text_input("Financial Goal")

goal_amount = st.sidebar.number_input("Goal Amount", min_value=0)

goal_months = st.sidebar.number_input("Months to Achieve Goal", min_value=1)


# Financial Analysis
if st.sidebar.button("Analyze Finances"):

    sr = savings_ratio(income, expenses)

    dr = debt_ratio(debt, income)

    ef = emergency_fund(expenses)

    monthly_goal = monthly_goal_saving(goal_amount, goal_months)

    st.subheader("Financial Metrics")

    col1, col2, col3 = st.columns(3)

    col1.metric("Savings Ratio", f"{sr:.2f}")

    col2.metric("Debt Ratio", f"{dr:.2f}")

    col3.metric("Emergency Fund Needed", f"₹{ef}")



    st.subheader("Goal Planning")

    st.write(f"Monthly saving required for goal: ₹{monthly_goal}")



    st.subheader("Charts")

    fig1 = income_expense_chart(income, expenses)

    st.pyplot(fig1)

    fig2 = savings_chart(savings, debt)

    st.pyplot(fig2)



    st.subheader("AI Financial Advice")

    advice = get_financial_advice(income, expenses, savings, debt, goal)

    formatted = format_advice(advice)

    for line in formatted:

        st.write(line)



# Chatbot Section
st.subheader("AI Financial Chatbot")

question = st.text_input("Ask a financial question")

if st.button("Ask AI"):

    answer = chatbot_response(question)

    st.write(answer)
