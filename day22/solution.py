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


def play_until_win(deck1, deck2):
    while deck1 and deck2:
        play(deck1, deck2)


def winscore(deck):
    score = 0
    for i, val in enumerate(deck):
        score += val * (len(deck) - i)
    return score


if __name__ == '__main__':
    with open('input.txt') as f:
        lines = f.readlines()

    player1, player2 = load_decks(lines)
    play_until_win(player1, player2)
    if player1:
        print(winscore(player1))
    else:
        print(winscore(player2))
