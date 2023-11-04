from project2 import *


def test_check_calculations():
    assert calculation(3, 4) == 7
    assert outcome(calculation(6, 7)) == "The outcome is 13"


test_check_calculations()
