All from www.codecademy.com

Python Code Challenges: Strings

    1. Count Letters:
        - Define the function to accept one parameter — the word whose letters we are counting
        - Create a counter to keep track of unique letters
        - Loop through every letter in our alphabet string. If the current letter was found in our word, increase our count
        - Return the count after looping through all letters.

    2. Count X:
        - Define the function to accept two parameters. word for the input string and x for the single character
        - Create a counter to keep track of the occurrences
        - Loop through every letter in the string. If the current letter is equal to the input letter, increase our counter
        - Return the counter after looping through the entire string.

    3. Count Multi X:
        - Define the function to accept two parameters. word for the input string and x for the second string we are searching for
        - Split the string into substrings based on the second input parameter
        - Count the number of instances the substring appeared in the first input string based on the split string
        - Return the result.

    4. Substring Between:
        - Define the function to accept three parameters, one string and two characters
        - find the starting index of our substring using the second input parameter
        - find the ending index of our substring using the third input parameter
        - If neither of the indices are -1, return the portion of the first input parameter string between the starting and ending indices (not including the starting and ending index)
        - If either of the indices are -1, that means the start or end of the substring didn’t exist in our string. Return the original string in this case.

    5. x Length:
        - Define the function to accept two parameters, one string, and one number
        - Split up the sentence into an array of words
        - Loop through the words. If the length of any of the words is less than the provided number return False
        - If we made it through the loop without returning False then return True.