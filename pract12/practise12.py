import requests

book = requests.get("https://www.gutenberg.org/cache/epub/76266/pg76266.txt")


ttt = book.text


with open('file.txt', 'w') as f:
    f.write(ttt)