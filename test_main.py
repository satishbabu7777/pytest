from main import is_even, reverse


# ---------- is_even tests ----------
def test_is_even_positive():
    assert is_even(2) is True, "2 is even"
    assert is_even(3) is False, "3 is not even"
    assert is_even(0) is True, "0 is even"
    assert is_even(-23) is False, "-23 is not even"


def test_is_even_invalid_input():
    assert is_even("-2") is False, "string input should return False"
    assert is_even(-3) is False, "-3 is not even"


# ---------- reverse tests ----------
def test_reverse():
    assert reverse(123) == 321, "reverse of 123 is 321"
    assert reverse(0) == 0, "reverse of 0 is 0"
    assert reverse(100) == 1, "reverse of 100 is 1"


def test_reverse_edge_cases():
    assert reverse(5) == 5, "single digit stays same"