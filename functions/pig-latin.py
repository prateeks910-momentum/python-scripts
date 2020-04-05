def pigLatin(word):
    firstLetter = word[0]
    if firstLetter in 'aeiou':
        word += 'ay'
    else:
        word = word[1:] + firstLetter + 'ay'
    print(word)    

pigLatin('apple')
pigLatin('word')
