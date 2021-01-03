from collections import deque


def load_decks(lines):
    lines = [line.strip() for line in lines if line.strip()]
    deck1 = deque()
    deck2 = deque()
    current_deck = deck1
    for line in lines:
        if line.startswith('Player 1'):
            current_deck = deck1
        elif line.startswith('Player 2'):
            current_deck = deck2
        else:
            current_deck.append(int(line))
    return deck1, deck2


def play(deck1, deck2):
    card1 = deck1.popleft()
    card2 = deck2.popleft()
    if card1 > card2:
        deck1.append(card1)
        deck1.append(card2)
    else:
        deck2.append(card2)
        deck2.append(card1)


def crab_combat(deck1, deck2):
    while deck1 and deck2:
        play(deck1, deck2)


def serialize_configuration(deck1, deck2):
    return ','.join(str(card) for card in deck1) + ';' + ','.join(str(card) for card in deck2)


def recursive_crab_combat(deck1, deck2):
    # make a local copy so we can modify the deck without changing the original
    deck1 = deque(deck1)
    deck2 = deque(deck2)
    played_configurations = set()  # keep track of played configurations
    while deck1 and deck2:
        serialized = serialize_configuration(deck1, deck2)
        if serialized in played_configurations:
            return True, deck1, deck2
        played_configurations.add(serialized)
        card1 = deck1.popleft()
        card2 = deck2.popleft()
        if len(deck1) >= card1 and len(deck2) >= card2:
            if recursive_crab_combat(tuple(deck1)[:card1], tuple(deck2)[:card2])[0]:
                deck1.append(card1)
                deck1.append(card2)
            else:
                deck2.append(card2)
                deck2.append(card1)
        elif card1 > card2:
            deck1.append(card1)
            deck1.append(card2)
        else:
            deck2.append(card2)
            deck2.append(card1)

    if not deck2:
        return True, deck1, deck2
    if not deck1:
        return False, deck1, deck2


def winscore(deck):
    score = 0
    for i, val in enumerate(deck):
        score += val * (len(deck) - i)
    return score


if __name__ == '__main__':
    with open('input.txt') as f:
        lines = f.readlines()

    # part 1
    player1, player2 = load_decks(lines)
    crab_combat(player1, player2)
    if player1:
        print(winscore(player1))
    else:
        print(winscore(player2))

    # part 2
    player1, player2 = load_decks(lines)
    result, player1, player2 = recursive_crab_combat(player1, player2)
    if result:
        print(winscore(player1))
    else:
        print(winscore(player2))
