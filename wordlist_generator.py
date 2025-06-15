from itertools import permutations, product

def leetspeak(word):
    leet_map = {'a': ['4', '@'], 'e': ['3'], 'i': ['1', '!'], 'o': ['0'], 's': ['$', '5'], 't': ['7']}
    combos = [leet_map.get(c.lower(), [c]) for c in word]
    for option in product(*combos):
        yield ''.join(option)

def generate_wordlist(inputs, years=[2023, 2024]):
    wordlist = set()

    for word in inputs:
        word = word.strip()
        wordlist.add(word)
        for variation in leetspeak(word):
            wordlist.add(variation)
            for year in years:
                wordlist.add(f"{variation}{year}")
                wordlist.add(f"{year}{variation}")

    return wordlist

user_input = input("Enter keywords (name, pet, etc) separated by commas: ").split(',')
wordlist = generate_wordlist(user_input)

with open("custom_wordlist.txt", "w") as f:
    for word in wordlist:
        f.write(word + '\n')

print(f"Generated wordlist with {len(wordlist)} entries.")
