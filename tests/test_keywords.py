from typing import List

from daidepp.keywords import *


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
    assert str(hld_1) == "(AUS FLT ALB) HLD"

    hld_2 = HLD(Unit("ENG", "AMY", "ANK"))
    assert str(hld_2) == "(ENG AMY ANK) HLD"


def test_MTO():
    mto_1 = MTO(Unit("AUS", "FLT", "ALB"), "BUL")
    assert str(mto_1) == "(AUS FLT ALB) MTO BUL"

    mto_2 = MTO(Unit("ENG", "AMY", "ANK"), "CLY")
    assert str(mto_2) == "(ENG AMY ANK) MTO CLY"


def test_SUP():
    sup_1 = SUP(Unit("AUS", "FLT", "ALB"), Unit("ENG", "AMY", "ANK"), "BUL")
    assert str(sup_1) == "(AUS FLT ALB) SUP (ENG AMY ANK) MTO BUL"

    sup_2 = SUP(Unit("FRA", "FLT", "APU"), Unit("GER", "AMY", "ARM"), "CLY")
    assert str(sup_2) == "(FRA FLT APU) SUP (GER AMY ARM) MTO CLY"


def test_CVY():
    cvy_1 = CVY(Unit("AUS", "FLT", "ALB"), Unit("ENG", "AMY", "ANK"), "BUL")
    assert str(cvy_1) == "(AUS FLT ALB) CVY (ENG AMY ANK) CTO BUL"

    cvy_2 = CVY(Unit("FRA", "FLT", "APU"), Unit("GER", "AMY", "ARM"), "CLY")
    assert str(cvy_2) == "(FRA FLT APU) CVY (GER AMY ARM) CTO CLY"


def test_MoveByCVY():
    mvc_1 = MoveByCVY(Unit("AUS", "FLT", "ALB"), "BUL", "ADR")
    assert str(mvc_1) == "(AUS FLT ALB) CTO BUL VIA (ADR)"

    mvc_2 = MoveByCVY(Unit("ENG", "AMY", "ANK"), "CLY", "ADR", "AEG")
    assert str(mvc_2) == "(ENG AMY ANK) CTO CLY VIA (ADR AEG)"

    mvc_3 = MoveByCVY(Unit("FRA", "FLT", "APU"), "CON", "ADR", "AEG", "BAL")
    assert str(mvc_3) == "(FRA FLT APU) CTO CON VIA (ADR AEG BAL)"


def test_RTO():
    rto_1 = RTO(Unit("AUS", "FLT", "ALB"), "BUL")
    assert str(rto_1) == "(AUS FLT ALB) RTO BUL"

    rto_2 = RTO(Unit("ENG", "AMY", "ANK"), "CLY")
    assert str(rto_2) == "(ENG AMY ANK) RTO CLY"


def test_DSB():
    dsb_1 = DSB(Unit("AUS", "FLT", "ALB"))
    assert str(dsb_1) == "(AUS FLT ALB) DSB"

    dsb_2 = DSB(Unit("ENG", "AMY", "ANK"))
    assert str(dsb_2) == "(ENG AMY ANK) DSB"


def test_BLD():
    bld_1 = BLD(Unit("AUS", "FLT", "ALB"))
    assert str(bld_1) == "(AUS FLT ALB) BLD"

    bld_2 = BLD(Unit("ENG", "AMY", "ANK"))
    assert str(bld_2) == "(ENG AMY ANK) BLD"


def test_REM():
    rem_1 = REM(Unit("AUS", "FLT", "ALB"))
    assert str(rem_1) == "(AUS FLT ALB) REM"

    rem_2 = REM(Unit("ENG", "AMY", "ANK"))
    assert str(rem_2) == "(ENG AMY ANK) REM"


def test_WVE():
    wve_1 = WVE("AUS")
    assert str(wve_1) == "AUS WVE"

    wve_2 = WVE("ENG")
    assert str(wve_2) == "ENG WVE"


