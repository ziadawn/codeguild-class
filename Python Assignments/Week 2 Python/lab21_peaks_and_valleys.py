'''
Lab 21: Peaks and Valleys

Define the following functions:

peaks - Returns the indices of peaks. A peak has a lower number on both the left and the right.

valleys - Returns the indices of 'valleys'. A valley is a number with a higher number on both the left and the right.

peaks_and_valleys - uses the above two functions to compile a single list of the peaks and valleys in order of appearance in the original data.

Data    1	2	3	4	5	6	7	6	5	4	5	6	7	8	9	8	7	6	7	8	9
Index	0	1	2	3	4	5	6	7	8	9	10	11	12	13	14	15	16	17	18	19	20
'''

data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]


def peaks(set):
    peaks = []
    for i in range(1, len(set)-1):
        if set[i - 1] < set[i] and set[i + 1] < set[i]:
            peaks.append(i)
    return peaks

def valleys(set):
    valleys = []
    for i in range(1, len(set)-1):
        if set[i-1] > set[i] and set[i+1] > set[i]:
            valleys.append(i)
    return valleys

def peaks_and_valleys(set):
    peaks_and_valleys = []
    peaks_and_valleys.extend(peaks(set))        # remember to call the function!
    peaks_and_valleys.extend(valleys(set))      # .extend attaches one at a time, rather than a whole lost and appending that to another whole list
    return peaks_and_valleys                    # my variable has the same name as the function which can have weird side effects. Change?


print(peaks(data))
print(valleys(data))

print(peaks_and_valleys(data))

x_list = ['']

for num in range(9, 0, -1):     # the -1 means we work backwards through the list
    for i in data:
        if i >= num:
            x_list.append('X')
        else:
            x_list.append(' ')
    x_list.append('\n')

print('  '.join(x_list))       # .join takes the string in front of it and puts it between every element of a list. Helpful!
print(data)

