import pytest

from daidepp.keywords.base_keywords import *


@pytest.mark.parametrize(
    ["input", "expected_output"],
    [
        (("AUS", "FLT", "ALB"), "AUS FLT ALB"),
        (("ENG", "AMY", "ANK"), "ENG AMY ANK"),
        (("FRA", "FLT", "APU"), "FRA FLT APU"),
        (("GER", "AMY", "ARM"), "GER AMY ARM"),
        (("ITA", "FLT", "BEL"), "ITA FLT BEL"),
        (("RUS", "AMY", "BER"), "RUS AMY BER"),
        (("TUR", "FLT", "BRE"), "TUR FLT BRE"),
    ],
)
def test_Unit(input, expected_output, daide_parser):
    unit = Unit(*input)
    assert str(unit) == expected_output
    assert unit == daide_parser(expected_output)
    hash(unit)


@pytest.mark.parametrize(
    ["input", "expected_output"],
    [
        ((Unit("AUS", "FLT", "ALB"),), "( AUS FLT ALB ) HLD"),
        ((Unit("ENG", "AMY", "ANK"),), "( ENG AMY ANK ) HLD"),
    ],
)
def test_HLD(input, expected_output, daide_parser):
    hld = HLD(*input)
    assert str(hld) == expected_output
    assert hld == daide_parser(expected_output)
    hash(hld)


@pytest.mark.parametrize(
    ["input", "expected_output"],
    [
        ((Unit("AUS", "FLT", "ALB"), "BUL"), "( AUS FLT ALB ) MTO BUL"),
        ((Unit("AUS", "FLT", "ALB"), Location("BUL")), "( AUS FLT ALB ) MTO BUL"),
        ((Unit("ENG", "AMY", "ANK"), "CLY"), "( ENG AMY ANK ) MTO CLY"),
        ((Unit("ENG", "AMY", "ANK"), Location("CLY")), "( ENG AMY ANK ) MTO CLY"),
    ],
)
def test_MTO(input, expected_output, daide_parser):
    mto = MTO(*input)
    assert str(mto) == expected_output
    assert mto == daide_parser(expected_output)
    hash(mto)


@pytest.mark.parametrize(
    ["input", "expected_output"],
    [
        (
            (Unit("AUS", "FLT", "ALB"), Unit("ENG", "AMY", "ANK"), "BUL"),
            "( AUS FLT ALB ) SUP ( ENG AMY ANK ) MTO BUL",
        ),
        (
            (Unit("FRA", "FLT", "APU"), Unit("GER", "AMY", "ARM"), "CLY"),
            "( FRA FLT APU ) SUP ( GER AMY ARM ) MTO CLY",
        ),
        (
            (
                Unit("FRA", "FLT", Location("APU")),
                Unit("GER", "AMY", Location("ARM")),
                "CLY",
            ),
            "( FRA FLT APU ) SUP ( GER AMY ARM ) MTO CLY",
        ),
        (
            (
                Unit("AUS", "FLT", Location("ALB")),
                Unit("ENG", "AMY", Location("ANK")),
                "BUL",
            ),
            "( AUS FLT ALB ) SUP ( ENG AMY ANK ) MTO BUL",
        ),
    ],
)
def test_SUP(input, expected_output, daide_parser):
    sup = SUP(*input)
    assert str(sup) == expected_output
    assert sup == daide_parser(expected_output)
    hash(sup)


@pytest.mark.parametrize(
    ["supporting_unit", "supported_unit", "province_no_coast"],
    [
        (
            Unit("AUS", "FLT", Location("ALB")),
            Unit("ENG", "AMY", Location("ANK")),
            "BUL",
        ),
        (
            Unit("AUS", "FLT", Location("ALB")),
            Unit("ENG", "AMY", Location("ANK")),
            Location("BUL"),
        ),
    ],
)
def test_SUP_location(supporting_unit, supported_unit, province_no_coast, daide_parser):
    sup = SUP(
        supported_unit=supported_unit,
        supporting_unit=supporting_unit,
        province_no_coast=province_no_coast,
    )
    assert isinstance(sup.province_no_coast, str)
    assert isinstance(sup.province_no_coast_location, Location)
    assert sup == daide_parser(str(sup))
    hash(sup)


@pytest.mark.parametrize(
    ["input", "expected_output"],
    [
        (
            (Unit("AUS", "FLT", "ALB"), Unit("ENG", "AMY", "ANK"), "BUL"),
            "( AUS FLT ALB ) CVY ( ENG AMY ANK ) CTO BUL",
        ),
        (
            (Unit("FRA", "FLT", "APU"), Unit("GER", "AMY", "ARM"), "CLY"),
            "( FRA FLT APU ) CVY ( GER AMY ARM ) CTO CLY",
        ),
    ],
)
def test_CVY(input, expected_output, daide_parser):
    cvy = CVY(*input)
    assert str(cvy) == expected_output
    assert cvy == daide_parser(expected_output)
    hash(cvy)