def test_turn():
    turn_1 = Turn("SPR", 1901)
    assert str(turn_1) == "SPR 1901"


def test_PCE():
    pce_1 = PCE("AUS")
    assert str(pce_1) == "PCE (AUS)"

    pce_2 = PCE("AUS", "ENG")
    assert str(pce_2) == "PCE (AUS ENG)"

    pce_3 = PCE("AUS", "ENG", "FRA")
    assert str(pce_3) == "PCE (AUS ENG FRA)"


def test_PRP():
    arr_1 = PRP(PCE("AUS"))
    assert str(arr_1) == "PRP (PCE (AUS))"

    arr_2 = PRP(PCE("AUS", "ENG"))
    assert str(arr_2) == "PRP (PCE (AUS ENG))"

    arr_2 = PRP(PCE("AUS", "ENG", "FRA"))
    assert str(arr_2) == "PRP (PCE (AUS ENG FRA))"


def test_CCL():
    ccl_1 = CCL(PRP(PCE("AUS")))
    assert str(ccl_1) == "CCL (PRP (PCE (AUS)))"

    ccl_2 = CCL(PRP(PCE("AUS", "ENG")))
    assert str(ccl_2) == "CCL (PRP (PCE (AUS ENG)))"

    ccl_3 = CCL(PRP(PCE("AUS", "ENG", "FRA")))
    assert str(ccl_3) == "CCL (PRP (PCE (AUS ENG FRA)))"


def test_TRY():
    try_1 = TRY("PRP")
    assert str(try_1) == "TRY (PRP)"

    try_2 = TRY("PCE", "ALY")
    assert str(try_2) == "TRY (PCE ALY)"

    try_3 = TRY("VSS", "DRW", "SLO")
    assert str(try_3) == "TRY (VSS DRW SLO)"


def test_HUH():
    huh_1 = HUH(PRP(PCE("AUS")))
    assert str(huh_1) == "HUH (PRP (PCE (AUS)))"

    huh_2 = HUH(PRP(PCE("AUS", "ENG")))
    assert str(huh_2) == "HUH (PRP (PCE (AUS ENG)))"

    huh_3 = HUH(PRP(PCE("AUS", "ENG", "FRA")))
    assert str(huh_3) == "HUH (PRP (PCE (AUS ENG FRA)))"


def test_ALYVSS():
    alyvss_1 = ALYVSS(["AUS"], ["ENG"])
    assert str(alyvss_1) == "ALY (AUS) VSS (ENG)"

    alyvss_2 = ALYVSS(["FRA"], ["GER", "TUR"])
    assert str(alyvss_2) == "ALY (FRA) VSS (GER TUR)"

    alyvss_3 = ALYVSS(["AUS", "FRA"], ["GER"])
    assert str(alyvss_3) == "ALY (AUS FRA) VSS (GER)"

    alyvss_4 = ALYVSS(["AUS", "GER"], ["TUR", "ITA"])
    assert str(alyvss_4) == "ALY (AUS GER) VSS (TUR ITA)"


def test_SLO():
    slo_1 = SLO("AUS")
    assert str(slo_1) == "SLO (AUS)"

    slo_2 = SLO("GER")
    assert str(slo_2) == "SLO (GER)"


def test_NOT():
    not_1 = NOT(PCE("AUS", "ENG"))
    assert str(not_1) == "NOT (PCE (AUS ENG))"


def test_NAR():
    nar_1 = NAR(PCE("AUS", "ENG"))
    assert str(nar_1) == "NAR (PCE (AUS ENG))"


def test_DRW():
    drw_1 = DRW()
    assert str(drw_1) == "DRW"

    drw_2 = DRW("AUS", "ENG")
    assert str(drw_2) == "DRW (AUS ENG)"


def test_YES():
    yes_1 = YES(PRP(PCE("AUS", "ENG")))
    assert str(yes_1) == "YES (PRP (PCE (AUS ENG)))"


