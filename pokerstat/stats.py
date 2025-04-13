def get_stats(cards, deck):
    """
    Get the statistics of a hand of cards.
    args:
        cards: a list of wnated cards
        deck: a deck of cards
    returns:
        a dictionary of statistics
    """
    value = None
    for card in cards:
        if value == None:
            value = card.value
        elif card.value != value:
            assert False
    return 1
            
