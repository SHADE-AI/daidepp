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
def test_Unit(input, expected_output):
    print(input)
    unit = Unit(*input)
    assert str(unit) == expected_output


@pytest.mark.parametrize(
    ["input", "expected_output"],
    [
        ((Unit("AUS", "FLT", "ALB"),), "( AUS FLT ALB ) HLD"),
        ((Unit("ENG", "AMY", "ANK"),), "( ENG AMY ANK ) HLD"),
    ],
)
def test_HLD(input, expected_output):
    hld = HLD(*input)
    assert str(hld) == expected_output


@pytest.mark.parametrize(
    ["input", "expected_output"],
    [
        ((Unit("AUS", "FLT", "ALB"), "BUL"), "( AUS FLT ALB ) MTO BUL"),
        ((Unit("ENG", "AMY", "ANK"), "CLY"), "( ENG AMY ANK ) MTO CLY"),
    ],
)
def test_MTO(input, expected_output):
    mto = MTO(*input)
    assert str(mto) == expected_output


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
def test_SUP(input, expected_output):
    sup = SUP(*input)
    assert str(sup) == expected_output


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
def test_SUP_location(supporting_unit, supported_unit, province_no_coast):
    sup = SUP(
        supported_unit=supported_unit,
        supporting_unit=supporting_unit,
        province_no_coast=province_no_coast,
    )
    assert isinstance(sup.province_no_coast, str)
    assert isinstance(sup.province_no_coast_location, Location)


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
def test_CVY(input, expected_output):
    cvy = CVY(*input)
    assert str(cvy) == expected_output


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
    ],
)
def test_MoveByCVY(input, expected_output):
    mvc = MoveByCVY(*input)
    assert str(mvc) == expected_output


@pytest.mark.parametrize(
    ["input", "expected_output"],
    [
        ((Unit("AUS", "FLT", "ALB"), "BUL"), "( AUS FLT ALB ) RTO BUL"),
        ((Unit("ENG", "AMY", "ANK"), "CLY"), "( ENG AMY ANK ) RTO CLY"),
    ],
)
def test_RTO(input, expected_output):
    rto = RTO(*input)
    assert str(rto) == expected_output


@pytest.mark.parametrize(
    ["input", "expected_output"],
    [
        ((Unit("AUS", "FLT", "ALB"),), "( AUS FLT ALB ) DSB"),
        ((Unit("ENG", "AMY", "ANK"),), "( ENG AMY ANK ) DSB"),
    ],
)
def test_DSB(input, expected_output):
    dsb = DSB(*input)
    assert str(dsb) == expected_output


@pytest.mark.parametrize(
    ["input", "expected_output"],
    [
        ((Unit("AUS", "FLT", "ALB"),), "( AUS FLT ALB ) BLD"),
        ((Unit("ENG", "AMY", "ANK"),), "( ENG AMY ANK ) BLD"),
    ],
)
def test_BLD(input, expected_output):
    bld = BLD(*input)
    assert str(bld) == expected_output


@pytest.mark.parametrize(
    ["input", "expected_output"],
    [
        ((Unit("AUS", "FLT", "ALB"),), "( AUS FLT ALB ) REM"),
        ((Unit("ENG", "AMY", "ANK"),), "( ENG AMY ANK ) REM"),
    ],
)
def test_REM(input, expected_output):
    rem = REM(*input)
    assert str(rem) == expected_output


@pytest.mark.parametrize(
    ["input", "expected_output"],
    [
        (("AUS",), "AUS WVE"),
        (("ENG",), "ENG WVE"),
    ],
)
def test_WVE(input, expected_output):
    wve = WVE(*input)
    assert str(wve) == expected_output


@pytest.mark.parametrize(
    ["input", "expected_output"],
    [
        (("SPR", 1901), "SPR 1901"),
    ],
)
def test_turn(input, expected_output):
    turn_1 = Turn(*input)
    assert str(turn_1) == expected_output
