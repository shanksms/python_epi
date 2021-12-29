from hypothesis import given, example
from hypothesis.strategies import text
from hypothesis import assume
from strings.runlength_encoding import encode, decode


@given(text())
@example('')
def test_encode(text):
    #assume(not text == '')
    assert text == decode(encode(text))

