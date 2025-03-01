from plates import is_valid


def test_plates():
    assert is_valid("AB1") == True
    assert is_valid("CHECO") == True

def test_errors():
    if is_valid("123") == True:
        raise SystemExit(1)
    elif is_valid("A") == True:
        raise SystemExit(1)
    elif is_valid("HOLABEBE") == True:
        raise SystemExit(1)
    elif is_valid("HI!") == True:
        raise SystemExit(1)
    elif is_valid("HOLA1B") == True:
        raise SystemExit(1)
    elif is_valid("FERXX0") == True:
        raise SystemExit(1)
