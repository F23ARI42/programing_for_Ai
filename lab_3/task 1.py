import  random
word=["programing","develop","deep","machine","learning"]
def choose_word():
    return random.choice(word)
def display(word,guess_word):
    return "".join([letter if letter in guess_word else "_" for letter in word])
def hugman():
    word = choose_word()
    guess_word = set()
    lives=10
    print("Welcome to hugman game!")
    while lives > 0:
        print(display(word,guess_word))
        guess=input("Guess a letter:").lower()
        if len(guess) != 1:
            print("Please enter a single letter.")
            continue
        guess_word.add(guess)
        if guess in word:
            print("correct!")
            if all(letter  in guess_word for letter in word):
                print("Congratulations You guessed the word!")
                break
        else:
            lives -= 1
            print(f"wrong guess!{lives}")
    if lives == 0:
        print("game over!")
hugman()