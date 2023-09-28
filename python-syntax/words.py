def print_upper_words(words, must_start_with):
    # this should print "HELLO", "HEY", "YO", and "YES"
    for char in words: #loop through list of words
        for prefix in must_start_with:  #must_start_with is a set so we loop through that too
            if char.startswith(prefix): 
                print(char.upper())


print_upper_words(['hello', 'hey', 'goodbye', 'yo', 'yes'], must_start_with={'h','y'})
