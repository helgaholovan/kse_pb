import random, addictional_result, list_of_answers, generate
def repeat():

    words = ['apple',    'bread','candy',    'dream','eagle','flame','grape','house','input','joker']
    secret_word = generate.generate(words)

    tries = 6
    wl = len(secret_word)
    w = secret_word

    print("Welcome to Wordle!")
    print("Guess the",wl,"-letter word. You have", tries, "tries.")

    while True:
        try:
            guess = input("Спроба " + str(7 - tries) + "/6 – Введіть слово: ").lower()
        except EOFError:
            print("неіснуюче слово")
            continue
        
        if len(guess)!=wl:
            print("Wrong length. Expected", wl  )
            continue

        if guess==w:
            print("You win!!!")
            answer = input("One more time?").lower()
            if answer == "yes":
                return
            else:
                break

        result = list_of_answers.check(guess, w)

        display = addictional_result.add_res(guess, wl, result)

        junk = ''.join([c for c in display if c])
        print("Result:", ' '.join(display))
        tries = tries - 1
    else:
        final = secret_word
        print("You lose! The word was:", final)
        if answer == "yes":
                return