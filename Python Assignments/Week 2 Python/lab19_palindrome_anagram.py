'''
Lab 19: Palindrome and Anagram

Let's write a palindrome and anagram checker.

Palindrome
Write a function check_palindrome which takes a string, and returns True if the string's a palindrome, or False if it's not.

Anagram
Write another function check_anagram that takes two strings as parameters and returns True if they're anagrams of eachother, False if they're not.

'''

def check_palindrome(palindrome):               # if you're going to have a variable, you need to have a variable in the function to receive it
    palindrome = palindrome.replace(' ', '')    # replace spaces with strings so it still returns true if your palindrome is more than one word
    return palindrome[::-1] == palindrome       # this is a true/false statement by def, so don't need to write an if/else statement


test_palindrome = input('What possible palindrome would you like to check? ')

print(check_palindrome(test_palindrome))        # this is where I'm using a variable, so need one in the function above


test_anagram_1 = input('What anagram? ')
test_anagram_2 = input('word 2. ')


def format_anagram(anagram):    # write two functions, one to sort each word, the second to compare the two sorted words
    anagram = anagram.lower()
    anagram = anagram.replace(' ', '')
    anagram = list(anagram)     # convert to list to sort
    anagram.sort()              # sorting the list, it returns nothing
    return anagram

def check_anagram(word1, word2):
    word1 = format_anagram(word1)
    word2 = format_anagram(word2)
    return word1 == word2

print(check_anagram(test_anagram_1, test_anagram_2))
