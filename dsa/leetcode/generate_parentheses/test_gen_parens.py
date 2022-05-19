from gen_parens import *


def test_generate_parentheses():
    assert generate_parentheses(1) == ["()"]
    assert generate_parentheses(3) == ["((()))","(()())","(())()","()(())","()()()"]

