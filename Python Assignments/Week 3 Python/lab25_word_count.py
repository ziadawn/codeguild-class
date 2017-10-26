'''
Lab: Count Words

Let's write a python module to analyze a given text file containing a book for its vocabulary frequency
and display the most frequent words to the user in the terminal.

NOT DOING THIS PART CAUSE WE HAVEN'T LEARNED IT YET:
Print the most frequent top 10 out with their counts.
'''

# this is a good lab to do as a function woo


punctuation = '\‘’",!.,:;-?()&_“”\n'    # punctuation to remove from book
word_count = {}  # blank dictionary, outside my loop

with open('prideandprejudice.txt', 'r') as file:
    # contents = file.read()
    # print(contents)
    for line in file:                       # going through line by line
        line = line.lower()                 # make it lowercase
        for char in punctuation:            # remove punctuaiton, as defined above
            line = line.replace(char, '')
        line = line.split(' ')              # breaking the lines apart so I can look at each word by itself
        # print(line)
        for word in line: # count the words!
            if word != '':
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1        # if the word isn't there, add it and set its count to 1


print(word_count)

print('''
*** space for second book ***
''')

word_count = {}  # blank dictionary, outside my loop

with open('beowulf.txt', 'r') as file:
    # contents = file.read()
    # print(contents)
    for line in file:                       # going through line by line
        line = line.lower()                 # make it lowercase
        for char in punctuation:            # remove punctuaiton, as defined above
            line = line.replace(char, '')
        line = line.split(' ')              # breaking the lines apart so I can look at each word by itself
        # print(line)
        for word in line: # count the words!
            if word != '':
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1        # if the word isn't there, add it and set its count to 1


print(word_count)