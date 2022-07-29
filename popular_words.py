from datasets import load_dataset
import random
import re
import collections
d=load_dataset("wikipedia", "20220301.en", split="train")
f = open("ALL_wiki_words.txt", "w")
word_count = {}

def count_words(article):
    article = re.sub(r'[^0-9^A-Z^a-z]', ' ', article)
    article = article.lower().split()
    for word in article:
        if word not in word_count:
            word_count[word] = 1
        else:
            word_count[word] += 1
# def quick_sort(list):
#     if len(list) == 1:
#         return list
#     pivot_value = list[0]
#     left = 1
#     right = len(list)-1
#     stuck = False
#     while left < right and stuck == False:
#         stuck = True
#         if list[left] < pivot_value:
#             left+=1
#             stuck = False
#         if list[right] > pivot_value:
#             right-=1
#             stuck = False
#     if stuck:
#         a = list[left]
#         list[left] = list[right]
#         list[right] = a
#         quick_sort(list)
#     else:
#         a = list[left]
#         list[left] = list[0]
#         list[0] = a
#         return quick_sort(list)[0:pivot_value] + quick_sort[left] + quick_sort(list)[pivot_value+1:]
def generate_abbreviations():
	# random_index = 36000
    for article in d:
        count_words(article["text"])
    word_counter = collections.Counter(word_count)
    for word, count in word_counter.most_common():
        f.write(word + " " + str(count) + "\n")
    #word_count_sorted = collections.OrderedDict(word_count)
    f.close()
generate_abbreviations()