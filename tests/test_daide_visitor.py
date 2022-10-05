from typing import List


def test_basic_visitor(sample_daide_messages: List[str]):
    from daidepp.daide_visitor import daide_visitor
    from daidepp.grammar import create_daide_grammar

    grammar = create_daide_grammar(level=130)
    for message in sample_daide_messages:
        tree = grammar.parse(message)
        daide_visitor.visit(tree)
    assert True
