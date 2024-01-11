from Account import Account  # Import the Account class from the Account.py file

def create_savings_account(balance, interest_rate, months):
    """Creates a savings account, calculates interest earned, and updates the account balance.

    Args:
        balance (float): The initial savings account balance.
        interest_rate (float): The APR interest rate for the savings account.
        months (int): The length of months to determine the amount of interest.

    Returns:
        tuple: The updated savings account balance after adding the interest earned,
               and the interest earned.
    """
    # Create an instance of the `Account` class with the initial balance and interest rate
    savings_account = Account(balance, interest_rate)

    # Calculate the interest earned using simple interest formula: A = P(1 + rt)
    # where P is the principal amount (initial balance), r is the annual interest rate,
    # and t is the time in years. Since we're given months, we convert it to years by dividing by 12.
    interest_earned = savings_account.balance * (savings_account.interest_rate * (months / 12))

    # Update the savings account balance by adding the interest earned
    updated_balance = savings_account.balance + interest_earned

    # Assuming the `Account` class has a method to update the balance.
    
    savings_account.set_balance(updated_balance)

    # Assuming the `Account` class has a method to set the interest.
    
    savings_account.set_interest(interest_earned)

    # Return the updated balance and interest earned as a tuple
    return updated_balance, interest_earned


