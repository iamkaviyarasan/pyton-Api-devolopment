import os
import sys

# Get the current directory of the script
current_dir = os.path.dirname(__file__)

# Assuming 'fastapi' is located in the parent directory
fastapi_dir = os.path.abspath(os.path.join(current_dir, '..'))

# Append the fastapi directory to sys.path
sys.path.append(fastapi_dir)

from app.calculations import add, subtract, multiply, divide, BankAccount   

def test_add():
    print ("test add function")

    assert add(1, 2)  == 3

def test_subtract():
    print ("test subtract function")

    assert subtract(2, 1) == 1

def test_multiply():
    print ("test multiply function")

def test_divide():
    print ("test divide function")

