# Macaulay Duration

# Formula


# The Macaulay Duration is a measure of the weighted average time until a bond's cash flows are received. It is calculated using the following formula:



def macaulay_duration(face_value,
                      coupon_rate,
                      yield_rate,
                      maturity):
    # """
    # Calculate Macaulay Duration.
    # """

    coupon = face_value * coupon_rate

    price = bond_price(face_value,
                       coupon_rate,
                       yield_rate,
                       maturity)

    weighted_sum = 0.0

    for t in range(1, maturity + 1):

        if t == maturity:
            cashflow = coupon + face_value
        else:
            cashflow = coupon

        pv = cashflow / ((1 + yield_rate) ** t)

        weighted_sum += t * pv

    duration = weighted_sum / price

    return duration


def macaulay_duration(face_value,
                      coupon_rate,
                      yield_rate,
                      maturity):
    """
    Calculate Macaulay Duration.
    """

    coupon = face_value * coupon_rate

    price = bond_price(face_value,
                       coupon_rate,
                       yield_rate,
                       maturity)

    weighted_sum = 0.0

    for t in range(1, maturity + 1):

        if t == maturity:
            cashflow = coupon + face_value
        else:
            cashflow = coupon

        pv = cashflow / ((1 + yield_rate) ** t)

        weighted_sum += t * pv

    duration = weighted_sum / price

    return duration