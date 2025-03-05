from seasons import get_minutes, transcript
import pytest

def test_get_minutes():
    from datetime import date
    born = date(1998, 1, 14)
    today = date.today()
    expected_minutes = (today - born).total_seconds() / 60
    assert get_minutes("1998-01-14") == int(expected_minutes)

    
def test_transcript():
    assert transcript(14271840) == "fourteen million, two hundred seventy-one thousand, eight hundred forty"

    


