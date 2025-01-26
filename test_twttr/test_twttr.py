import pytest
from twttr import shorten

def test_shorten():
    try:
        assert shorten("Hola") == "Hl"
        assert shorten("hola") == "hl"
        assert shorten("LMFAO") == "LMF"
        assert shorten("123e") == "123"
    except AssertionError:
        print(f"Something went wrong")

def test_errors():
    if shorten("Hola") == "Hola":
        raise SystemExit(1)
    elif shorten("HOLA") == "HOLA":
        raise SystemExit(1)
    elif shorten("1") == "":
        raise SystemExit(1)
    elif shorten(".") == "":
        raise SystemExit(1)
    elif shorten("b") == "B":
        raise SystemExit(1)

test_shorten()