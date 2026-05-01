from main import is_even

def test_is_even_positive():
    assert is_even(2) == True,"2 is even number"
    assert is_even(3) == False,"3 is not an even number"
    assert is_even(0) == True,"0 is an even number"
    assert is_even(-23) == False,"-23 is not an even number"


def test_is_even_negative():
    assert is_even("-2") == False,"-2 is an even number"
    assert is_even(-3) == False,"-3 is not an even number"

