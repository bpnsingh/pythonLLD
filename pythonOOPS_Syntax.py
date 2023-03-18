class BankAccount:
    """
    This class represents a bank account.
    Attributes: balance,account_number,owner
    Methods: add_funds, withdraw_fund,check_fund
    """
    __MIN_BALANCE = 100
    def __init__(self,owner,account_number,balance=0):
        self._owner = owner
        self._account_number = account_number
        if balance < self.__MIN_BALANCE:
            raise ValueError("Balance is very low,minimum amount to open account is 100")
        else:
            self._balance = balance

    def __eq__(self, other):
        return True if self._account_number == other._account_number else False

    def __str__(self):
        return f"""
        Bank Account:
            Account Owner: {self._owner}
            Account Number: {self._account_number}
            Current Balance: {self._balance}
        """

    def __repr__(self):
        return f"BankAccount(owner='{self._owner}', " \
               f"account_number={self._account_number}, " \
               f"balance={self._balance})"

    def __getitem__(self, key):
        return getattr(self, key)

a = BankAccount('Bipin',123,200)
print(str(a))
print(repr(a))
print(a["_owner"])

"""
Output:
        Bank Account:
            Account Owner: Bipin
            Account Number: 123
            Current Balance: 200
        
BankAccount(owner='Bipin', account_number=123, balance=200)
Bipin
"""