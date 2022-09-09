# 1. Count Letters:

from itertools import count


letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

def unique_english_letters(word):       # Defines a function called unique_english_letters with 1 parameter (word).
    uniques = 0                         # Creating a blank variable with nothing in it. An empty container.
    for letter in letters:              # Says for as many letters that are in the string "letters" (52 times)
        if letter in word:              # Checking each letter in the function parameter (word)
            uniques += 1                # If a unique letter is found this counter adds 1 to uniques
    return uniques                      # Returns the total number of unique letters in the word.

print(unique_english_letters("Mississippi"))

print(unique_english_letters("Georgia"))



# 2. Count X:

def count_char_x(word, x):              # Defines a function called count_char_x with 2 parameters (word, x).
    char = 0                            # Creating a blank variable with nothing in it. An empty container.
    for letter in word:                 # Says to itirate through every letter in (word)
        if letter == x:                 # Each time (x) is present in (word)...
            char += 1                   # Add 1 to the variable char
    return char                         # Returns the amount of times (x) appears in (word)

print(count_char_x("mississippi", "s"))

print(count_char_x("mississippi", "m"))

print(count_char_x("mississippi", "i"))



# 3. Count Multi X:

def count_multi_char_x(word, x):        # Defines a function called count_multi_char_x with 2 parameters (word, x).
    splits = word.split(x)              # Splits the string (word) at each (x). m | iss | iss | ippi
    return (len(splits) - 1)            # Returns the number of items in the variable minus 1

print(count_multi_char_x("mississippi", "iss"))

print(count_multi_char_x("Hello, World!", "l"))



# 4. Substring Between:

def substring_between_letters(word, start, end):        # Defines a function called substring_between_letters with 3 parameters (word, start, end).
    start_point = word.find(start)                      # Finds the start point in (word)
    end_point = word.find(end)                          # Finds the end point in (word)
    if start_point > -1 and end_point > -1:             # Says that if both (start and end) are found then ... 
        return (word[start_point + 1: end_point])       # Prints the string between (start and end) in (word)
    return word                                         # If both start and end are not found then just the original (word) will be returned.

print(substring_between_letters("apple", "p", "e"))

print(substring_between_letters("apple", "p", "c"))



# 5. X Length:

def x_length_words(sentence, x):                # Defines a function called x_length_words with 2 parameters (sentence, x)
    words = sentence.split(" ")                 # Splits the sentence at every space (" ")
    for word in words:                          # Check each word after the split
        if len(word) < x:                       # If the length of a word is less than (x)...
            return False                            # Return False
    return True                                 # If all the words are greater than (x) return True.

print(x_length_words("i like apples", 2))       # Should print False

print(x_length_words("he likes apples", 2))     # Should print True