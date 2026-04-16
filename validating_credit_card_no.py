import re

def validate_credit_card(card):

    structure_pattern = r"^[456]\d{3}(-?\d{4}){3}$"
    
    if not re.match(structure_pattern, card):
        return "Invalid"
    clean_card = card.replace("-", "")

    if re.search(r"(\d)\1{3,}", clean_card):
        return "Invalid"
    
    return "Valid"

if __name__ == "__main__":
    n = int(input())
    for _ in range(n):
        card_number = input().strip()
        print(validate_credit_card(card_number))