@pytest.mark.parametrize(
    ["input", "expected_output"],
    [
        (
            (Unit("AUS", "FLT", "ALB"), "BUL", "ADR"),
            "( AUS FLT ALB ) CTO BUL VIA ( ADR )",
        ),
        (
            (Unit("ENG", "AMY", "ANK"), "CLY", "ADR", "AEG"),
            "( ENG AMY ANK ) CTO CLY VIA ( ADR AEG )",
        ),
        (
            (Unit("FRA", "FLT", "APU"), "CON", "ADR", "AEG", "BAL"),
            "( FRA FLT APU ) CTO CON VIA ( ADR AEG BAL )",
        ),
        (
            (Unit("AUS", "FLT", "ALB"), Location("BUL"), "ADR"),
            "( AUS FLT ALB ) CTO BUL VIA ( ADR )",
        ),
        (
            (Unit("ENG", "AMY", "ANK"), Location("CLY"), "ADR", "AEG"),
            "( ENG AMY ANK ) CTO CLY VIA ( ADR AEG )",
        ),
        (
            (Unit("FRA", "FLT", "APU"), Location("CON"), "ADR", "AEG", "BAL"),
            "( FRA FLT APU ) CTO CON VIA ( ADR AEG BAL )",
        ),
    ],
)
def test_MoveByCVY(input, expected_output, daide_parser):
    mvc = MoveByCVY(*input)
    assert str(mvc) == expected_output
    assert mvc == daide_parser(expected_output)
    hash(mvc)


@pytest.mark.parametrize(
    ["input", "expected_output"],
    [
        ((Unit("AUS", "FLT", "ALB"), "BUL"), "( AUS FLT ALB ) RTO BUL"),
        ((Unit("AUS", "FLT", "ALB"), Location("BUL")), "( AUS FLT ALB ) RTO BUL"),
        ((Unit("ENG", "AMY", "ANK"), "CLY"), "( ENG AMY ANK ) RTO CLY"),
        ((Unit("ENG", "AMY", "ANK"), Location("CLY")), "( ENG AMY ANK ) RTO CLY"),
    ],
)
def test_RTO(input, expected_output, daide_parser):
    rto = RTO(*input)
    assert str(rto) == expected_output
    assert rto == daide_parser(expected_output)
    hash(rto)


@pytest.mark.parametrize(
    ["input", "expected_output"],
    [
        ((Unit("AUS", "FLT", "ALB"),), "( AUS FLT ALB ) DSB"),
        ((Unit("ENG", "AMY", "ANK"),), "( ENG AMY ANK ) DSB"),
    ],
)
def test_DSB(input, expected_output, daide_parser):
    dsb = DSB(*input)
    assert str(dsb) == expected_output
    assert dsb == daide_parser(expected_output)
    hash(dsb)


@pytest.mark.parametrize(
    ["input", "expected_output"],
    [
        ((Unit("AUS", "FLT", "ALB"),), "( AUS FLT ALB ) BLD"),
        ((Unit("ENG", "AMY", "ANK"),), "( ENG AMY ANK ) BLD"),
    ],
)
def test_BLD(input, expected_output, daide_parser):
    bld = BLD(*input)
    assert str(bld) == expected_output
    assert bld == daide_parser(expected_output)
    hash(bld)


@pytest.mark.parametrize(
    ["input", "expected_output"],
    [
        ((Unit("AUS", "FLT", "ALB"),), "( AUS FLT ALB ) REM"),
        ((Unit("ENG", "AMY", "ANK"),), "( ENG AMY ANK ) REM"),
    ],
)
def test_REM(input, expected_output, daide_parser):
    rem = REM(*input)
    assert str(rem) == expected_output
    assert rem == daide_parser(expected_output)
    hash(rem)


@pytest.mark.parametrize(
    ["input", "expected_output"],
    [
        (("AUS",), "AUS WVE"),
        (("ENG",), "ENG WVE"),
    ],
)
def test_WVE(input, expected_output, daide_parser):
    wve = WVE(*input)
    assert str(wve) == expected_output
    assert wve == daide_parser(expected_output)
    hash(wve)


@pytest.mark.parametrize(
    ["input", "expected_output"],
    [
        (("SPR", 1901), "SPR 1901"),
    ],
)
def test_turn(input, expected_output, daide_parser):
    turn_1 = Turn(*input)
    assert str(turn_1) == expected_output
    assert turn_1 == daide_parser(expected_output)
    hash(turn_1)
