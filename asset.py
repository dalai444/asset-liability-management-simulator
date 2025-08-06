import numpy as np

# Basic function that creates an array of the incoming cash flow for a bond based on its face, coupon, frequency, and maturity
def bond_cashflows(face, coupon_rate, freq, maturity):
    num_periods = maturity * freq
    coupon = face * coupon_rate / freq

    cashflows = np.full(num_periods, coupon)

    cashflows[-1] += face # Adding in the full value of the bond at the very end

    return cashflows