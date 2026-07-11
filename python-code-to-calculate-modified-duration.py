def bond_price(face_value, coupon_rate, yield_rate, maturity):
    """
    Calculate the price of a coupon-bearing bond.

    Parameters
    ----------
    face_value : float
        Face value (par value) of the bond.

    coupon_rate : float
        Annual coupon rate (e.g. 0.08 for 8%).

    yield_rate : float
        Annual yield to maturity (decimal).

    maturity : int
        Number of years until maturity.

    Returns
    -------
    float
        Bond price.
    """

    coupon = face_value * coupon_rate

    price = 0.0

    for t in range(1, maturity + 1):

        if t == maturity:
            cashflow = coupon + face_value
        else:
            cashflow = coupon

        pv = cashflow / ((1 + yield_rate) ** t)

        price += pv

    return price







    