def test_REJ():
    rej_1 = REJ(PRP(PCE("AUS", "ENG")))
    assert str(rej_1) == "REJ (PRP (PCE (AUS ENG)))"


def test_BWX():
    bwx_1 = BWX(PRP(PCE("AUS", "ENG")))
    assert str(bwx_1) == "BWX (PRP (PCE (AUS ENG)))"


def test_FCT():
    fct_1 = FCT(PCE("AUS", "ENG"))
    assert str(fct_1) == "FCT (PCE (AUS ENG))"

    fct_2 = FCT(NOT(PCE("AUS", "ENG")))
    assert str(fct_2) == "FCT (NOT (PCE (AUS ENG)))"


def test_FRM():
    frm_1 = FRM("AUS", ["GER", "FRA"], PRP(PCE("AUS", "ENG")))

    assert str(frm_1) == "FRM (AUS) (GER FRA) (PRP (PCE (AUS ENG)))"


def test_XDO():
    xdo_1 = XDO(HLD(Unit("AUS", "FLT", "ALB")))
    assert str(xdo_1) == "XDO ((AUS FLT ALB) HLD)"

    xdo_2 = XDO(MTO(Unit("AUS", "FLT", "ALB"), "BUL"))
    assert str(xdo_2) == "XDO ((AUS FLT ALB) MTO BUL)"


def test_DMZ():
    dmz_1 = DMZ(["AUS"], ["EDI"])
    assert str(dmz_1) == "DMZ (AUS) (EDI)"

    dmz_2 = DMZ(["ITA", "TUR"], ["CLY", "ALB"])
    assert str(dmz_2) == "DMZ (ITA TUR) (CLY ALB)"


def test_AND():
    and_1 = AND(PRP(PCE("AUS")), PRP(PCE("AUS", "ENG")))
    assert str(and_1) == "AND ((PRP (PCE (AUS))) (PRP (PCE (AUS ENG))))"

    and_2 = AND(PRP(PCE("AUS")), PRP(PCE("AUS", "ENG")), PRP(PCE("AUS", "ENG", "FRA")))
    assert (
        str(and_2)
        == "AND ((PRP (PCE (AUS))) (PRP (PCE (AUS ENG))) (PRP (PCE (AUS ENG FRA))))"
    )


def test_ORR():
    orr_1 = ORR(PRP(PCE("AUS")), PRP(PCE("AUS", "ENG")))
    assert str(orr_1) == "ORR ((PRP (PCE (AUS))) (PRP (PCE (AUS ENG))))"

    orr_2 = ORR(PRP(PCE("AUS")), PRP(PCE("AUS", "ENG")), PRP(PCE("AUS", "ENG", "FRA")))
    assert (
        str(orr_2)
        == "ORR ((PRP (PCE (AUS))) (PRP (PCE (AUS ENG))) (PRP (PCE (AUS ENG FRA))))"
    )


def test_SCD():
    scd_1 = SCD("AUS", "ANK", "BEL", "BER")
    assert str(scd_1) == "SCD (AUS ANK BEL BER)"

    scd_2 = SCD("GER", "BRE", "BUD")
    assert str(scd_2) == "SCD (GER BRE BUD)"


def test_OCC():
    unit_1 = Unit("AUS", "FLT", "ALB")
    unit_2 = Unit("ENG", "AMY", "ANK")
    unit_3 = Unit("FRA", "FLT", "APU")

    occ_1 = OCC(unit_1, unit_2, unit_3)
    assert str(occ_1) == "OCC ((AUS FLT ALB) (ENG AMY ANK) (FRA FLT APU))"


def test_CHO():
    cho_1 = CHO(1901, 1903, PCE("AUS"), PCE("AUS", "ENG"))
    assert str(cho_1) == "CHO (1901 1903) (PCE (AUS)) (PCE (AUS ENG))"


