import pytest

from daidepp.keywords import *


def test_Unit():
    loc_1 = Location("ALB")
    unit_1 = Unit("AUS", "FLT", loc_1)
    assert str(unit_1) == "AUS FLT ALB"

    loc_2 = Location("ANK")
    unit_2 = Unit("ENG", "AMY", loc_2)
    assert str(unit_2) == "ENG AMY ANK"

    loc_3 = Location("APU")
    unit_3 = Unit("FRA", "FLT", loc_3)
    assert str(unit_3) == "FRA FLT APU"

    loc_4 = Location("ARM")
    unit_4 = Unit("GER", "AMY", loc_4)
    assert str(unit_4) == "GER AMY ARM"

    loc_5 = Location("BEL")
    unit_5 = Unit("ITA", "FLT", loc_5)
    assert str(unit_5) == "ITA FLT BEL"

    loc_6 = Location("BER")
    unit_6 = Unit("RUS", "AMY", loc_6)
    assert str(unit_6) == "RUS AMY BER"

    loc_7 = Location("BRE")
    unit_7 = Unit("TUR", "FLT", loc_7)
    assert str(unit_7) == "TUR FLT BRE"


def test_HLD():
    loc_1 = Location("ALB")
    hld_1 = HLD(Unit("AUS", "FLT", loc_1))
    assert str(hld_1) == "( AUS FLT ALB ) HLD"

    loc_2 = Location("ANK")
    hld_2 = HLD(Unit("ENG", "AMY", loc_2))
    assert str(hld_2) == "( ENG AMY ANK ) HLD"


def test_MTO():
    unit_1_loc = Location("ALB")
    destination_1 = Location("BUL")
    mto_1 = MTO(Unit("AUS", "FLT", unit_1_loc), destination_1)
    assert str(mto_1) == "( AUS FLT ALB ) MTO BUL"

    unit_2_loc = Location("ANK")
    destination_2 = Location("CLY")
    mto_2 = MTO(Unit("ENG", "AMY", unit_2_loc), destination_2)
    assert str(mto_2) == "( ENG AMY ANK ) MTO CLY"


def test_SUP():
    unit_11_loc = Location("ALB")
    unit_12_loc = Location("ANK")
    destination_1 = Location("BUL")
    sup_1 = SUP(
        Unit("AUS", "FLT", unit_11_loc), Unit("ENG", "AMY", unit_12_loc), destination_1
    )
    assert str(sup_1) == "( AUS FLT ALB ) SUP ( ENG AMY ANK ) MTO BUL"

    unit_21_loc = Location("APU")
    unit_22_loc = Location("ARM")
    destination_2 = Location("CLY")
    sup_2 = SUP(
        Unit("FRA", "FLT", unit_21_loc), Unit("GER", "AMY", unit_22_loc), destination_2
    )
    assert str(sup_2) == "( FRA FLT APU ) SUP ( GER AMY ARM ) MTO CLY"


def test_CVY():
    loc_11 = Location("ALB")
    loc_12 = Location("ANK")
    loc_13 = Location("BUL")
    cvy_1 = CVY(Unit("AUS", "FLT", loc_11), Unit("ENG", "AMY", loc_12), loc_13)
    assert str(cvy_1) == "( AUS FLT ALB ) CVY ( ENG AMY ANK ) CTO BUL"

    loc_21 = Location("APU")
    loc_22 = Location("ARM")
    loc_23 = Location("CLY")
    cvy_2 = CVY(Unit("FRA", "FLT", loc_21), Unit("GER", "AMY", loc_22), loc_23)
    assert str(cvy_2) == "( FRA FLT APU ) CVY ( GER AMY ARM ) CTO CLY"


