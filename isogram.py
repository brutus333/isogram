def is_isogram(word):
    allcaps=word.upper()
    return 1 == max(allcaps.count(uniqueletter) for uniqueletter in \
           set([letter for letter in allcaps if letter.isalpha()])) if word else True