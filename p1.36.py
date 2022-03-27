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