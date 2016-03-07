# Henry Dinh
# CS 6375.001
# Assignment 2 - Logistic Regression algorithm
# To test the program, read the README file for instructions

import os
import sys
import collections
import re
import math

# Stores emails as dictionaries. email_file_name : Document (class defined below)
training_set = dict()
test_set = dict()

# Vocabulary/tokens in the training set
training_set_vocab = []

# store weights as dictionary. w0 initiall 0.0, others initially 0.5. token : weight value
weights = {'weight_zero': 0.0}

# ham = 0 for not spam, spam = 1 for is spam
classes = ["ham", "spam"]

# Natural learning rate constant and number of iterations for learning weights
learning_constant = .001
num_iterations = 1000

# Read all text files in the given directory and construct the data set, D
# the directory path should just be like "train/ham" for example
# storage is the dictionary to store the email in
# True class is the true classification of the email (spam or ham)
def makeDataSet(storage_dict, directory, true_class):
    for dir_entry in os.listdir(directory):
        dir_entry_path = os.path.join(directory, dir_entry)
        if os.path.isfile(dir_entry_path):
            with open(dir_entry_path, 'r') as text_file:
                # stores dictionary of dictionary of dictionary as explained above in the initialization
                text = text_file.read()
                storage_dict.update({dir_entry_path: Document(text, bagOfWords(text), true_class)})


# Extracts the vocabulary of all the text in a data set
def extractVocab(data_set):
    all_text = ""
    v = []
    for x in data_set:
        all_text += data_set[x].getText()
    for y in bagOfWords(all_text):
        v.append(y)
    return v


# counts frequency of each word in the text files and order of sequence doesn't matter
def bagOfWords(text):
    bagsofwords = collections.Counter(re.findall(r'\w+', text))
    return dict(bagsofwords)


# Learn weights
def learnWeights():
    pass


# Document class to store email instances easier
class Document:
    text = ""
    word_freqs = {}

    # spam or ham
    true_class = ""
    learned_class = ""

    # Constructor
    def __init__(self, text, counter, true_class):
        self.text = text
        self.word_freqs = counter
        self.true_class = true_class

    def getText(self):
        return self.text

    def getWordFreqs(self):
        return self.word_freqs

    def getTrueClass(self):
        return self.true_class

    def getLearnedClass(self):
        return self.learned_class

    def setLearnedClass(self, guess):
        self.learned_class = guess


# takes directories holding the data text files as paramters. "train/ham" for example
def main(training_spam_dir, training_ham_dir, test_spam_dir, test_ham_dir):
    # Set up data sets. Dictionaries containing the text, word frequencies, and true/learned classifications
    makeDataSet(training_set, training_spam_dir, classes[1])
    makeDataSet(training_set, training_ham_dir, classes[0])
    makeDataSet(test_set, test_spam_dir, classes[1])
    makeDataSet(test_set, test_ham_dir, classes[0])

    # Extract training set vocabulary
    training_set_vocab = extractVocab(training_set)

    # Set all weights in training set vocabulary to be initially 0.5. w0 ('weight_zero') is initially 0.0
    for i in training_set_vocab:
        weights[i] = 0.5

    # Prints out the data set for testing purposes to make sure data is correctly read
    # for i in test_set:
    #     print i + " : "
    #     print test_set[i].getText()
    #     print test_set[i].getWordFreqs()
    #     print test_set[i].getTrueClass()
    #     print


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])