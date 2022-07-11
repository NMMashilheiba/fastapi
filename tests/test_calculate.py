import pytest
from app.calculate import add, subtract, multiply, divide, BankAccount, Insufficient_Funds

@pytest.fixture
def zero_bank_account():
    return BankAccount()

@pytest.fixture
def bank_account():
    return BankAccount(100)

@pytest.mark.parametrize("num1, num2, expected", [
    (1, 2, 3),
    (5, 19, 24),
    (1, 1, 2)
])
def test_add(num1, num2, expected):
    assert add(num1, num2) == expected 

def test_subtract():
    assert subtract(5, 2) == 3 

def test_multiply():
    assert multiply(5 , 2) == 10

def test_divide():
    assert divide(5, 2) == 2.5 

# BankAccount class
def test_set_init_amount(bank_account):
    # bank_account = BankAccount(100)
    assert bank_account.balance == 100

def test_account_default_amount(zero_bank_account):
    # bank_account = BankAccount()
    assert zero_bank_account.balance == 0

def test_withdraw():
    bank_account = BankAccount(100)
    bank_account.withdraw(10)
    assert bank_account.balance == 90

def test_deposit():
    bank_account = BankAccount(100)
    bank_account.deposit(110)
    assert bank_account.balance == 210

def test_collect_interest():
    bank_account = BankAccount(100)
    bank_account.collect_interest()
    assert round(bank_account.balance, 3) == 110
    # print(round(bank_account.balance, 6))

@pytest.mark.parametrize("deposited, withdrew, cur_balance", [
    (500, 100, 400),
    (500, 111, 389),
    (1000, 200, 800)
])
def test_bank_transaction(zero_bank_account, deposited, withdrew, cur_balance):
    zero_bank_account.deposit(deposited)
    zero_bank_account.withdraw(withdrew)
    assert zero_bank_account.balance == cur_balance

def test_insufficient_fund(bank_account):
    with pytest.raises(Insufficient_Funds):
        bank_account.withdraw(200)



