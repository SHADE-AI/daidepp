# DAIDE++

| Feature | Tools |
|---|---|
| Languages | [![Python 3.7](https://img.shields.io/badge/Python-3.7-3776AB?logo=python&logoColor=ffdd54)](https://www.python.org/downloads/release/python-370/) [![Markdown](https://img.shields.io/badge/markdown-%23000000.svg?logo=markdown&logoColor=white)](https://daringfireball.net/projects/markdown/) |
| Git | [![Conventional Commits](https://img.shields.io/badge/Conventional%20Commits-1.0.0-%23FE5196?logo=conventionalcommits&logoColor=white)](https://conventionalcommits.org) |
| Formatting | [![Black](https://img.shields.io/badge/Code%20Style-black-000000)](https://github.com/psf/black) [![docformatter](https://img.shields.io/badge/Docstring%20Formatter-docformatter-fedcba.svg)](https://github.com/PyCQA/docformatter) [![numpy](https://img.shields.io/badge/Docstring%20Style-numpy-459db9.svg)](https://numpydoc.readthedocs.io/en/latest/format.html) [![Imports: isort](https://img.shields.io/badge/%20Imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/) |

Repo to store universal communication specification and parser.

- The original DAIDE specification is [here](daide-syntax.pdf)
- The working markdown document that will included DAIDE enhancements is [here](daide-specification.md)
- The machine-parsable grammar can be found in [this `.py` file](./daidepp/parser/grammar.py)

In order to make updates, please make sure to update both the `grammar.py` file as well as the `daide-specification.md` file so that changes are both human and machine readable.
