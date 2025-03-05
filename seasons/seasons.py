from datetime import date, timedelta
import sys
import re
import operator
import inflect
p = inflect.engine()


def main():
    ...
    minutes = get_minutes(input("Date of Birth: "))
    if not minutes:
        sys.exit("Invalid date")
    return print(transcript(minutes) + " minutes")


def get_minutes(s):
    ...
    if match := re.search(r"^(\d{4})\-(\d{2})\-(\d{2})$", s):
        Date = date(int(match.group(1)), int(match.group(2)), int(match.group(3)))
        today = date.today()
        duration = operator.__sub__(today, Date)
        minutes = timedelta.total_seconds(duration)/60

        return minutes
    return False 


def transcript(s):
    ...
    # delete " and " in transcription
    text = p.number_to_words(s)
    if curated := re.sub(r"\b and\b", '', text):
        return curated
    return text


if __name__ == "__main__":
    main()