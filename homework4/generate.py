import random
def generate(words):
    x = random.random()
    y = x * len(words)
    z = int(y)
    secret_word = words[z]
    return secret_word

