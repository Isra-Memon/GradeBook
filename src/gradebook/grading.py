import re


def letter_grade(score):
    if score < 0 or score > 100:
        raise ValueError(f"Invalid score: {score}. Must be between 0 and 100.")
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


def validate_name(name):
    if not name:
        raise ValueError("Name cannot be empty")
    if len(name) > 50:
        raise ValueError(f"Name too long ({len(name)} chars), max 50 allowed")
    if not re.fullmatch(r"[A-Za-z\s\-]+", name):
        raise ValueError("Name must contain only letters, spaces, and hyphens")
    return True
