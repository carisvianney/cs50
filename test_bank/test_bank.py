from bank import value

def test_hello():
    assert value("hello") == 0

def test_hi():
    assert value("hi") == 20

def test_word():
    assert value("sayonara") == 100

def test_errors():
    if value("Hello") == 100:
        raise SystemExit(1)
    elif value("ola") == 0:
        raise SystemExit(1)
    
