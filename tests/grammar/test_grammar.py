import pytest
from parsimonious.exceptions import ParseError
from daidepp.grammar.grammar import DAIDELevel


@pytest.mark.parametrize(
    "grammar",
    [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160],
    indirect=True,
)
def test_level_10_messages(grammar, level_10_messages):
    for message in level_10_messages:
        grammar.parse(message)


@pytest.mark.parametrize(
    "grammar",
    [20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160],
    indirect=True,
)
def test_level_20_messages(grammar, level_20_messages):
    for message in level_20_messages:
        grammar.parse(message)


@pytest.mark.parametrize(
    "grammar", [30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160], indirect=True
)
def test_level_30_messages(grammar, level_30_messages):
    for message in level_30_messages:
        grammar.parse(message)


@pytest.mark.parametrize(
    "grammar", [40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160], indirect=True
)
def test_level_40_messages(grammar, level_40_messages):
    for message in level_40_messages:
        grammar.parse(message)


@pytest.mark.parametrize(
    "grammar", [50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160], indirect=True
)
def test_level_50_messages(grammar, level_50_messages):
    for message in level_50_messages:
        grammar.parse(message)


@pytest.mark.parametrize(
    "grammar", [60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160], indirect=True
)
def test_level_60_messages(grammar, level_60_messages):
    for message in level_60_messages:
        grammar.parse(message)


@pytest.mark.parametrize(
    "grammar", [70, 80, 90, 100, 110, 120, 130, 140, 150, 160], indirect=True
)
def test_level_70_messages(grammar, level_70_messages):
    for message in level_70_messages:
        grammar.parse(message)


@pytest.mark.parametrize(
    "grammar", [80, 90, 100, 110, 120, 130, 140, 150, 160], indirect=True
)
def test_level_80_messages(grammar, level_80_messages):
    for message in level_80_messages:
        grammar.parse(message)


@pytest.mark.parametrize("grammar", [90, 100, 110, 120, 130, 140, 150, 160], indirect=True)
def test_level_90_messages(grammar, level_90_messages):
    for message in level_90_messages:
        grammar.parse(message)


@pytest.mark.parametrize("grammar", [100, 110, 120, 130, 140, 150, 160], indirect=True)
def test_level_100_messages(grammar, level_100_messages):
    for message in level_100_messages:
        grammar.parse(message)


@pytest.mark.parametrize("grammar", [110, 120, 130, 140, 150, 160], indirect=True)
def test_level_110_messages(grammar, level_110_messages):
    for message in level_110_messages:
        grammar.parse(message)


@pytest.mark.parametrize("grammar", [120, 130, 140, 150, 160], indirect=True)
def test_level_120_messages(grammar, level_120_messages):
    for message in level_120_messages:
        grammar.parse(message)


@pytest.mark.parametrize("grammar", [130, 140, 150, 160], indirect=True)
def test_level_130_messages(grammar, level_130_messages):
    for message in level_130_messages:
        grammar.parse(message)


@pytest.mark.parametrize("grammar", [140, 150, 160], indirect=True)
def test_level_140_messages(grammar, level_140_messages):
    for message in level_140_messages:
        grammar.parse(message)


@pytest.mark.parametrize("grammar", [150, 160], indirect=True)
def test_level_150_messages(grammar, level_150_messages):
    for message in level_150_messages:
        grammar.parse(message)


@pytest.mark.parametrize("grammar", [160], indirect=True)
def test_level_160_messages(grammar, level_160_messages):
    for message in level_160_messages:
        grammar.parse(message)


@pytest.mark.parametrize("grammar", [160], indirect=True)
def test_bad_messages(grammar, bad_messages):
    with pytest.raises(ParseError):
        for message in bad_messages:
            grammar.parse(message)