def test_MoveByCVY():
    loc_11 = Location("ALB")
    loc_12 = Location("BUL")
    loc_13 = Location("ADR")
    mvc_1 = MoveByCVY(Unit("AUS", "FLT", loc_11), loc_12, loc_13)
    assert str(mvc_1) == "( AUS FLT ALB ) CTO BUL VIA ( ADR )"

    loc_21 = Location("ANK")
    loc_22 = Location("CLY")
    loc_23 = Location("ADR")
    loc_24 = Location("AEG")
    mvc_2 = MoveByCVY(Unit("ENG", "AMY", loc_21), loc_22, loc_23, loc_24)
    assert str(mvc_2) == "( ENG AMY ANK ) CTO CLY VIA ( ADR AEG )"

    loc_21 = Location("APU")
    loc_22 = Location("CON")
    loc_23 = Location("ADR")
    loc_24 = Location("AEG")
    loc_25 = Location("BAL")
    mvc_3 = MoveByCVY(Unit("FRA", "FLT", loc_21), loc_22, loc_23, loc_24, loc_25)
    assert str(mvc_3) == "( FRA FLT APU ) CTO CON VIA ( ADR AEG BAL )"


def test_RTO():
    loc_11 = Location("ALB")
    loc_12 = Location("BUL")
    rto_1 = RTO(Unit("AUS", "FLT", loc_11), loc_12)
    assert str(rto_1) == "( AUS FLT ALB ) RTO BUL"

    loc_21 = Location("ANK")
    loc_22 = Location("CLY")
    rto_2 = RTO(Unit("ENG", "AMY", loc_21), loc_22)
    assert str(rto_2) == "( ENG AMY ANK ) RTO CLY"


def test_DSB():
    loc_1 = Location("ALB")
    dsb_1 = DSB(Unit("AUS", "FLT", loc_1))
    assert str(dsb_1) == "( AUS FLT ALB ) DSB"

    loc_2 = Location("ANK")
    dsb_2 = DSB(Unit("ENG", "AMY", loc_2))
    assert str(dsb_2) == "( ENG AMY ANK ) DSB"


def test_BLD():
    loc_1 = Location("ALB")
    bld_1 = BLD(Unit("AUS", "FLT", loc_1))
    assert str(bld_1) == "( AUS FLT ALB ) BLD"

    loc_2 = Location("ANK")
    bld_2 = BLD(Unit("ENG", "AMY", loc_2))
    assert str(bld_2) == "( ENG AMY ANK ) BLD"


def test_REM():
    loc_1 = Location("ALB")
    rem_1 = REM(Unit("AUS", "FLT", loc_1))
    assert str(rem_1) == "( AUS FLT ALB ) REM"

    loc_2 = Location("ANK")
    rem_2 = REM(Unit("ENG", "AMY", loc_2))
    assert str(rem_2) == "( ENG AMY ANK ) REM"


def test_WVE():

    wve_1 = WVE("AUS")
    assert str(wve_1) == "AUS WVE"

    wve_2 = WVE("ENG")
    assert str(wve_2) == "ENG WVE"


def test_turn():
    turn_1 = Turn("SPR", 1901)
    assert str(turn_1) == "SPR 1901"


def test_PCE():
    # pce_1 = PCE("AUS")
    # assert str(pce_1) == "PCE ( AUS )"

    pce_2 = PCE("AUS", "ENG")
    assert str(pce_2) == "PCE ( AUS ENG )"

    pce_3 = PCE("AUS", "ENG", "FRA")
    assert str(pce_3) == "PCE ( AUS ENG FRA )"


def test_PRP():
    # arr_1 = PRP(PCE("AUS"))
    # assert str(arr_1) == "PRP ( PCE ( AUS ) )"

    arr_2 = PRP(PCE("AUS", "ENG"))
    assert str(arr_2) == "PRP ( PCE ( AUS ENG ) )"

    arr_2 = PRP(PCE("AUS", "ENG", "FRA"))
    assert str(arr_2) == "PRP ( PCE ( AUS ENG FRA ) )"


def test_CCL():
    # ccl_1 = CCL(PRP(PCE("AUS")))
    # assert str(ccl_1) == "CCL ( PRP ( PCE ( AUS ) ) )"

    ccl_2 = CCL(PRP(PCE("AUS", "ENG")))
    assert str(ccl_2) == "CCL ( PRP ( PCE ( AUS ENG ) ) )"

    ccl_3 = CCL(PRP(PCE("AUS", "ENG", "FRA")))
    assert str(ccl_3) == "CCL ( PRP ( PCE ( AUS ENG FRA ) ) )"


