import math
import argparse

# =========================
# Parsing console arguments
# =========================
argparser = argparse.ArgumentParser(description="Credit calculator")
argparser.add_argument("--type")
argparser.add_argument("--payment", type=int)
argparser.add_argument("--principal", type=int)
argparser.add_argument("--periods", type=int)
argparser.add_argument("--interest", type=float)
args = argparser.parse_args()

# ===============================
# Functions for main calculations
# ===============================
def calc_loan_principal(payment, interest, period):
    rate = calc_interest_rate(interest)
    principal = payment / (((rate * ((1 + rate) ** period)) / (((1 + rate) ** period) - 1)))
    return math.floor(principal)

def calc_diff_payment(principal, interest, period):
    diff_payments = []
    rate = calc_interest_rate(interest)
    for month in range(period):
        paymnt = (principal / period) + (rate * (principal - ((principal * ((month + 1) - 1)) / period)))
        diff_payments.append(math.ceil(paymnt))
    return diff_payments

def calc_annuity_payment(principal, interest, period):
    rate = calc_interest_rate(interest)
    payment = principal * (((rate * ((1 + rate) ** period)) / (((1 + rate) ** period) - 1)))
    return math.ceil(payment)

def calc_loan_period(principal, interest, payment):
    rate = calc_interest_rate(interest)
    period = math.log(payment / (payment - rate * principal), 1 + rate)
    return period

def calc_interest_rate(percent_interest):
    rate = percent_interest / (12 * 100)
    return rate

def calc_overpayment(principal, period, payment):
    if isinstance(payment, list):
        overpayment = sum(payment) - principal
    else:
        overpayment = (period * payment) - principal
    return overpayment

# =======================================
# Functions for result and error messages
# =======================================
def msg_calc_result(calc_type, data):
    msg_repay_period = "It will take {} to repay this loan!"
    msg_annuity_payment = "Your annuity payment = {}!"
    msg_loan_principal = "Your loan principal = {}!"
    if calc_type == "period":
        msg = msg_repay_period.format(data)
    elif calc_type == "annuity":
        msg = msg_annuity_payment.format(data)
    elif calc_type == "principal":
        msg = msg_loan_principal.format(data)
    print(msg)

def msg_diff_payments(month, data):
    msg = f"Month {month}: payment is {data}"
    print(msg)

def msg_overpayment(data):
    print(f"Overpayment = {data}")

def msg_error():
    print("Incorrect parameters")


def main():
    # Variables from arguments
    payment_type = args.type
    loan_principal = args.principal
    loan_period = args.periods
    loan_payment = args.payment
    loan_interest = args.interest

    # Differentiated payments
    if payment_type == "diff":
        # Check for all necessary arguments for payment calculation
        if loan_principal and loan_interest and loan_period:
            paymnt = calc_diff_payment(loan_principal, loan_interest, loan_period)
            for i in range(len(paymnt)):
                msg_diff_payments(i + 1, paymnt[i])
            overpmnt = calc_overpayment(loan_principal, loan_period, paymnt)
            msg_overpayment(overpmnt)
        else:
            msg_error()
    # Annuity payment
    elif payment_type == "annuity":
        # Check for all necessary arguments for payment calculation
        if loan_principal and loan_interest and loan_period:
            paymnt = calc_annuity_payment(loan_principal, loan_interest, loan_period)
            msg_calc_result("annuity", paymnt)
            # Calculating overpayment and according output message
            overpmnt = calc_overpayment(loan_principal, loan_period, paymnt)
            msg_overpayment(overpmnt)
        # Loan Principal
        elif loan_payment and loan_interest and loan_period:
            princpl = calc_loan_principal(loan_payment, loan_interest, loan_period)
            msg_calc_result("principal", princpl)
            paymnt = calc_annuity_payment(princpl, loan_interest, loan_period)
            # Calculating overpayment and according output message
            overpmnt = calc_overpayment(princpl, loan_period, paymnt)
            msg_overpayment(overpmnt)
        # Period to repay loan
        elif loan_principal and loan_interest and loan_payment:
            period = calc_loan_period(loan_principal, loan_interest, loan_payment)
            period = math.ceil(period)
            # Make valid months/years message output
            if period == 1:
                term = "1 month"
                msg_calc_result("period", term)
            elif period < 12:
                term = period
                msg_calc_result("period", term)
            elif period == 12:
                term = "1 year"
                msg_calc_result("period", term)
            elif period > 12:
                years = period // 12
                months = period - (years * 12)
                if years == 1:
                    period_years = f"{years} year"
                else:
                    period_years = f"{years} years"
                if months == 1:
                    period_months = f"{months} month"
                else:
                    period_months = f"{months} months"
                if months == 0:
                    term = f"{period_years}"
                else:
                    term = f"{period_years} and {period_months}"
                msg_calc_result("period", term)
            # Calculating overpayment and according output message
            overpmnt = calc_overpayment(loan_principal, period, loan_payment)
            msg_overpayment(overpmnt)
        else:
            msg_error()
    else:
        msg_error()


main()
