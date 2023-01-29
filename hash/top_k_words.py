import heapq
from typing import List
from collections import Counter
from heapq import heapify, heappop

"""
Given an array of strings words and an integer k, return the k most frequent strings.

Return the answer sorted by the frequency from highest to lowest. Sort the words with the same frequency by their lexicographical order.

 

Example 1:

Input: words = ["i","love","leetcode","i","love","coding"], k = 2
Output: ["i","love"]
Explanation: "i" and "love" are the two most frequent words.
Note that "i" comes before "love" due to a lower alphabetical order.
Example 2:

Input: words = ["the","day","is","sunny","the","the","the","sunny","is","is"], k = 4
Output: ["the","is","sunny","day"]
Explanation: "the", "is", "sunny" and "day" are the four most frequent words, with the number of occurrence being 4, 3, 2 and 1 respectively.

"""
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        """

        """


        word_counter = Counter(words)
        word_counter_list = list(word_counter.items())
        """
        lambda x: (-x[1], x[0]) will first sort it by -x[1], in case of tie, it will sort it by x[0]
        """
        word_counter_list = sorted(word_counter_list, key=lambda x: (-x[1], x[0]))[:k]
        return [x[0] for x in word_counter_list]

    def approach2(self, words: List[str], k: int) -> List[str]:
        """
        Algo:
        1. Create a word counter map
        2. Heapify the list of words. First sort it by counter. in case of tie, sort it lexicographically.
        :param words:
        :param k:
        :return:
        """

        cnt = Counter(words)
        """
        According to the heapq documentation, the way to customize the heap order is to have each element on the heap
         to be a tuple, with the first tuple element being one that accepts normal Python comparisons.

The functions in the heapq module are a bit cumbersome (since they are not object-oriented), and always require 
our heap object (a heapified list) to be explicitly passed as the first parameter. We can kill two birds with one stone by creating a very simple wrapper class that will allow us to specify a key function, and present the heap as an object.
        """
        heap = [(-freq, word) for word, freq in cnt.items()]
        heapify(heap)

        return [heappop(heap)[1] for _ in range(k)]