def test_INS():
    ins_1 = INS(PCE("AUS"))
    assert str(ins_1) == "INS (PCE (AUS))"


def test_QRY():
    qry_1 = QRY(PCE("AUS"))
    assert str(qry_1) == "QRY (PCE (AUS))"


def test_THK():
    thk_1 = THK(PCE("AUS"))
    assert str(thk_1) == "THK (PCE (AUS))"


def test_SUG():
    sug_1 = SUG(PCE("AUS"))
    assert str(sug_1) == "SUG (PCE (AUS))"


def test_WHT():
    wht_1 = WHT(Unit("AUS", "FLT", "ALB"))

    assert str(wht_1) == "WHT (AUS FLT ALB)"


def test_HOW():
    how_1 = HOW("AUS")
    assert str(how_1) == "HOW (AUS)"

    how_2 = HOW("APU")
    assert str(how_2) == "HOW (APU)"


def test_EXP():
    exp_1 = EXP(Turn("SPR", 1901), PRP(PCE("AUS", "ENG")))

    assert str(exp_1) == "EXP (SPR 1901) (PRP (PCE (AUS ENG)))"


def test_SRY():
    sry_1 = SRY(EXP(Turn("SPR", 1901), PRP(PCE("AUS", "ENG"))))

    assert str(sry_1) == "SRY (EXP (SPR 1901) (PRP (PCE (AUS ENG))))"


def test_FOR():
    for_1 = FOR(Turn("SPR", 1901), None, PCE("AUS", "ENG"))
    assert str(for_1) == "FOR (SPR 1901) (PCE (AUS ENG))"

    for_2 = FOR(Turn("SPR", 1901), Turn("FAL", 1903), PCE("AUS", "ENG"))
    assert str(for_2) == "FOR ((SPR 1901) (FAL 1903)) (PCE (AUS ENG))"


def test_IFF():
    iff_1 = IFF(PCE("AUS", "ENG"), PRP(PCE("AUS")))
    assert str(iff_1) == "IFF (PCE (AUS ENG)) THN (PRP (PCE (AUS)))"

    iff_2 = IFF(PCE("AUS", "ENG"), PRP(PCE("AUS")), PRP(PCE("GER", "FRA")))
    assert (
        str(iff_2)
        == "IFF (PCE (AUS ENG)) THN (PRP (PCE (AUS))) ELS (PRP (PCE (GER FRA)))"
    )


def test_XOY():
    xoy_1 = XOY("AUS", "ENG")
    assert str(xoy_1) == "XOY (AUS) (ENG)"


def test_YDO():
    ydo_1 = YDO("AUS", Unit("AUS", "FLT", "ALB"))
    assert str(ydo_1) == "YDO (AUS) (AUS FLT ALB)"

    ydo_2 = YDO("AUS", Unit("AUS", "FLT", "ALB"), Unit("ENG", "AMY", "ANK"))
    assert str(ydo_2) == "YDO (AUS) (AUS FLT ALB) (ENG AMY ANK)"


def test_SND():
    snd_1 = SND("AUS", ["GER", "FRA"], PRP(PCE("TUR", "RUS")))
    assert str(snd_1) == "SND (AUS) (GER FRA) (PRP (PCE (TUR RUS)))"


def test_FWD():
    fwd_1 = FWD(["GER", "ITA"], "FRA", "AUS")
    assert str(fwd_1) == "FWD (GER ITA) (FRA) (AUS)"


def test_BCC():
    bcc_1 = BCC("AUS", ["GER", "FRA"], "ITA")
    assert str(bcc_1) == "BCC (AUS) (GER FRA) (ITA)"


def test_WHY():
    why_1 = WHY(PRP(PCE("AUS", "GER")))
    assert str(why_1) == "WHY (PRP (PCE (AUS GER)))"


def test_POB():
    pob_1 = POB(WHY(PRP(PCE("AUS", "GER"))))
    assert str(pob_1) == "POB (WHY (PRP (PCE (AUS GER))))"
