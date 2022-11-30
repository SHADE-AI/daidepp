import pytest

from daidepp.keywords.press_keywords import *


def test_PCE():
    pce_1 = PCE("AUS", "ENG")
    assert str(pce_1) == "PCE ( AUS ENG )"

    pce_2 = PCE("AUS", "ENG", "FRA")
    assert str(pce_2) == "PCE ( AUS ENG FRA )"

    with pytest.raises(Exception):
        PCE("AUS")


def test_PRP():
    arr_1 = PRP(PCE("AUS", "ENG"))
    assert str(arr_1) == "PRP ( PCE ( AUS ENG ) )"

    arr_2 = PRP(PCE("AUS", "ENG", "FRA"))
    assert str(arr_2) == "PRP ( PCE ( AUS ENG FRA ) )"

    with pytest.raises(Exception):
        PRP(PCE("AUS"))


def test_CCL():
    ccl_1 = CCL(PRP(PCE("AUS", "ENG")))
    assert str(ccl_1) == "CCL ( PRP ( PCE ( AUS ENG ) ) )"

    ccl_2 = CCL(PRP(PCE("AUS", "ENG", "FRA")))
    assert str(ccl_2) == "CCL ( PRP ( PCE ( AUS ENG FRA ) ) )"

    with pytest.raises(Exception):
        CCL(PRP(PCE("AUS")))


def test_TRY():
    try_1 = TRY("PRP")
    assert str(try_1) == "TRY ( PRP )"

    try_2 = TRY("PCE", "ALY")
    assert str(try_2) == "TRY ( PCE ALY )"

    try_3 = TRY("VSS", "DRW", "SLO")
    assert str(try_3) == "TRY ( VSS DRW SLO )"


def test_HUH():

    huh_1 = HUH(PRP(PCE("AUS", "ENG")))
    assert str(huh_1) == "HUH ( PRP ( PCE ( AUS ENG ) ) )"

    huh_2 = HUH(PRP(PCE("AUS", "ENG", "FRA")))
    assert str(huh_2) == "HUH ( PRP ( PCE ( AUS ENG FRA ) ) )"

    with pytest.raises(Exception):
        HUH(PRP(PCE("AUS")))

def test_ALYVSS():
    alyvss_1 = ALYVSS(["AUS", "GER"], ["TUR", "ITA"])
    assert str(alyvss_1) == "ALY ( AUS GER ) VSS ( TUR ITA )"

    with pytest.raises(Exception):
        ALYVSS(["AUS"], ["ENG"])

    with pytest.raises(Exception):
        ALYVSS(["FRA"], ["GER", "TUR"])

    with pytest.raises(Exception):
        ALYVSS(["AUS", "FRA"], ["GER"])


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


def test_AND():
    and_1 = AND(PCE("AUS", "GER"), PCE("AUS", "ENG"))
    assert str(and_1) == "AND ( PCE ( AUS GER ) ) ( PCE ( AUS ENG ) )"

    and_2 = AND(PCE("AUS", "GER"), PCE("AUS", "ENG"), PCE("AUS", "ENG", "FRA"))
    assert (
        str(and_2)
        == "AND ( PCE ( AUS GER ) ) ( PCE ( AUS ENG ) ) ( PCE ( AUS ENG FRA ) )"
    )


def test_ORR():
    orr_1 = ORR(PCE("AUS", "GER"), PCE("AUS", "ENG"))
    assert str(orr_1) == "ORR ( PCE ( AUS GER ) ) ( PCE ( AUS ENG ) )"

    orr_2 = ORR(PCE("AUS", "GER"), PCE("AUS", "ENG"), PCE("AUS", "ENG", "FRA"))
    assert (
        str(orr_2)
        == "ORR ( PCE ( AUS GER ) ) ( PCE ( AUS ENG ) ) ( PCE ( AUS ENG FRA ) )"
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


def test_CHO():
    cho_1 = CHO(1901, 1903, PCE("AUS", "GER"), PCE("AUS", "ENG"))
    assert str(cho_1) == "CHO ( 1901 1903 ) ( PCE ( AUS GER ) ) ( PCE ( AUS ENG ) )"


def test_INS():
    ins_1 = INS(PCE("AUS", "GER"))
    assert str(ins_1) == "INS ( PCE ( AUS GER ) )"


def test_QRY():
    qry_1 = QRY(PCE("AUS", "GER"))
    assert str(qry_1) == "QRY ( PCE ( AUS GER ) )"


def test_THK():
    thk_1 = THK(PCE("AUS", "GER"))
    assert str(thk_1) == "THK ( PCE ( AUS GER ) )"


def test_IDK():
    idk_1 = IDK(PRP(PCE("AUS", "GER")))
    assert str(idk_1) == "IDK ( PRP ( PCE ( AUS GER ) ) )"


def test_SUG():
    sug_1 = SUG(PCE("AUS", "GER"))
    assert str(sug_1) == "SUG ( PCE ( AUS GER ) )"


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


def test_IFF():
    iff_1 = IFF(PCE("AUS", "ENG"), PRP(PCE("AUS", "GER")))
    assert str(iff_1) == "IFF ( PCE ( AUS ENG ) ) THN ( PRP ( PCE ( AUS GER ) ) )"

    iff_2 = IFF(PCE("AUS", "ENG"), PRP(PCE("AUS", "GER")), PRP(PCE("GER", "FRA")))
    assert (
        str(iff_2)
        == "IFF ( PCE ( AUS ENG ) ) THN ( PRP ( PCE ( AUS GER ) ) ) ELS ( PRP ( PCE ( GER FRA ) ) )"
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
