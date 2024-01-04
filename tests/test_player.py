from player import validate_input


def test_validate_input():
    # Test case 1: Valid input
    assert validate_input(1, 2) is True

    # Test case 2: Out of bound input
    assert validate_input(4, 2) is False
