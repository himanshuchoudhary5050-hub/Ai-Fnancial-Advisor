from config import client, MODEL_NAME


def chatbot_response(question):

    try:
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=question
        )

        return response.text

    except Exception as e:
        return f"AI chatbot error: {str(e)}"


def get_financial_advice(income, expenses, savings, debt, goal):

    prompt = f"""
    A user has the following financial details:

    Income: {income}
    Expenses: {expenses}
    Savings: {savings}
    Debt: {debt}
    Goal: {goal}

    Provide simple financial advice for budgeting, saving, and investing.
    """

    try:
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=prompt
        )

        return response.text

    except Exception as e:
        return f"AI advice error: {str(e)}"
