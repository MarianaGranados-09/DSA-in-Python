''''
Write a Python program that inputs a list of words, separated by whitespace, and outputs how many times each word appears in the list. You
need not worry about efficiency at this point, however, as this topic is
something that will be addressed later in this book.
'''

#.split() #return a list of strings, as separated by spaces

listofWords=str(input('Enter a list of words, each one separated by a whitespace: '))
#print(listofWords)

NewList=listofWords.split()

#print(NewList)
wordCount={}

for item in NewList: #for each word in the list
    wordCount[item] = NewList.count(item) #Take each item from the word #list, and count them
print(wordCount)



#Python program to count how many times a letter appears in a name
NameCount = {}

def _countLetters(Name):
    #n = len(Name)
    for n in Name:
        NameCount[n] = Name.count(n)
    print(NameCount)


_countLetters('Mariana Granados')

