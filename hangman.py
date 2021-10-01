import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''

                   
def cls():
  print("\n" * 50)


print(logo + "\n")

word_list = ["kurczak", "walizka", "plakat", "poduszka", "plecak"]
chosen_word = random.choice(word_list) 
display = []
life_count = 6
end_of_game = False
for _ in chosen_word:
  display += "_"


while not end_of_game:
  guess = input("Guess the letter: ").lower()

  if guess in display:
    print(f"You have already guessed {guess}")

  for position in range(len(chosen_word)):
    letter = chosen_word[position]
    if guess == letter:
      display[position] = letter

  cls()

  if guess not in chosen_word:
    life_count -= 1
    print(f"You guessed {guess}. That's not the letter ")
    if life_count == 0:
      end_of_game = True
      print("You lose!")

  print(stages[life_count])
  print(f"{' '.join(display)}")


  if guess == chosen_word:
    end_of_game = True
    print(f"You win! The word was {chosen_word}")

  if "_" not in display:
    end_of_game = True    
    print("You win!")
