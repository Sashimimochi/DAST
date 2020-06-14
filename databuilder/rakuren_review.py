import os
import numpy as np


filepath = 'data/rakuten_ja/rakuten_reviews.txt'
with open(filepath, 'r', encoding='utf-8') as f:
    data = [line.rstrip('\n').split(' __SEP__ ') for line in f.readlines()]


def rescore(x):
    if len(x.split(' ')) > 0:
        tmp = np.array(x.split(' '), dtype=np.float)
        val = np.average(tmp)
    else:
        val = x

    return 5.0 if float(val) >= 4.0 else 1.0

reviews = []
for d in data:
    if d[0] == '':
        continue
    reviews += ['{{"score": {}, "review": "{}"}}'.format(rescore(d[0]), d[1].replace("\"", "").replace("\\", ""))]


with open('data/rakuten_ja/rakuten_reviews.json', 'w', encoding='utf-8') as f:
    f.write('\n'.join(reviews))