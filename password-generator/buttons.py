from string import ascii_lowercase, ascii_uppercase, digits, punctuation
from enum import Enum


class Characters(Enum):
    btn_upper = ascii_uppercase
    btn_lower = ascii_lowercase
    btn_digit = digits
    btn_special = punctuation


CHARACTER_NUMBER = {
    'btn_lower': len(Characters.btn_lower.value),
    'btn_upper': len(Characters.btn_upper.value),
    'btn_digit': len(Characters.btn_digit.value),
    'btn_special': len(Characters.btn_special.value)
}

GENERATE_PASSWORD = (
    'btn_refresh', 'btn_lower', 'btn_upper', 'btn_digit', 'btn_special'
)