def test_TRY():
    try_1 = TRY("PRP")
    assert str(try_1) == "TRY ( PRP )"

    try_2 = TRY("PCE", "ALY")
    assert str(try_2) == "TRY ( PCE ALY )"

    try_3 = TRY("VSS", "DRW", "SLO")
    assert str(try_3) == "TRY ( VSS DRW SLO )"


def test_HUH():
    # huh_1 = HUH(PRP(PCE("AUS")))
    # assert str(huh_1) == "HUH ( PRP ( PCE ( AUS ) ) )"

    huh_2 = HUH(PRP(PCE("AUS", "ENG")))
    assert str(huh_2) == "HUH ( PRP ( PCE ( AUS ENG ) ) )"

    huh_3 = HUH(PRP(PCE("AUS", "ENG", "FRA")))
    assert str(huh_3) == "HUH ( PRP ( PCE ( AUS ENG FRA ) ) )"


def test_ALYVSS():

    # This shouldn't work
    alyvss_1 = ALYVSS(["AUS"], ["ENG"])
    assert str(alyvss_1) == "ALY ( AUS ) VSS ( ENG )"

    alyvss_2 = ALYVSS(["FRA"], ["GER", "TUR"])
    assert str(alyvss_2) == "ALY ( FRA ) VSS ( GER TUR )"

    alyvss_3 = ALYVSS(["AUS", "FRA"], ["GER"])
    assert str(alyvss_3) == "ALY ( AUS FRA ) VSS ( GER )"

    alyvss_4 = ALYVSS(["AUS", "GER"], ["TUR", "ITA"])
    assert str(alyvss_4) == "ALY ( AUS GER ) VSS ( TUR ITA )"


def test_SLO():
    slo_1 = SLO("AUS")
    assert str(slo_1) == "SLO ( AUS )"

    slo_2 = SLO("GER")
    assert str(slo_2) == "SLO ( GER )"


def test_NOT():
    not_1 = NOT(PCE("AUS", "ENG"))
    assert str(not_1) == "NOT ( PCE ( AUS ENG ) )"


def test_NAR():
    nar_1 = NAR(PCE("AUS", "ENG"))
    assert str(nar_1) == "NAR ( PCE ( AUS ENG ) )"


def test_DRW():
    drw_1 = DRW()
    assert str(drw_1) == "DRW"

    drw_2 = DRW("AUS", "ENG")
    assert str(drw_2) == "DRW ( AUS ENG )"


def test_YES():
    yes_1 = YES(PRP(PCE("AUS", "ENG")))
    assert str(yes_1) == "YES ( PRP ( PCE ( AUS ENG ) ) )"


def test_REJ():
    rej_1 = REJ(PRP(PCE("AUS", "ENG")))
    assert str(rej_1) == "REJ ( PRP ( PCE ( AUS ENG ) ) )"


def test_BWX():
    bwx_1 = BWX(PRP(PCE("AUS", "ENG")))
    assert str(bwx_1) == "BWX ( PRP ( PCE ( AUS ENG ) ) )"


def test_FCT():
    fct_1 = FCT(PCE("AUS", "ENG"))
    assert str(fct_1) == "FCT ( PCE ( AUS ENG ) )"

    fct_2 = FCT(NOT(PCE("AUS", "ENG")))
    assert str(fct_2) == "FCT ( NOT ( PCE ( AUS ENG ) ) )"


def test_FRM():
    frm_1 = FRM("AUS", ["GER", "FRA"], PRP(PCE("AUS", "ENG")))

    assert str(frm_1) == "FRM ( AUS ) ( GER FRA ) ( PRP ( PCE ( AUS ENG ) ) )"


def test_XDO():
    loc_1 = Location("ALB")
    xdo_1 = XDO(HLD(Unit("AUS", "FLT", loc_1)))
    assert str(xdo_1) == "XDO ( ( AUS FLT ALB ) HLD )"

    loc_21 = Location("ALB")
    loc_22 = Location("BUL")
    xdo_2 = XDO(MTO(Unit("AUS", "FLT", loc_21), loc_22))
    assert str(xdo_2) == "XDO ( ( AUS FLT ALB ) MTO BUL )"


