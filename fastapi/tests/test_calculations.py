import os
import sys

# Get the current directory of the script
current_dir = os.path.dirname(__file__)

# Assuming 'fastapi' is located in the parent directory
fastapi_dir = os.path.abspath(os.path.join(current_dir, '..'))

# Append the fastapi directory to sys.path
sys.path.append(fastapi_dir)

from app.calculations import BankAccount, InsufficientFunds, add, subtract, multiply, divide  
import pytest


@pytest.fixture
def zero_bank_account():
    print("creating empty bank account")
    return BankAccount()
 
@pytest.fixture
def bank_account():
   
    return BankAccount(1000)

@pytest.mark.parametrize("num1,num2,expected",[(3,2,5),(7,1,8),(12,4,16)   ] )

def test_add(num1,num2,expected):
    

    assert add(num1,num2)  == expected

def test_subtract():


    assert subtract(9, 4) == 5

def test_multiply():
    assert multiply(4, 3) == 12


def test_divide():
    assert divide(20, 5) == 4

def test_bank_set_initial_amount(bank_account):
     print("testing setting initial amount")
     assert bank_account.balance == 1000


def test_bank_default_amount(zero_bank_account):
    print("testing default amount of 0")
    assert zero_bank_account.balance == 0


def test_withdraw(bank_account):
    
    bank_account.withdraw(500)
    assert bank_account.balance == 500

def test_deposit(bank_account):
    
    bank_account.deposit(500)
    assert bank_account.balance == 1500

def test_collect_interest(bank_account):
    bank_account.collect_interest()
    assert bank_account.balance == 1100


@pytest.mark.parametrize("deposited,withdraw,expected",[(1500,500,1000),(50,10,40),(1200,200,1000)   ] )

def test_bank_transaction(zero_bank_account,deposited,withdraw,expected):
    zero_bank_account.deposit(deposited)
    zero_bank_account.withdraw(withdraw)
    assert zero_bank_account.balance == expected

def test_insufficient_funds(bank_account):
    with pytest.raises(InsufficientFunds):
        bank_account.withdraw(1500)
