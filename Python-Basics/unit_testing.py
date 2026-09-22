from UnitTest import square
import pytest

def main():
    # test_square()
    assert_square()

# def test_square():
#     if(square(2) == 4):
#         print("function working porperly")
#     else:
#         print("function not work")

def assert_square():
    # assert square(2) == 4
    # assert square(3) != 9 # AssertionError = for assert error

    try:
        assert square(2) == 4
    except AssertionError:
        print("2 square was not 4")
    try:
        assert square(3) != 9
    except AssertionError:
        print("3 square is 9 you used wrong operator use ==")


if __name__ == "__main__":
    main()