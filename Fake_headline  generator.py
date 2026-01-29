import random
import wordlist



while True:
    with open("wordlist.txt", "r") as file:
        words = [line.strip() for line in file.readlines()]
    
    with open("vocab.txt", "r") as file:
        vocab_words = [line.strip() for line in file.readlines()]

    with open("places and things.txt", "r") as file:
        places_and_things = [line.strip() for line in file.readlines()]


        headline =f"BREAKING NEWS: {random.choice(words).upper()} {random.choice(vocab_words).upper()} {random.choice(places_and_things).upper()}"
        print("\n" +headline)

        user_input = input("\n Want more to generate headlines?(y/n): ").strip().lower()
        if user_input =="n":
            print("\n Thanks for using the Fake Headline Generator. Have a Good day!")

            break
