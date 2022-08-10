# daidepp
DAIDE parser using [parsimonious](https://github.com/erikrose/parsimonious). Parsimonious is a python package that uses "a simplified sort of EBNF notation" to define a grammar. The parser currently supports all 130 levels of DAIDE. 

## How to use
Using the grammar in grammar.py, you can create a parse tree from a DAIDE press message or reply. The nodes of the parse tree can be visited to return something more useful. The visiting rules for each of the nodes of the parse tree are defined in node_visitor.py.

Example:
```python3
>>> parse_tree = grammar.parse('PRP (AND (SLO (ENG)) (SLO (GER)) (SLO (RUS)) (AND (SLO (ENG)) (SLO (GER)) (SLO (RUS))))')
>>> dv = DaideVisitor()
>>> output = dv.visit(parse_tree)
>>> print(output)
('PRP',
 ('AND',
  [('SLO', 'ENG'),
   ('SLO', 'GER'),
   ('SLO', 'RUS'),
   ('AND', [('SLO', 'ENG'), ('SLO', 'GER'), ('SLO', 'RUS')])]))
```
If the DAIDE token is not in the grammar or if the message is malformed, the parser will just thrown an exception. We're currently working on returning a list of unrecognized tokens instead of just erroring out.