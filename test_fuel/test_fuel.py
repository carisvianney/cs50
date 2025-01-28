from fuel import convert, gauge
import pytest

def test_convert():
    assert convert("1/1") == 100
    assert convert("2/4") == 50
    assert convert("1/100") == 1

    with pytest.raises(ZeroDivisionError):
        convert("2/0")
    with pytest.raises(ValueError):
        convert("a/b")


def test_gauge():
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(67) == "67%"




