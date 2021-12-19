from hypothesis import given
from hypothesis.strategies import integers, lists
from arrays.max_product_of_two_elements import max_product

@given(lists(integers(), min_size=2))
def test_max_product(li):
    print(li)
    assert max_product(li) >= li[0] * li[1]