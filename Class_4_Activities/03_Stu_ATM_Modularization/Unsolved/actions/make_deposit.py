import sys
import questionary

def make_deposit(account):
    """Deposit Dialog.

        This application captures the deposit amount from the user, validates the amount,
        adjusts the account balance for the deposit and returns the adjusted account.

        Args:
            account(dict): user account information including pin and balance.

        Return:
            account(dict): user account with balance adjusted for deposit

    """
    # Use questionary to capture the deposit and set equal to amount variable. Set amount as a floating point number.
    amount = questionary.text("How much would you like to deposit?").ask()
    amount = float(amount)

    # Validates amount of deposit. If true processes deposit, else returns error.
    if amount > 0.0:
        account["balance"] = account["balance"] + amount
        print(f"Your deposit was successful.")
        return account
    else:
        sys.exit(f"This is not a valid deposit amount. Please try again.")
