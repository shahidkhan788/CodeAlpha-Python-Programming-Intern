import random

word_list = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
         'goose hawk lion lizard llama mole monkey moose mouse mule newt '
         'otter owl panda parrot pigeon python rabbit ram rat raven '
         'rhino salmon seal shark sheep skunk sloth snake spider '
         'stork swan tiger toad trout turkey turtle weasel whale wolf '
         'wombat zebra ').split()

chosen_word = random.choice(word_list).lower()
pattern = list('_' * len(chosen_word))
print(pattern)
print()

stages = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
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
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

lives = 0
for i in range(len(chosen_word)+5):
    guess = input('Guess a letter : ').lower()[0]
    for j in range(len(chosen_word)):
        if guess == chosen_word[j]:
            if '_' != pattern[j]:
                continue
            pattern[j] = guess
            if '_' not in pattern:
                print('---------------------------------------')
                print(pattern)
                print('---------------------------------------')
                print('You won!')
                exit()
            print(pattern)
            print()
            break
            
    else:
        lives += 1
        print()
        if lives == 6:
            print(stages[lives])
            print('You lose!')
            exit()
        print(stages[lives])
        print('wrong letter!')

