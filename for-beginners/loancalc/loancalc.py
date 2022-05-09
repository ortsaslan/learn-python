import math


def calc_loan_principal(payment, interest, period):
    rate = calc_interest_rate(interest)
    principal = payment / (((rate * ((1 + rate) ** period)) / (((1 + rate) ** period) - 1)))
    return round(principal)

def calc_loan_payment(principal, interest, period):
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

def give_answer(msg_type, data):
    msg_repay_period = "It will take {} to repay this loan!"
    msg_annuity_payment = "Your monthly payment = {}!"
    msg_loan_principal = "Your loan principal = {}!"
    if msg_type == "n":
        answer = msg_repay_period.format(data)
    elif msg_type == "a":
        answer = msg_annuity_payment.format(data)
    elif msg_type == "p":
        answer = msg_loan_principal.format(data)
    return answer

    
def main():
    
    # Which value to calculate
    query_to_calc = input('''What do you want to calculate?
    type "n" for number of monthly payments,
    type "a" for annuity monthly payment amount,
    type "p" for loan principal:\n''')

    # Case: Period to repay loan
    if query_to_calc == 'n':
        loan_principal = float(input("Enter the loan principal:\n"))
        loan_payment = float(input("Enter the monthly payment:\n"))
        loan_interest = float(input("Enter the loan interest:\n"))
        loan_period = math.ceil(calc_loan_period(loan_principal, loan_interest, loan_payment))
        if loan_period == 1:
            period = "1 month"
            print(give_answer("n", period))
        elif loan_period < 12:
            period = loan_period
            print(give_answer("n", period))
        elif loan_period == 12:
            period = "1 year"
            print(give_answer("n", period))
        elif loan_period > 12:
            years = loan_period // 12
            months = loan_period - (years * 12)
            if years == 1:
                period_years = f"{years} year"
            else:
                period_years = f"{years} years"
            if months == 1:
                period_months = f"{months} month"
            else:
                period_months = f"{months} months"
            period = f"{period_years} and {period_months}"
            print(give_answer("n", period))
    
    # Case: Annuity monthly payment
    elif query_to_calc == 'a':
        loan_principal = float(input("Enter the loan principal:\n"))
        loan_period = float(input("Enter the number of periods:\n"))
        loan_interest = float(input("Enter the loan interest:\n"))
        loan_payment = calc_loan_payment(loan_principal, loan_interest, loan_period)
        print(give_answer("a", loan_payment))
    
    # Case: Loan principal
    elif query_to_calc == "p":
        loan_payment = float(input("Enter the annuity payment:\n"))
        loan_period = float(input("Enter the number of periods:\n"))
        loan_interest = float(input("Enter the loan interest:\n"))
        loan_principal = calc_loan_principal(loan_payment, loan_interest, loan_period)
        print(give_answer("p", loan_principal))


main()