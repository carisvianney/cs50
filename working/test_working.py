import pytest
import sys
from working import convert

def main():
    test_convert()
    test_convert_errors()
    test_value_errors()
    test_range()

def test_convert():
    assert convert("7 AM to 9 PM") == "07:00 to 21:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("10 AM to 8:50 PM") == "10:00 to 20:50"
    assert convert("10:30 PM to 8 AM") == "22:30 to 08:00"
#    assert convert("7 AM TO 9 PM")

def test_convert_errors():
    with pytest.raises(ValueError):
       convert("7 AM - 9 PM"),
    
def test_value_errors():
    with pytest.raises(ValueError):
        convert("7 AM a 9 PM"),

def test_range():
    with pytest.raises(ValueError):
       convert("5:60 AM to 7:60 PM"),

if __name__ == "__main__":
    main()