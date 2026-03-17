def savings_ratio(income, expenses):
    if income == 0:
        return 0
    return (income - expenses) / income


def debt_ratio(debt, income):
    if income == 0:
        return 0
    return debt / income


def emergency_fund(expenses):
    return expenses * 6


def monthly_goal_saving(goal_amount, months):
    if months == 0:
        return 0
    return goal_amount / months
