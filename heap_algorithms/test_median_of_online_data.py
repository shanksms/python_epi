from heap_algorithms.median_of_online_data import Median


def test_median():
    median = Median()
    assert median.median(1) == 1
    assert median.median(2) == 1.5
    assert median.median(3) == 2