def test_DMZ():

    loc_1 = Location("EDI")
    dmz_1 = DMZ(["AUS"], [loc_1])
    assert str(dmz_1) == "DMZ ( AUS ) ( EDI )"

    loc_21 = Location("CLY")
    loc_22 = Location("ALB")
    dmz_2 = DMZ(["ITA", "TUR"], [loc_21, loc_22])
    assert str(dmz_2) == "DMZ ( ITA TUR ) ( CLY ALB )"


@pytest.mark.xfail
def test_AND():

    # Both of these should fail because you can't have peace with only one power

    and_1 = AND(PRP(PCE("AUS")), PRP(PCE("AUS", "ENG")))
    assert str(and_1) == "AND ( PRP ( PCE ( AUS ) ) ) ( PRP ( PCE ( AUS ENG ) ) )"

    and_2 = AND(PRP(PCE("AUS")), PRP(PCE("AUS", "ENG")), PRP(PCE("AUS", "ENG", "FRA")))
    assert (
        str(and_2)
        == "AND ( PRP ( PCE ( AUS ) ) ) ( PRP ( PCE ( AUS ENG ) ) ) ( PRP ( PCE ( AUS ENG FRA ) ) )"
    )


@pytest.mark.xfail
def test_ORR():

    # Both of these should fail because you can't have peace with one power

    orr_1 = ORR(PRP(PCE("AUS")), PRP(PCE("AUS", "ENG")))
    assert str(orr_1) == "ORR ( PRP ( PCE ( AUS ) ) ) ( PRP ( PCE ( AUS ENG ) ) )"

    orr_2 = ORR(PRP(PCE("AUS")), PRP(PCE("AUS", "ENG")), PRP(PCE("AUS", "ENG", "FRA")))
    assert (
        str(orr_2)
        == "ORR ( PRP ( PCE ( AUS ) ) ) ( PRP ( PCE ( AUS ENG ) ) ) ( PRP ( PCE ( AUS ENG FRA ) ) )"
    )


def test_SCD():
    loc_11 = Location("ANK")
    loc_12 = Location("BEL")
    loc_13 = Location("BER")
    loc_14 = Location("BRE")
    loc_15 = Location("BUD")
    scd_1 = SCD(
        PowerAndSupplyCenters("AUS", loc_11, loc_12, loc_13),
        PowerAndSupplyCenters("GER", loc_14, loc_15),
    )
    assert str(scd_1) == "SCD ( AUS ANK BEL BER ) ( GER BRE BUD )"


def test_OCC():
    loc_11 = Location("ALB")
    loc_12 = Location("ANK")
    loc_13 = Location("APU")
    unit_1 = Unit("AUS", "FLT", loc_11)
    unit_2 = Unit("ENG", "AMY", loc_12)
    unit_3 = Unit("FRA", "FLT", loc_13)

    occ_1 = OCC(unit_1, unit_2, unit_3)
    assert str(occ_1) == "OCC ( AUS FLT ALB ) ( ENG AMY ANK ) ( FRA FLT APU )"


@pytest.mark.xfail
def test_CHO():
    cho_1 = CHO(1901, 1903, PCE("AUS"), PCE("AUS", "ENG"))
    assert str(cho_1) == "CHO ( 1901 1903 ) ( PCE ( AUS ) ) ( PCE ( AUS ENG ) )"


@pytest.mark.xfail
def test_INS():
    ins_1 = INS(PCE("AUS"))
    assert str(ins_1) == "INS ( PCE ( AUS ) )"


@pytest.mark.xfail
def test_QRY():
    qry_1 = QRY(PCE("AUS"))
    assert str(qry_1) == "QRY ( PCE ( AUS ) )"


@pytest.mark.xfail
def test_THK():
    thk_1 = THK(PCE("AUS"))
    assert str(thk_1) == "THK ( PCE ( AUS ) )"


@pytest.mark.xfail
def test_IDK():
    idk_1 = IDK(PRP(PCE("AUS")))
    assert str(idk_1) == "IDK ( PRP ( PCE ( AUS ) ) )"


