from cd_account import create_cd_account
from savings_account import create_savings_account

def main():
    """This function prompts the user to enter the savings and CD account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """

    # Prompt the user for the savings balance
    savings_balance = float(input("Please enter the savings account balance: "))
    
    # Prompt the user for the interest rate
    savings_interest = float(input("Please enter the annual interest rate for savings (as a decimal, e.g., 0.05 for 5%): "))
    
    # Prompt the user for the number of months
    savings_months = int(input("Please enter the number of months for the savings account: "))
    
    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, savings_interest_earned = create_savings_account(savings_balance, savings_interest, savings_months)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    print(f"Savings Account: Interest earned over {savings_months} months: ${savings_interest_earned:.2f}")
    print(f"Savings Account: Updated balance after interest: ${updated_savings_balance:.2f}")

    # Prompt the user for the CD balance
    cd_balance = float(input("Please enter the CD account balance: "))
    
    # Prompt the user for the interest rate
    cd_interest = float(input("Please enter the annual interest rate for CD (as a decimal, e.g., 0.05 for 5%): "))
    
    # Prompt the user for the number of months
    cd_months = int(input("Please enter the number of months for the CD account: "))
    
    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, cd_interest_earned = create_cd_account(cd_balance, cd_interest, cd_months)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    print(f"CD Account: Interest earned over {cd_months} months: ${cd_interest_earned:.2f}")
    print(f"CD Account: Updated balance after interest: ${updated_cd_balance:.2f}")

if __name__ == "__main__":
    main()

