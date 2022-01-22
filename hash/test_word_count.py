import pytest

from hash import word_count


@pytest.mark.parametrize('words, k, result',
                         [
                             (['a', 'b', 'c', 'a', 'b', 'a', 'd'], 2, [('a', 3), ('b', 2)]),

                         ])
def test_top_k_word_count(words, k, result):
    assert word_count.top_k_word_count(k, words) == result


def test_top_k_word_count_k_is_more_than_word_length():
    with pytest.raises(ValueError) as exc:
        word_count.top_k_word_count(2, ['a'])
    assert 'size should be more than or equal to 2' == str(exc.value)
