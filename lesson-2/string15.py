sentence=input('Enter a sentence:')
words=sentence.split()
acronym=' '.join([word[0].upper() for word in words])
print(f'the acronym is: {acronym}')