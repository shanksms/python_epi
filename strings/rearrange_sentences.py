'''
You are given a string sentence representing a valid sentence. A valid sentence consists of words separated by single-spaces, ending with a period. Each word contains only latin letters. The first word in the sentence always starts with capital letter, and all others are lowercase. In other words, a sentence is a string matching the regex ^[A-Z][a-z]*( [a-z]+)*\.$.

Your task is to rearrange the words in the sentence in ascending order of their length. In the case of a tie, the words should be ordered according to their relative order in the initial sentence. The final sequence should be formatted to be a valid sentence as well (ie: match the regex ^[A-Z][a-z]*( [a-z]+)*\.$).

Example

For sentence = "Houston we have a problem.", the output should be
rearrangeTheSentence(sentence) = "A we have houston problem.".
'''

import operator


def rearrangeTheSentence(sentence):
    sentence = sentence.strip(".")
    words = sentence.split()
    lengths = [len(word) for word in words]

    pairs = list(zip(lengths, words))
    pairs.sort(key=operator.itemgetter(0))
    new_sentence = []
    for i, j in pairs:
        new_sentence.append(j)
    new_sentence = " ".join(new_sentence)\
        .lower()
    new_sentence = new_sentence[0].upper() + new_sentence[1:] + "."
    return new_sentence

if __name__ == '__main__':
    print(rearrangeTheSentence('I love to code.'))