from datasets import load_dataset
import random
import re
import collections
d=load_dataset("wikipedia", "20220301.en", split="train")
f = open("ALL_wiki_words.txt", "w")
word_count = {}

def count_words(article):
    # only keeping numbers and words in the article
    article = re.sub(r'[^0-9^A-Z^a-z]', ' ', article)
    # article changed to lowercase
    article = article.lower().split()
    for word in article:
        if word not in word_count:
            word_count[word] = 1
        else:
            word_count[word] += 1

def generate_abbreviations():
    for article in d:
        count_words(article["text"])
    # sorting dictionary by highest count
    word_counter = collections.Counter(word_count)
    for word, count in word_counter.most_common():
        f.write(word + " " + str(count) + "\n")
    f.close()

generate_abbreviations()