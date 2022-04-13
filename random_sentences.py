import random

def random_choice():
    # Open the file in read mode
    with open("MyFile.txt", "r") as file:
        allText = file.read()
        words = list(map(str, allText.split('\n')))

        # print random string
        return random.choice(words)