def value_of_card(card):
    if isinstance(card, str):
        cards = card.upper()
        if cards == "J" or cards == "K" or cards == "Q":
            return 10
        elif cards == "A":
            return 1
        return int(cards)

    elif isinstance(card, int):
        if 0 < card <= 11:
            return card

def higher_card(card_one, card_two):
    value_one = card_one
    value_two = card_two

    if card_one.upper() == "A":
        value_one = 1
    elif card_one.upper() in ("J", "Q", "K"):
        value_one = 10
    else:
        value_one = int(card_one)

    if card_two.upper() == "A":
        value_two = 1
    elif card_two.upper() in ("J", "Q", "K"):
        value_two = 10
    else:
        value_two = int(card_two)

    if value_one == value_two:
        return (card_one, card_two)
    elif value_one < value_two:
        return card_two
    else:
        return card_one
def value_of_ace(card_one,card_two):
    if isinstance(card_one, str) and card_one.upper() == "A":
        value_one = 11
    else:
        value_one = value_of_card(card_one)

    if isinstance(card_two, str) and card_two.upper() == "A":
        value_two = 11
    else:
        value_two = value_of_card(card_two)

    if value_one + value_two + 11 > 21:
        return 1
    else:
        return 11



    
def is_blackjack(card_one,card_two):
    if isinstance(card_one, int) and isinstance(card_two, int):
        if card_one+card_two==21:
            return True 
        elif card_one+card_two<21:
            return False
        elif card_one+card_two>21:
            return False
    elif card_one.upper()=="A" and card_two==10:
        return True 
    
    elif card_two.upper()=="A" and card_one==10:
        return True
    
    elif card_one.upper()=="A" and isinstance(card_two,str) and card_two.upper()!="A":
        return True
    elif card_one.upper()=="A" and isinstance(card_two,str) and card_two.upper()=="A":
        return False
    elif card_two.upper()=="A" and isinstance(card_one,str) and card_one.upper()!="A":
        return True
    elif card_two.upper()=="A" and isinstance(card_one,str) and card_one.upper()=="A":
        return False
    elif isinstance(card_one,str) and isinstance(card_two,str) and card_two.upper()!="A" and card_one.upper()!="A":
        return False
def can_split_pairs(card_one,card_two):
    return value_of_card(card_one) == value_of_card(card_two)
    
    
def can_double_down(card_one,card_two):
    total=value_of_card(card_one)+value_of_card(card_two)
    return 9<=total <=11
    
