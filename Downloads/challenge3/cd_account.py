from Account import Account  # Import the Account class from the Account.py file

def create_cd_account(balance, interest_rate, months):
    """Creates a CD account, calculates interest earned, and updates the account balance.

    Args:
        balance (float): The initial CD account balance.
        interest_rate (float): The APR interest rate for the CD account.
        months (int): The length of months for the CD.

    Returns:
        tuple: A tuple containing the updated CD account balance after adding the interest earned
               and the interest earned.
    """
    # Create an instance of the `Account` class and pass in the balance and interest rate
    cd_account = Account(balance, interest_rate)

    # Calculate interest earned (assuming simple interest)
    interest_earned = cd_account.balance * (cd_account.interest_rate / 12) * months

    # Update the CD account balance by adding the interest earned
    updated_balance = cd_account.balance + interest_earned

    # Pass the updated_balance to the set_balance method using the instance of the Account class.
    cd_account.set_balance(updated_balance)

    # Since the original prompt suggests a set_interest method but the class has set_interest_rate,
    # let's assume we're updating the interest rate with the earned interest rate for the period.
    
    cd_account.set_interest_rate(interest_earned / cd_account.balance)

    # Return the updated balance and interest earned.
    return updated_balance, interest_earned

# Example usage:
# This will print the updated balance after interest is applied and the interest earned.
print(create_cd_account(1000, 0.05, 6))