@pytest.mark.xfail
def test_SUG():
    sug_1 = SUG(PCE("AUS"))
    assert str(sug_1) == "SUG ( PCE ( AUS ) )"


def test_WHT():
    loc_1 = Location("ALB")
    wht_1 = WHT(Unit("AUS", "FLT", loc_1))

    assert str(wht_1) == "WHT ( AUS FLT ALB )"


def test_HOW():
    how_1 = HOW("AUS")
    assert str(how_1) == "HOW ( AUS )"

    loc_2 = Location("APU")
    how_2 = HOW(loc_2)
    assert str(how_2) == "HOW ( APU )"


def test_EXP():
    exp_1 = EXP(Turn("SPR", 1901), PRP(PCE("AUS", "ENG")))

    assert str(exp_1) == "EXP ( SPR 1901 ) ( PRP ( PCE ( AUS ENG ) ) )"


def test_SRY():
    sry_1 = SRY(EXP(Turn("SPR", 1901), PRP(PCE("AUS", "ENG"))))

    assert str(sry_1) == "SRY ( EXP ( SPR 1901 ) ( PRP ( PCE ( AUS ENG ) ) ) )"


def test_FOR():
    for_1 = FOR(Turn("SPR", 1901), None, PCE("AUS", "ENG"))
    assert str(for_1) == "FOR ( SPR 1901 ) ( PCE ( AUS ENG ) )"

    for_2 = FOR(Turn("SPR", 1901), Turn("FAL", 1903), PCE("AUS", "ENG"))
    assert str(for_2) == "FOR ( ( SPR 1901 ) ( FAL 1903 ) ) ( PCE ( AUS ENG ) )"


@pytest.mark.xfail
def test_IFF():
    iff_1 = IFF(PCE("AUS", "ENG"), PRP(PCE("AUS")))
    assert str(iff_1) == "IFF ( PCE ( AUS ENG ) ) THN ( PRP ( PCE ( AUS ) ) )"

    iff_2 = IFF(PCE("AUS", "ENG"), PRP(PCE("AUS")), PRP(PCE("GER", "FRA")))
    assert (
        str(iff_2)
        == "IFF ( PCE ( AUS ENG ) ) THN ( PRP ( PCE ( AUS ) ) ) ELS ( PRP ( PCE ( GER FRA ) ) )"
    )


def test_XOY():
    xoy_1 = XOY("AUS", "ENG")
    assert str(xoy_1) == "XOY ( AUS ) ( ENG )"


def test_YDO():
    loc_1 = Location("ALB")
    ydo_1 = YDO("AUS", Unit("AUS", "FLT", loc_1))
    assert str(ydo_1) == "YDO ( AUS ) ( AUS FLT ALB )"

    loc_21 = Location("ALB")
    loc_22 = Location("ANK")
    ydo_2 = YDO("AUS", Unit("AUS", "FLT", loc_21), Unit("ENG", "AMY", loc_22))
    assert str(ydo_2) == "YDO ( AUS ) ( AUS FLT ALB ) ( ENG AMY ANK )"


def test_SND():
    snd_1 = SND("AUS", ["GER", "FRA"], PRP(PCE("TUR", "RUS")))
    assert str(snd_1) == "SND ( AUS ) ( GER FRA ) ( PRP ( PCE ( TUR RUS ) ) )"


def test_FWD():
    fwd_1 = FWD(["GER", "ITA"], "FRA", "AUS")
    assert str(fwd_1) == "FWD ( GER ITA ) ( FRA ) ( AUS )"


def test_BCC():
    bcc_1 = BCC("AUS", ["GER", "FRA"], "ITA")
    assert str(bcc_1) == "BCC ( AUS ) ( GER FRA ) ( ITA )"


def test_WHY():
    why_1 = WHY(PRP(PCE("AUS", "GER")))
    assert str(why_1) == "WHY ( PRP ( PCE ( AUS GER ) ) )"


def test_POB():
    pob_1 = POB(WHY(PRP(PCE("AUS", "GER"))))
    assert str(pob_1) == "POB ( WHY ( PRP ( PCE ( AUS GER ) ) ) )"
