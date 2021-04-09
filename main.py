from random import random as rand
import os

wordlists0 = os.path.join(os.path.dirname(__file__), "wordlists")

n = 20

def main():
    wordlist = []

    for dir, subdirs, files in os.walk(wordlists0):
        for file0 in files:
            absfile0 = os.path.join(dir, file0)
            wordlist_file = open(absfile0, "r")
            wordlist += wordlist_file.read().split("\n")
            wordlist_file.close()

    wordlist_len = len(wordlist)

    def rand_word():
        return wordlist[rand_int(wordlist_len)]

    print("Length of wordlist: " + str(wordlist_len))

    print("\n\n" + "-" * 10 + "Printing " + str(n) + " random words" + "-" * 10 + "\n")
    for i in range(n):
        print(rand_word())
    print("\n" + "-" * len("-" * 10 + "Printing " + str(n) + " random words" + "-" * 1))


def rand_int(max):
    return int(rand() * max)

if __name__ == '__main__':
    main()
