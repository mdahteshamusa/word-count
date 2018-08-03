from collections import Counter, OrderedDict
import re


def n_most_frequent(text, top_n=5):
    # find words in text using regex
    words = re.findall(r'\w+', text)
    # find top-n most frequently occurring words
    frequent = Counter(words).most_common(top_n)
    od = OrderedDict()
    for k, v in frequent:
        od[k] = v
    key = 'top-{}-most-frequent-words'.format(top_n)
    return {key: od}
