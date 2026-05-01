


def is_even(number:int) -> bool:
    if(not isinstance(number,int)):
      return False
    return number % 2 == 0