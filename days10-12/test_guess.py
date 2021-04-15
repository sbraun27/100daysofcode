from fizzbuzz import fizzbuzz
from unittest.mock import patch
import pytest

import random

from guessing_game import get_random_number, GuessingGame

# pytest --cov-report term-missing --cov='.'

# parameterize testing with pytest:


@pytest.mark.parametrize("arg, ret", [
    (1, 1),
    (2, 2),
    (3, "Fizz"),
    (4, 4),
    (5, "Buzz"),
    (6, "Fizz"),
    (7, 7),
    (8, 8),
    (9, "Fizz"),
    (15, "Fizz Buzz")
])
def test_fizzbuzz(arg, ret):
    assert fizzbuzz(arg) == ret


@patch.object(random, "randint")
def test_get_random_number(m):
    m.return_value = 17
    assert get_random_number() == 17


@patch("builtins.input", side_effect=[11, "12", "bob", 12, 5, -1, 21, 7, None])
def test_guess(inp):
    game = GuessingGame()
    # good
    assert game.guess() == 11
    assert len(game._guesses) == 1

    assert game.guess() == 12
    assert len(game._guesses) == 2

    # Not a Number
    with pytest.raises(ValueError):
        game.guess()
    assert len(game._guesses) == 2

    with pytest.raises(ValueError):
        game.guess()

    assert game.guess() == 5

    with pytest.raises(ValueError):
        game.guess()

    with pytest.raises(ValueError):
        game.guess()

    assert game.guess() == 7

    with pytest.raises(ValueError):
        game.guess()

    assert len(game._guesses) == 4


def test_validate_guess(capfd):
    game = GuessingGame()
    game._answer = 2

    assert not game._validate_guess(1)
    out, _ = capfd.readouterr()
    assert out.rstrip() == "1 is too low"

    assert not game._validate_guess(3)
    out, _ = capfd.readouterr()
    assert out.rstrip() == "3 is too high"

    assert game._validate_guess(2)
    out, _ = capfd.readouterr()
    assert out.rstrip() == "2 is correct!"


@patch("builtins.input", side_effect=[4, 22, 9, 4, 6])
def test_game_win(inp, capfd):
    game = GuessingGame()
    game._answer = 6

    game()
    assert game._win is True
    out, _ = capfd.readouterr()
    expected = ["4 is too low", "Number not in range",
                "9 is too high", "You already guessed that number",
                "6 is correct!", "It took you 3 guesses"]

    output = [line.strip() for line in out.split("\n") if line.strip()]
    for line, expect in zip(output, expected):
        assert line == expect


@patch("builtins.input", side_effect=[4, 22, 19, 4, 6, 17, 16])
def test_game_loss(inp, capfd):
    game = GuessingGame()
    game._answer = 18

    game()
    assert game._win is False
    out, _ = capfd.readouterr()
    expected = ["4 is too low", "Number not in range",
                "19 is too high", "You already guessed that number",
                "6 is too low", "17 is too low",
                "16 is too low", "Guessed 5 times, and answer was 18"]

    output = [line.strip() for line in out.split("\n") if line.strip()]
    for line, expect in zip(output, expected):
        assert line == expect
