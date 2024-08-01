# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 15:40:07 2024

@author: Arun.Rameshbabu
"""

text = """Feeling groggy this morning? On your third cup of the black stuff? Coffee may be an energy lifeline for many – but how much is too much?

While coffee shops have been on the decline thanks to a lack of commuters, sales of homebrewed caffeinated drinks have soared. Coffee was the largest growth area for the world’s largest food producer Nestle, with a 17% increase in Nespresso products in the first few months of 2021.

It’s pretty easy to understand why: we are all looking for a dose of energy to beat social fatigue now that restrictions have eased, as well as searching for comfort and warmth to help get us through the day. From a classic flat white to a trendy Tik Tok protein coffee, we just can’t get enough.

Let’s be honest though, coffee gets a bad rap, particularly for anyone who’s found pouring the third mug of the day before 10am. But what is it about coffee that we are all worried about?"""

# Remove newlines and punctuations
text = text.replace('\n','')
text = text.replace(',','')
text = text.replace('.','')
text = text.replace('?','')
text = text.replace('-','')

# Turn to lowercase
text = text.lower()

# Turn to a list
words = text.split(' ')

def count_words(word_list):
    word_count = {}
    for word in word_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count


def display_word_count(word_count):
    words = list(word_count.keys())
    words.sort(key=str.lower)
    for word in words:
        count = word_count[word]
        print(word, '=', count)

def main():
    print("The Word Counter program")
    print()
    
    print(f"Number of words = {len(words)}")
    word_count_printable = count_words(words)
    print(f'Number of unique words = {len(list(word_count_printable.keys()))}')
    print('Word occurences: ')
    for key, value in word_count_printable.items():
        print('\t' + key + ' = ' + str(value))

if __name__ == '__main__':
    main()
