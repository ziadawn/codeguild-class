'''
Lab: Compute Automated Readability Index

Compute the ARI for a given body of text loaded in from a file.
The automated readability index (ARI) is a formula for computing the U.S. grade level for a given block of text.
The general formula to compute the ARI is as follows:

4.17(char/word) + 0.5(words/sentences) - 21.43

The score is computed by multiplying the number of characters divided by the number of words by 4.17,
adding the number of words divided by the number of sentences multiplied by 0.5, and subtracting 21.43.
If the result is a decimal, always round up.
Once you’ve computed the ARI score, you can use the following dictionary to look up the age range and grade level:

Scores greater than 14 should be presented as having the same age and grade level as scores of 14.
'''

from math import ceil       # built in funtion which let's me round up later

ari_scale = {
     1: {'ages':   '5-6', 'grade_level': 'Kindergarten'},
     2: {'ages':   '6-7', 'grade_level':    '1st Grade'},
     3: {'ages':   '7-8', 'grade_level':    '2nd Grade'},
     4: {'ages':   '8-9', 'grade_level':    '3rd Grade'},
     5: {'ages':  '9-10', 'grade_level':    '4th Grade'},
     6: {'ages': '10-11', 'grade_level':    '5th Grade'},
     7: {'ages': '11-12', 'grade_level':    '6th Grade'},
     8: {'ages': '12-13', 'grade_level':    '7th Grade'},
     9: {'ages': '13-14', 'grade_level':    '8th Grade'},
    10: {'ages': '14-15', 'grade_level':    '9th Grade'},
    11: {'ages': '15-16', 'grade_level':   '10th Grade'},
    12: {'ages': '16-17', 'grade_level':   '11th Grade'},
    13: {'ages': '17-18', 'grade_level':   '12th Grade'},
    14: {'ages': '18-22', 'grade_level':      'College'}
}

filename = input('Enter the name of the file you\'d like to look at: ')

# text = '''
# Everyone got its legs kicked or its feet trodden on in the scramble to get out of the carriage that very minute, but no
# one seemed to mind. Mother, curiously enough, was in no hurry to get out; and even when she had come down slowly and by
# the step, and with no jump at all, she seemed to wish to see the boxes carried in, and even to pay the driver, instead
# of joining in that first glorious rush round the garden and orchard and the thorny, thistly, briery, brambly wilderness
# beyond the broken gate and the dry fountain at the side of the house. But the children were wiser, for once. It was not
# really a pretty house at all; it was quite ordinary, and mother thought it was rather inconvenient, and was quite
# annoyed at there being no shelves, to speak of, and hardly a cupboard in the place. Father used to say that the
# iron-work on the roof and coping was like an architect's nightmare. But the house was deep in the country, with no
# other house in sight, and the children had been in London for two years, without so much as once going to the seaside
# even for a day by an excursion train, and so the White House seemed to them a sort of Fairy Palace set down in an
# Earthly Paradise. For London is like prison for children, especially if their relations are not rich.
# '''         # five children and it
#
# text = '''
# Then Aunt Ruby and Aunt Docia put on their flannel petticoats and their plain petticoats and their stiff, starched white
# petticoats with knitted lace all around the flounces. And they put on their beautiful dresses.
#
# Aunt Docia's dress was a sprigged print, dark blue, with sprigs of red flowers and green leaves thick upon it. The
# basque was buttoned down the front with black buttons which looked so exactly like juicy big blackberries that Laura
# wanted to taste them.
#
# Aunt Ruby's dress was wine-colored calico, covered all over with a feathery pattern in lighter wine color. It buttoned
# with gold-colored buttons, and every button had a little castle and a tree carved on it.
#
# Aunt Docia's pretty white collar was fastened in front with a large round cameo pin, which had a lady's head on it. But
# Aunt Ruby pinned her collar with a red rose made of sealing wax. She had made it herself, on the head of a darning
# needle which had a broken eye, so it couldn't be used as a needle any more.
#
# They looked lovely, sailing over the floor so smoothly with their large, round skirts. Their little waists rose up tight
# and slender in the middle, and their cheeks were red and their eyes bright, under the wings of shining, sleek hair.
#
# Ma was beautiful, too, in her dark green delaine, with the little leaves that looked like strawberries scattered over
# it. The skirt was ruffled and flounced and draped and trimmed with knots of dark green ribbon, and nestling at her
# throat was a gold pin. The pin was flat, as long and as wide as Laura's two biggest fingers, and it was carved all over,
# and scalloped on the edges. Ma looked so rich and fine that Laura was afraid to touch her.
# '''     # little house in the big woods

with open(filename, 'r') as file:
    text = file.read()


punctuation = '\‘’",.,:;-()&_“”\n '    # punctuation to remove from text, including a space for when I calculate characters

text = text.replace('!', '.')
text = text.replace('?', '.')
text = text.replace('\n', '')
sentences = text.split('.')

while "" in sentences:              # before this, I was having an incorrect sentence count
    sentences.remove("")

# print(sentences)

sentences = len(sentences)        # calculates the length of the list, which means how many sentences there are (elements of the list)
words = len(text.split(' '))            # calculates the length of the list, which means how many words there are

for char in punctuation:                # remove punctuaiton, as defined above
    text = text.replace(char, '')

characters = len(text)                  # same as above, now only counting letters
                                        # is the code counting spaces as characters here?


# print(f'{sentences} sentences')
# print(f'{words} words')
# print(f'{characters} characters')

ari = ceil(4.17 * (characters/words) + 0.5 * (words/sentences) - 21.43)

if ari >= 14:
    ari = 14

print(
f'''
{sentences} sentences
{words} words
{characters} characters

--------------------------------------------------------

The ARI for the given text is {ari}
This corresponds to a {ari_scale[ari]['grade_level']} level of difficulty
that is suitable for an average person {ari_scale[ari]['ages']} years old.

--------------------------------------------------------
''')
