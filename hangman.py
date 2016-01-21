import random
words = (["telephone", "wealthy", "shocking", "table", "slap", "donkey", "tame",
          "insurance", "worm", "deserve", "engine", "waves", "strong", "lumpy", "walk",
          "squirrel", "round", "trick", "crawl", "possessive", "certain", "nebulous",
          "squeeze", "toothbrush", "sponge"])
playing = True
tries = 6
right_guesses = []
player_guesses = []
first_turn = True
def word_sele():    #selects random word from list
    c_word = []
    key = {}
    rand_num = random.randrange(0,len(words))
    for i in words[rand_num]:
        c_word.append(i)
    for j in range(0,len(c_word)):
        key[j] = c_word[j]
    return key
def guess_manager(word):    #returns a list of places where the player had a correct guess
    global right_guesses
    lists = []
    guess = raw_input("Guess a letter!   ")
    if len(lists) == 0:
        for j in word:
            lists.append(False)
        if len(right_guesses) == 0:
            for x in word:
                right_guesses.append(False)
    for i in range(0,len(word)):
        if guess == word[i]:
            lists[i] = True
        else:
            lists[i] = False
    return lists
def guess_comp(word, guess_list):   #checks which positions had a correct guess and displays a letter or "_" accordingly
    global right_guesses
    complete_word = []
    for i in range(0,len(guess_list)):
        if guess_list[i] == False and right_guesses[i]:
            right_guesses[i] = True
        elif guess_list[i] and right_guesses[i]:
            right_guesses[i] = True
        elif guess_list[i] and right_guesses[i] == False:
            right_guesses[i] = True
        elif guess_list[i] == False and right_guesses[i] == False:
            right_guesses[i] = False
    for j in range(0,len(guess_list)):
        if right_guesses[j]:
            complete_word.append(word[j])
        else:
            complete_word.append("_")
    print "".join(complete_word)
def tries_manager(guess):  #keeps count of how many tries the player has before they get a game over
    global tries
    correct = None
    num_wrong = 0
    num_right = 0
    if tries == 0:
        correct = True
        return correct
    for i in range(0,len(guess)):
        if guess[i] == False:
            num_wrong += 1
        if right_guesses[i]:
            num_right += 1
        if len(guess) == num_wrong:
            tries -= 1
        if len(right_guesses) == num_right+1:
            correct = False
            return correct
    print "Lives:      " + str(tries)
    return correct
def add_word(new_word):
    words.append(new_word)
add_word("picture")
add_word("superficial")
add_word("magical")
add_word("school")
add_word("dangerous")
add_word("challenge")
add_word("orange")
add_word("daughter")
add_word("cakes")
add_word("chicken")
boss = word_sele()
while playing:
    if first_turn:
        print "Welcome to Hangman! This is a classic game of Hangman, a word has been selected from a random list! See if you can guess what it is! Here is a hint it has %d letters!" % (len(boss.values()))
        first_turn = False
    else:
        r_guess_list = guess_manager(boss.values())
        lives = tries_manager(r_guess_list)
        guess_comp(boss.values(), r_guess_list)
        if lives:
            print "RIP You got hanged :'("
            playing = False
        elif lives == False:
            print "Congratulation you won!"
            playing = False