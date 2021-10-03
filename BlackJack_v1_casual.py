import random


def game_start():
    from logo import logo
    cheat = bool(input("Type '1' to enable cheats: "))
    print(logo)
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    player_cards = []
    computer_cards = []
    for user in range(0, 2):
        index_of_dawn_card = random.randint(0, len(cards) - 1)
        player_cards.append(cards[index_of_dawn_card])
        index_of_dawn_card = random.randint(0, len(cards) - 1)
        computer_cards.append(cards[index_of_dawn_card])
    print(f"Your cards: {player_cards}")
    if cheat:
        print(f"Computer cards: {computer_cards}\n")
    else:
        pass
    draw_players_cards(player_cards, cards)
    sum_of_computers_cards = sum(computer_cards)
    draw_computer_cards(sum_of_computers_cards, computer_cards, cards)
    sum_of_player_cards = sum(player_cards)
    who_won(sum_of_computers_cards, sum_of_player_cards)


def who_won(sum_of_computers_cards, sum_of_player_cards):
    if sum_of_player_cards == sum_of_computers_cards:
        print(f"It's draw!\nYou have: {sum_of_player_cards}\nand computer have: {sum_of_computers_cards}")
    if sum_of_player_cards > 21 and sum_of_computers_cards > 21:
        if sum_of_computers_cards > sum_of_player_cards:
            print(f"You win!\nYou have: {sum_of_player_cards}\nand computer have: {sum_of_computers_cards}")
        else:
            print(f"You lost!\nYou have: {sum_of_player_cards}\nand computer have: {sum_of_computers_cards}")
    if 21 >= sum_of_computers_cards > sum_of_player_cards <= 21:
        print(f"You lost!\nYou have: {sum_of_player_cards}\nand computer have: {sum_of_computers_cards}")
    elif sum_of_computers_cards < sum_of_player_cards <= 21:
        print(f"You win!\nYou have: {sum_of_player_cards}\nand computer have: {sum_of_computers_cards}")


def draw_computer_cards(sum_of_computers_cards, computer_cards, cards):
    if 11 in computer_cards:
        if sum_of_computers_cards > 21:
            j = computer_cards.indexOf(11)
            computer_cards[j] = 1
        else:
            pass
    else:
        pass
    if sum_of_computers_cards <= 19:
        gamble = random.randint(0, 1)
        if gamble == 0:
            index_of_dawn_card = random.randint(0, len(cards) - 1)
            computer_cards.append(cards[index_of_dawn_card])
        else:
            pass
    elif 9 >= sum_of_computers_cards <= 17:
        index_of_dawn_card = random.randint(0, len(cards) - 1)
        computer_cards.append(cards[index_of_dawn_card])
    else:
        pass


def draw_players_cards(player_cards, cards):
    if input("\nType 'y' to get another card,\nType 'n' to pass: ") == 'n':
        return player_cards, cards
    else:
        index_of_dawn_card = random.randint(0, len(cards) - 1)
        player_cards.append(cards[index_of_dawn_card])
        print(f"Your cards: {player_cards}")
        draw_players_cards(player_cards, cards)
    if 11 in player_cards:
        if input("Type 'y' to 11 to 1?: ") == 'y':
            j = player_cards.indexOf(11)
            player_cards[j] = 1
    else:
        pass


game_start()
