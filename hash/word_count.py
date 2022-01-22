from typing import List, Tuple
from collections import Counter


def top_k_word_count(k: int, words: List) -> List[Tuple]:
    if k > len(words):
        raise ValueError('size should be more than or equal to {}'.format(k))
    word_count = dict(Counter(words))
    word_count_tuple = [(k, v) for k, v in word_count.items()]
    sorted_word_count = sorted(word_count_tuple, key=lambda x: x[1], reverse=True)
    return sorted_word_count[:k]