from daidepp.keywords.base_keywords import *


def test_Unit():
    unit_1 = Unit("AUS", "FLT", "ALB")
    assert str(unit_1) == "AUS FLT ALB"

    unit_2 = Unit("ENG", "AMY", "ANK")
    assert str(unit_2) == "ENG AMY ANK"

    unit_3 = Unit("FRA", "FLT", "APU")
    assert str(unit_3) == "FRA FLT APU"

    unit_4 = Unit("GER", "AMY", "ARM")
    assert str(unit_4) == "GER AMY ARM"

    unit_5 = Unit("ITA", "FLT", "BEL")
    assert str(unit_5) == "ITA FLT BEL"

    unit_6 = Unit("RUS", "AMY", "BER")
    assert str(unit_6) == "RUS AMY BER"

    unit_7 = Unit("TUR", "FLT", "BRE")
    assert str(unit_7) == "TUR FLT BRE"


def test_HLD():
    hld_1 = HLD(Unit("AUS", "FLT", "ALB"))
    assert str(hld_1) == "( AUS FLT ALB ) HLD"

    hld_2 = HLD(Unit("ENG", "AMY", "ANK"))
    assert str(hld_2) == "( ENG AMY ANK ) HLD"


def test_MTO():
    mto_1 = MTO(Unit("AUS", "FLT", "ALB"), "BUL")
    assert str(mto_1) == "( AUS FLT ALB ) MTO BUL"

    mto_2 = MTO(Unit("ENG", "AMY", "ANK"), "CLY")
    assert str(mto_2) == "( ENG AMY ANK ) MTO CLY"


def test_SUP():
    sup_1 = SUP(Unit("AUS", "FLT", "ALB"), Unit("ENG", "AMY", "ANK"), "BUL")
    assert str(sup_1) == "( AUS FLT ALB ) SUP ( ENG AMY ANK ) MTO BUL"

    sup_2 = SUP(Unit("FRA", "FLT", "APU"), Unit("GER", "AMY", "ARM"), "CLY")
    assert str(sup_2) == "( FRA FLT APU ) SUP ( GER AMY ARM ) MTO CLY"


def test_CVY():
    cvy_1 = CVY(Unit("AUS", "FLT", "ALB"), Unit("ENG", "AMY", "ANK"), "BUL")
    assert str(cvy_1) == "( AUS FLT ALB ) CVY ( ENG AMY ANK ) CTO BUL"

    cvy_2 = CVY(Unit("FRA", "FLT", "APU"), Unit("GER", "AMY", "ARM"), "CLY")
    assert str(cvy_2) == "( FRA FLT APU ) CVY ( GER AMY ARM ) CTO CLY"


def test_MoveByCVY():
    mvc_1 = MoveByCVY(Unit("AUS", "FLT", "ALB"), "BUL", "ADR")
    assert str(mvc_1) == "( AUS FLT ALB ) CTO BUL VIA ( ADR )"

    mvc_2 = MoveByCVY(Unit("ENG", "AMY", "ANK"), "CLY", "ADR", "AEG")
    assert str(mvc_2) == "( ENG AMY ANK ) CTO CLY VIA ( ADR AEG )"

    mvc_3 = MoveByCVY(Unit("FRA", "FLT", "APU"), "CON", "ADR", "AEG", "BAL")
    assert str(mvc_3) == "( FRA FLT APU ) CTO CON VIA ( ADR AEG BAL )"


def test_RTO():
    rto_1 = RTO(Unit("AUS", "FLT", "ALB"), "BUL")
    assert str(rto_1) == "( AUS FLT ALB ) RTO BUL"

    rto_2 = RTO(Unit("ENG", "AMY", "ANK"), "CLY")
    assert str(rto_2) == "( ENG AMY ANK ) RTO CLY"


def test_DSB():
    dsb_1 = DSB(Unit("AUS", "FLT", "ALB"))
    assert str(dsb_1) == "( AUS FLT ALB ) DSB"

    dsb_2 = DSB(Unit("ENG", "AMY", "ANK"))
    assert str(dsb_2) == "( ENG AMY ANK ) DSB"


def test_BLD():
    bld_1 = BLD(Unit("AUS", "FLT", "ALB"))
    assert str(bld_1) == "( AUS FLT ALB ) BLD"

    bld_2 = BLD(Unit("ENG", "AMY", "ANK"))
    assert str(bld_2) == "( ENG AMY ANK ) BLD"


def test_REM():
    rem_1 = REM(Unit("AUS", "FLT", "ALB"))
    assert str(rem_1) == "( AUS FLT ALB ) REM"

    rem_2 = REM(Unit("ENG", "AMY", "ANK"))
    assert str(rem_2) == "( ENG AMY ANK ) REM"


def test_WVE():
    wve_1 = WVE("AUS")
    assert str(wve_1) == "AUS WVE"

    wve_2 = WVE("ENG")
    assert str(wve_2) == "ENG WVE"


def test_turn():
    turn_1 = Turn("SPR", 1901)
    assert str(turn_1) == "SPR 1901"
