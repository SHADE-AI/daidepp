# DAIDE++

| Feature | Tools |
|---|---|
| Languages | [![Python 3.7](https://img.shields.io/badge/Python-3.7-3776AB?logo=python&logoColor=ffdd54)](https://www.python.org/downloads/release/python-370/) [![Markdown](https://img.shields.io/badge/markdown-%23000000.svg?logo=markdown&logoColor=white)](https://daringfireball.net/projects/markdown/) |
| Git | [![Conventional Commits](https://img.shields.io/badge/Conventional%20Commits-1.0.0-%23FE5196?logo=conventionalcommits&logoColor=white)](https://conventionalcommits.org) |
| Formatting | [![Black](https://img.shields.io/badge/Code%20Style-black-000000)](https://github.com/psf/black) [![docformatter](https://img.shields.io/badge/Docstring%20Formatter-docformatter-fedcba.svg)](https://github.com/PyCQA/docformatter) [![numpy](https://img.shields.io/badge/Docstring%20Style-numpy-459db9.svg)](https://numpydoc.readthedocs.io/en/latest/format.html) [![Imports: isort](https://img.shields.io/badge/%20Imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/) |
| Testing | [![Pytest](https://img.shields.io/badge/pytest-%23000000.svg?logo=pytest)](https://docs.pytest.org/)

DAIDE parser using [parsimonious](https://github.com/erikrose/parsimonious). Parsimonious is a python package that uses "a simplified sort of EBNF notation" to define a grammar. The parser currently supports all 130 levels of DAIDE.

- The original DAIDE specification is [here](daide-syntax.pdf)
- The working markdown document that will included DAIDE enhancements is [here](daide-specification.md)
- The machine-parsable grammar can be found in [this `.py` file](./src/daidepp/grammar.py)

## Use

Using the grammar in `grammar.py`, you can create a parse tree from a DAIDE press message or reply. The nodes of the parse tree can be visited to return something more useful. The visiting rules for each of the nodes of the parse tree are defined in `node_visitor.py`.

Example:

```python3
>>> from daidepp import create_daide_grammar, daide_visitor
>>> grammar = create_daide_grammar(level=130)
>>> message = 'PRP (AND (SLO (ENG)) (SLO (GER)) (SLO (RUS)) (AND (SLO (ENG)) (SLO (GER)) (SLO (RUS))))'
>>> parse_tree = grammar.parse(message)
>>> output = daide_visitor.visit(parse_tree) # object composed of dataclass objects in keywords.py
>>> print(output)
PRP ( AND ( SLO ( ENG ) ) ( SLO ( GER ) ) ( SLO ( RUS ) ) ( AND ( SLO ( ENG ) ) ( SLO ( GER ) ) ( SLO ( RUS ) ) ) )
```

If the DAIDE token is not in the grammar or if the message is malformed, the parser will just thrown an exception. We're currently working on returning a list of unrecognized tokens instead of just erroring out.


In addition, DAIDE strings can be constructed using the classes in `keywords.py`. Each class has type hints that indicate the parameters that should be used.

Example:

```python3
>>> from daidepp import AND, PRP, PCE
>>> str(AND(PRP(PCE("AUS")), PRP(PCE("AUS", "ENG"))))
`AND ( PRP ( PCE ( AUS ) ) ) ( PRP ( PCE ( AUS ENG ) ) ) ( PRP ( PCE ( AUS ENG FRA ) ) )`
 ```
Each class in `keywords.py` uses different parameters for instantiation, so it is recommended to carefully follow the type hints or checkout `tests/test_keywords.py`, which provides examples for each class. 

## Pull Requests

Three files should be updated whenever making a PR:

- [`grammar.py`](./src/daidepp/grammar.py): the machine-readable grammar
- [`node_visitor.py`](./src/daidepp/node_visitor.py): the visitor object to parse a message
- [The daide markdown specification](./daide-specification.md): the human-readable specification
