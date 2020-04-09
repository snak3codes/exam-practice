"""Prep 2 Synthesize Sample Tests

=== CSC148 Winter 2020 ===
Department of Mathematical and Computational Sciences,
University of Toronto Mississauga

=== Module Description ===
This module contains sample tests for Prep 2.

WARNING: THIS IS AN EXTREMELY INCOMPLETE SET OF TESTS!
Add your own to practice writing tests and to be confident your code is correct.

For more information on hypothesis (one of the testing libraries we're using),
please see
<https://mcs.utm.utoronto.ca/~148/software/hypothesis.html>.

Note: this file is for support purposes only, and is not part of your
submission.
"""
from hypothesis import given
from hypothesis.strategies import integers
from prep2 import Spinner
from random import seed, randint

seed(0)


# This is a hypothesis test; it generates a random integer to use as input,
# so that we don't need to hard-code a specific number of slots in the test.
@given(slots=integers(min_value=1))
def test_new_spinner_position(slots: int) -> None:
    """Test that the position of a new spinner is always 0."""
    spinner = Spinner(slots)
    assert spinner.position == 0

    spinner.spin(slots)
    assert spinner.position == 0

    spinner.spin(slots - 1)
    assert spinner.position == slots - 1


def test_doctest() -> None:
    """Test the given doctest in the Spinner class docstring."""
    spinner = Spinner(8)

    spinner.spin(4)
    assert spinner.position == 4

    spinner.spin(2)
    assert spinner.position == 6

    spinner.spin(2)
    assert spinner.position == 0

    spinner.spin(8)
    assert spinner.position == 0

    spinner.spin(100)
    assert spinner.position == 4

    spinner.spin_randomly()
    assert spinner.position == 2

    if __name__ == '__main__':
        import pytest

        pytest.main(['prep2_sample_test.py'])
