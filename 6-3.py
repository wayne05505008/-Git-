# _*_ coding: utf-8 _*_
# 程式 6-3.py (Python 3.x version)
# 計算單字在文章中出現的頻率
# 只列出出現超過一次以上的單字
import re

article = "WE ARE THE ONCE WEjhkhTOOK A DAY"
new_article = re.sub("[^a-zA-Z\s]", "", article)
words = list(new_article)
word_counts = {}
for word in words:
    if word in word_counts:
        word_counts[word] = word_counts[word] + 1
    else:
        word_counts[word] = 1

key_list = list(word_counts.keys())
key_list.sort()
for key in key_list:
    if word_counts[key] > 0:
        print("{}:{}".format(key, word_counts[key]))
