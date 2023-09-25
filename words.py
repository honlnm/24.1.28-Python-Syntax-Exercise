def print_upper_words(words, must_start_with):
    """Given a list of words, this function will print each word, in uppercase, on a seperate line.
    For example:
    print_upper_words([tomato, onion, pepper])
    Should print:
    TOMATO
    ONION
    PEPPER
    """

    for word in words:
        for letter in must_start_with:
            if word.startswith(letter):
                print(word.upper())
                break

print_upper_words(["tomato", "onion", "pepper"],"o")
