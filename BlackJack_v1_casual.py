import random


def game_start():
    from logo import logo
    cheat = bool(input("Type '1' to enable cheats: "))
    print(logo)
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    player_cards = []
    computer_cards = []
    knowledge_of_cards_computer = cards
    for user in range(0, 2):
        index_of_dawn_card = random.randint(0, len(cards) - 1)
        player_cards.append(cards[index_of_dawn_card])
        index_of_dawn_card = random.randint(0, len(cards) - 1)
        computer_cards.append(cards[index_of_dawn_card])
        knowledge_of_cards_computer.pop(index_of_dawn_card)
    print(f"Your cards: {player_cards}")
    if cheat:
        print(f"Computer cards: {computer_cards}\n")
    else:
        pass
    sum_of_computers_cards = sum(computer_cards)
    draw_computer_cards(sum_of_computers_cards, computer_cards, cards)
    draw_players_cards(player_cards, cards)
    sum_of_player_cards = sum(player_cards)
    result = who_won(sum_of_computers_cards, sum_of_player_cards)
    return result


def who_won(sum_of_computers_cards, sum_of_player_cards):
    if sum_of_player_cards == sum_of_computers_cards:
        return f"It's draw!\nYou have: {sum_of_player_cards}\nand computer have: {sum_of_computers_cards}"
    elif 21 >= sum_of_player_cards and 21 >= sum_of_computers_cards:
        if sum_of_player_cards > sum_of_computers_cards:
            return f"You win!\nYou have: {sum_of_player_cards}\nand computer have: {sum_of_computers_cards}"
        else:
            return f"You lost!\nYou have: {sum_of_player_cards}\nand computer have: {sum_of_computers_cards}"
    elif 21 < sum_of_player_cards and sum_of_computers_cards > 21:
        if sum_of_player_cards > sum_of_computers_cards:
            return f"You win!\nYou have: {sum_of_player_cards}\nand computer have: {sum_of_computers_cards}"
        else:
            return f"You lost!\nYou have: {sum_of_player_cards}\nand computer have: {sum_of_computers_cards}"
    elif 21 >= sum_of_player_cards and 21 < sum_of_computers_cards:
        return f"You win!\nYou have: {sum_of_player_cards}\nand computer have: {sum_of_computers_cards}"
    elif 21 < sum_of_player_cards and 21 >= sum_of_computers_cards:
        return f"You lost!\nYou have: {sum_of_player_cards}\nand computer have: {sum_of_computers_cards}"


def draw_computer_cards(sum_of_computers_cards, computer_cards, cards):
    if 11 in computer_cards:
        if sum_of_computers_cards > 21:
            j = computer_cards.indexOf(11)
            computer_cards[j] = 1
        else:
            pass
    else:
        pass
    is_best_hand = True
    while not is_best_hand:
        is_best_hand = False
    if sum_of_computers_cards <= 19:
        gamble = random.randint(0, 1)
        if gamble == 0:
            index_of_dawn_card = random.randint(0, len(cards) - 1)
            computer_cards.append(cards[index_of_dawn_card])
            print(f"{computer_cards}")
        else:
            pass
    elif 9 >= sum_of_computers_cards <= 17:
        index_of_dawn_card = random.randint(0, len(cards) - 1)
        computer_cards.append(cards[index_of_dawn_card])
    else:
        pass


def draw_players_cards(player_cards, cards):
    if 11 in player_cards:
        if input("Type 'y' to 11 to 1?: ") == 'y':
            j = player_cards.index(11)
            player_cards[j] = 1
    else:
        pass
    if input("\nType 'y' to get another card,\nType 'n' to pass: ") == 'n':
        return player_cards, cards
    else:
        index_of_dawn_card = random.randint(0, len(cards) - 1)
        player_cards.append(cards[index_of_dawn_card])
        print(f"Your cards: {player_cards}")
        draw_players_cards(player_cards, cards)


print(game_start())
