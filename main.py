# Project 2
# Completed on the 23rd July 2022 at 11:02am.

board = {
    0: """  
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========""",
    1: """
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========""",
    2: """
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========""",
    3: """
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""",
    4: """
  +---+
  |   |
  O   |
  |   |
      |
      |
=========""",
    5: """
  +---+
  |   |
  O   |
      |
      |
      |
=========""",
    6: """
  +---+
  |   |
      |
      |
      |
      |
=========""",
    7: """
  +---+
      |
      |
      |
      |
      |
========="""
}


def player_to_string(p):
    if p == 1:
        return "One"
    else:
        return "Two"


def get_alternate_player(p):
    if p == 1:
        return 2
    else:
        return 1


def check_word(aword, attempt):
    return aword == attempt


def check_letter(aword, letter):
    for l in aword:
        if l.lower() == letter.lower():
            return True


def turn(player, word=None, chances=7, guessed=None, joined="") -> None:
    if guessed is None:
        guessed = []
    if word is None:
        word = input("Player" + " " + player_to_string(player) + " please enter a word:")
        joined = "_"*len(word)

    if word is None or len(word) <= 1 or not word.isalpha():
        print("The word must have a length greater than 1 and must be purely alphabetical.")
        turn(player)
        return

    guess = input("Player " + player_to_string(get_alternate_player(player)) + "enter a letter or word you wish to "
                                                                               "guess:")

    if len(str(guess)) > 1:
        if check_word(word, str(guess)):
            print(board[chances])
            print(joined)
            print("Player " + player_to_string(get_alternate_player(player)) + " has guessed the word correctly.")
            turn(get_alternate_player(player))
            return
        else:
            chances -= 1
            print(board[chances])
            print(joined)
            turn(player, word, chances, guessed, joined)
    elif len(str(guess)) == 1:
        if guess in guessed:
            print("You have already guessed that letter.")
            turn(player, word, chances, guessed, joined)
            return
        else:
            if check_letter(word, guess):
                key = 0
                for letter in word:
                    if letter.lower() == guess.lower():
                        joined = joined[:key] + guess + joined[key + 1:]
                    key += 1

                if check_word(word, joined):
                    print(board[chances])
                    print(joined)
                    print("Player " + player_to_string(get_alternate_player(player)) + "has guessed the word "
                                                                                       "correctly.")
                    turn(get_alternate_player(player))
                else:
                    guessed.append(guess)
                    print(board[chances])
                    print(joined)
                    turn(player, word, chances, guessed, joined)
            else:
                chances -= 1
                if chances == 0:
                    print(board[chances])
                    print(joined)
                    print("Player " + player_to_string(
                        get_alternate_player(player)) + " has ran out of chances, " + " player " + player_to_string(
                        player) + " wins!")
                    turn(get_alternate_player(player))
                    return
                else:
                    guessed.append(guess)
                    print(board[chances])
                    print(joined)
                    turn(player, word, chances, guessed, joined)
    else:
        print("The letter/word must have a length greater than 0!")
        turn(player)


turn(1)
