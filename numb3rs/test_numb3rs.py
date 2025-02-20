import pytest
import sys
from numb3rs import validate, main


def test_validate():
    assert validate("cat") == False
    assert validate("255.255.255.255") == True
    assert validate("0.0.0.0") == True
    assert validate("1.1.1.1000") == False

def test_validate_errors():
    if validate("3.333.333.333") == True:
        raise SystemExit(1)

if __name__ == "__main__":
    main()