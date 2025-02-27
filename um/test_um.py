import pytest
from um import count

def main():
    test_um()

def test_um():
    assert count("hello, um, world") == 1
    assert count("helloum") == 0
    assert count("humano") == 0
    assert count("UM") == 1
    assert count("Um, hi") == 1


if __name__ == "__main__":
    main()