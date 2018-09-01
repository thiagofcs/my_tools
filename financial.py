def calc_amount(pr, mo, ir):
    """
    Calculates compounding interest and returns both period and amount calculated
    after each period
    :param pr: value for principal
    :param mo: number of periods to walk trough
    :param ir: value for the interest rate
    :return: [x] list of period and [y] list of accumulated amount
    """
    mo += 1
    amount = 0
    x = list()
    y = list()
    for month in range(1, mo):
        amount = amount + pr * (1.0 + ir) ** month
        x.append(month)
        y.append(amount)
    return x, y
