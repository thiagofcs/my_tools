def compound_interest(principal, period, rate):
    """
    Calculates compounding interest and returns both period and amount calculated
    after each period iteration
    :param principal: principal value
    :param period: number of periods to iterate with
    :param rate: interest rate value
    :return: [x] list of period and [y] list of accumulated amount
    """
    amount = 0
    x = y = list()
    x.append(1)
    y.append(principal)
    for p in range(1, period+1):
        amount = amount + principal * (1.0 + rate) ** p
        x.append(p)
        y.append(amount)
    return x, y


