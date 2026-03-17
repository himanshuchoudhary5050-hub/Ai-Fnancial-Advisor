import matplotlib.pyplot as plt


def income_expense_chart(income, expenses):

    labels = ["Income", "Expenses"]
    values = [income, expenses]

    fig, ax = plt.subplots()

    ax.bar(labels, values)

    ax.set_title("Income vs Expenses")

    return fig


def savings_chart(savings, debt):

    labels = ["Savings", "Debt"]
    values = [savings, debt]

    fig, ax = plt.subplots()

    ax.pie(values, labels=labels, autopct="%1.1f%%")

    ax.set_title("Savings vs Debt Distribution")

    return fig
