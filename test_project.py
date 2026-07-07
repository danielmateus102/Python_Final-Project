from project import header, print_options, valid
import pytest


def test_header():
    assert header("CS50") == "CS50 rendered"
    assert header("Hello, world") == "Hello, world rendered"
    assert header("50") == "50 rendered"
    assert header("-50") == "-50 rendered"


def test_print_options():
    # Checks valid input
    assert print_options(1) == "Questions q1 printed successfully"
    assert print_options(2) == "Questions q2 printed successfully"
    assert print_options(3) == "Questions q3 printed successfully"
    assert print_options(4) == "Questions q4 printed successfully"
    assert print_options(5) == "Questions q5 printed successfully"
    assert print_options(6) == "Questions q6 printed successfully"
    assert print_options(7) == "Questions q7 printed successfully"

    # Checks options without questions
    assert print_options(10) == "No questions found at 10"
    assert print_options(-10) == "No questions found at -10"

    # Checks non-int input
    with pytest.raises(ValueError):
        print_options("cs50")

    with pytest.raises(ValueError):
        print_options("Hello world")


def test_valid():
    assert valid("a", "a") == 1
    assert valid("b", "b") == 1
    assert valid("c", "c") == 1
    assert valid("b", "a") == 0
    assert valid(50, "a") == 0
