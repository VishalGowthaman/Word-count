# Developed by Vishal Gowthaman K.R
# Reference no: 21002997
# To write a program for getting the word count from a file.

num_of_words = 0
file = open('text1.txt')
wordtext = file.read()
words = wordtext.split()
num_of_words = len(words)
print("Number of words = ",num_of_words)
        
        
