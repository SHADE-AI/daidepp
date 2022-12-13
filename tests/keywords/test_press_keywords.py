import pytest

from daidepp.keywords.press_keywords import *


@pytest.mark.parametrize(
    # fmt: off
    ["input", "expected_output"], 
    [
        (("AUS", "ENG"), "PCE ( AUS ENG )"),
        (("AUS", "ENG", "FRA"), "PCE ( AUS ENG FRA )"),
    ],
    # fmt: on
)
def test_PCE(input, expected_output):
    pce = PCE(*input)
    assert str(pce) == expected_output

    with pytest.raises(Exception):
        PCE("AUS")


@pytest.mark.parametrize(
    # fmt: off
    ["input"], 
    [
        (("AUS",), ),
    ],
    # fmt: on
)
def test_PCE_bad(input):
    with pytest.raises(Exception):
        PCE(*input)


@pytest.mark.parametrize(
    # fmt: off
    ["input", "expected_output"], 
    [
        ((PCE("AUS", "ENG"),), "PRP ( PCE ( AUS ENG ) )"),
        ((PCE("AUS", "ENG", "FRA"),), "PRP ( PCE ( AUS ENG FRA ) )"),
    ],
    # fmt: on
)
def test_PRP(input, expected_output):
    arr = PRP(*input)
    assert str(arr) == expected_output


def test_PRP_bad():
    with pytest.raises(Exception):
        PRP(PCE("AUS"))


@pytest.mark.parametrize(
    # fmt: off
    ["input", "expected_output"],
    [
        ((PRP(PCE("AUS", "ENG")),), "CCL ( PRP ( PCE ( AUS ENG ) ) )"),
        ((PRP(PCE("AUS", "ENG", "FRA")),), "CCL ( PRP ( PCE ( AUS ENG FRA ) ) )"),
    ],
    # fmt: on
)
def test_CCL(input, expected_output):
    ccl = CCL(*input)
    assert str(ccl) == expected_output


@pytest.mark.parametrize(
    # fmt: off
    ["input", "expected_output"],
    [
        (("PRP",), "TRY ( PRP )"),
        (("PCE", "ALY",), "TRY ( PCE ALY )"),
        (("VSS", "DRW", "SLO",), "TRY ( VSS DRW SLO )"),
    ],
    # fmt: on
)
def test_TRY(input, expected_output):
    try_1 = TRY(*input)
    assert str(try_1) == expected_output


@pytest.mark.parametrize(
    # fmt: off
    ["input", "expected_output"],
    [
        ((PRP(PCE("AUS", "ENG")),), "HUH ( PRP ( PCE ( AUS ENG ) ) )"),
        ((PRP(PCE("AUS", "ENG", "FRA")),), "HUH ( PRP ( PCE ( AUS ENG FRA ) ) )"),
    ],
    # fmt: on
)
def test_HUH(input, expected_output):
    huh_1 = HUH(*input)
    assert str(huh_1) == expected_output


@pytest.mark.parametrize(
    # fmt: off
    ["input", "expected_output"],
    [
        ((["AUS", "GER"], ["TUR", "ITA"],), "ALY ( AUS GER ) VSS ( TUR ITA )"),
    ],
    # fmt: on
)
def test_ALYVSS(input, expected_output):
    alyvss = ALYVSS(*input)
    assert str(alyvss) == expected_output

    
@pytest.mark.parametrize(
    # fmt: off
    ["input"],
    [
        ((["AUS"], ["ENG"],),),
        ((["FRA"], ["GER", "TUR"],),),
        ((["AUS", "FRA"],[]),),
    ],
    # fmt: on
)
def test_ALYVSS_bad(input):
    with pytest.raises(Exception):
        ALYVSS(*input)


@pytest.mark.parametrize(
    # fmt: off
    ["input", "expected_output"],
    [
        (("AUS",), "SLO ( AUS )"),
        (("GER",), "SLO ( GER )"),
    ],
    # fmt: on
)
def test_SLO(input, expected_output):
    slo = SLO(*input)
    assert str(slo) == expected_output


@pytest.mark.parametrize(
    # fmt: off
    ["input", "expected_output"],
    [
        ((PCE("AUS", "ENG"),), "NOT ( PCE ( AUS ENG ) )"),
    ],
    # fmt: on
)
def test_NOT(input, expected_output):
    not_1 = NOT(*input)
    assert str(not_1) == expected_output


@pytest.mark.parametrize(
    # fmt: off
    ["input", "expected_output"],
    [
        ((PCE("AUS", "ENG"), ), "NAR ( PCE ( AUS ENG ) )"),
    ],
    # fmt: on
)
def test_NAR(input, expected_output):
    nar = NAR(*input)
    assert str(nar) == expected_output


@pytest.mark.parametrize(
    # fmt: off
    ["input", "expected_output"],
    [
        ((), "DRW"),
        (("AUS", "ENG",), "DRW ( AUS ENG )"),
    ],
    # fmt: on
)
def test_DRW(input, expected_output):
    drw = DRW(*input)
    assert str(drw) == expected_output


@pytest.mark.parametrize(
    # fmt: off
    ["input", "expected_output"],
    [
        ((PRP(PCE("AUS", "ENG")),), "YES ( PRP ( PCE ( AUS ENG ) ) )"),
    ],
    # fmt: on
)
def test_YES(input, expected_output):
    yes = YES(*input)
    assert str(yes) == expected_output


@pytest.mark.parametrize(
    # fmt: off
    ["input", "expected_output"],
    [
        ((PRP(PCE("AUS", "ENG")),), "REJ ( PRP ( PCE ( AUS ENG ) ) )"),
    ],
    # fmt: on
)
def test_REJ(input, expected_output):
    rej = REJ(*input)
    assert str(rej) == expected_output


@pytest.mark.parametrize(
    # fmt: off
    ["input", "expected_output"],
    [
        ((PRP(PCE("AUS", "ENG")),), "BWX ( PRP ( PCE ( AUS ENG ) ) )"),
    ],
    # fmt: on
)
def test_BWX(input, expected_output):
    bwx = BWX(*input)
    assert str(bwx) == expected_output


@pytest.mark.parametrize(
    # fmt: off
    ["input", "expected_output"],
    [
        ((PCE("AUS", "ENG"),), "FCT ( PCE ( AUS ENG ) )"),
        ((NOT(PCE("AUS", "ENG")),), "FCT ( NOT ( PCE ( AUS ENG ) ) )"),
    ],
    # fmt: on
)
def test_FCT(input, expected_output):
    fct = FCT(*input)
    assert str(fct) == expected_output


@pytest.mark.parametrize(
    # fmt: off
    ["input", "expected_output"],
    [
        (("AUS", ["GER", "FRA"], PRP(PCE("AUS", "ENG")),), "FRM ( AUS ) ( GER FRA ) ( PRP ( PCE ( AUS ENG ) ) )"),
    ],
    # fmt: on
)
def test_FRM(input, expected_output):
    frm = FRM(*input)

    assert str(frm) == expected_output


@pytest.mark.parametrize(
    # fmt: off
    ["input", "expected_output"],
    [
        ((HLD(Unit("AUS", "FLT", Location("ALB"))),), "XDO ( ( AUS FLT ALB ) HLD )"),
        ((MTO(Unit("AUS", "FLT", Location("ALB")), Location("BUL")),), "XDO ( ( AUS FLT ALB ) MTO BUL )"),
    ],
    # fmt: on
)
def test_XDO(input, expected_output):
    xdo = XDO(*input)
    assert str(xdo) == expected_output


@pytest.mark.parametrize(
    # fmt: off
    ["input", "expected_output"],
    [
        ((["AUS"], [Location("EDI")],), "DMZ ( AUS ) ( EDI )"),
        ((["ITA", "TUR"], [Location("CLY"), Location("ALB")],), "DMZ ( ITA TUR ) ( CLY ALB )"),
    ],
    # fmt: on
)
def test_DMZ(input, expected_output):
    dmz = DMZ(*input)
    assert str(dmz) == expected_output


@pytest.mark.parametrize(
    # fmt: off
    ["input", "expected_output"],
    [
        ((PCE("AUS", "GER"), PCE("AUS", "ENG"),), "AND ( PCE ( AUS GER ) ) ( PCE ( AUS ENG ) )"),
        ((PCE("AUS", "GER"), PCE("AUS", "ENG"), PCE("AUS", "ENG", "FRA"),), "AND ( PCE ( AUS GER ) ) ( PCE ( AUS ENG ) ) ( PCE ( AUS ENG FRA ) )"),
    ],
    # fmt: on
)
def test_AND(input, expected_output):
    and_1 = AND(*input)
    assert str(and_1) == expected_output


@pytest.mark.parametrize(
    # fmt: off
    ["input", "expected_output"],
    [
        ((PCE("AUS", "GER"), PCE("AUS", "ENG"),), "ORR ( PCE ( AUS GER ) ) ( PCE ( AUS ENG ) )"),
        ((PCE("AUS", "GER"), PCE("AUS", "ENG"), PCE("AUS", "ENG", "FRA"),), "ORR ( PCE ( AUS GER ) ) ( PCE ( AUS ENG ) ) ( PCE ( AUS ENG FRA ) )"),
    ],
    # fmt: on
)
def test_ORR(input, expected_output):
    orr = ORR(*input)
    assert str(orr) == expected_output


@pytest.mark.parametrize(
    # fmt: off
    ["input", "expected_output"],
    [
        ((PowerAndSupplyCenters("AUS", Location("ANK"), Location("BEL"), Location("BER")), PowerAndSupplyCenters("GER", Location("BRE"), Location("BUD")),), "SCD ( AUS ANK BEL BER ) ( GER BRE BUD )"),
    ],
    # fmt: on
)
def test_SCD(input, expected_output):
    scd = SCD(*input)
    assert str(scd) == expected_output


@pytest.mark.parametrize(
    # fmt: off
    ["input", "expected_output"],
    [
        ((Unit("AUS", "FLT", Location("ALB")), Unit("ENG", "AMY", Location("ANK")), Unit("FRA", "FLT", Location("APU")),), "OCC ( AUS FLT ALB ) ( ENG AMY ANK ) ( FRA FLT APU )"),
    ],
    # fmt: on
)
def test_OCC(input, expected_output):
    occ = OCC(*input)
    assert str(occ) == expected_output


@pytest.mark.parametrize(
    # fmt: off
    ["input", "expected_output"],
    [
        ((1901, 1903, PCE("AUS", "GER"), PCE("AUS", "ENG"),), "CHO ( 1901 1903 ) ( PCE ( AUS GER ) ) ( PCE ( AUS ENG ) )"),
    ],
    # fmt: on
)
def test_CHO(input, expected_output):
    cho = CHO(*input)
    assert str(cho) == expected_output


@pytest.mark.parametrize(
    # fmt: off
    ["input", "expected_output"],
    [
        ((PCE("AUS", "GER"),), "INS ( PCE ( AUS GER ) )"),
    ],
    # fmt: on
)
def test_INS(input, expected_output):
    ins = INS(*input)
    assert str(ins) == expected_output


@pytest.mark.parametrize(
    # fmt: off
    ["input", "expected_output"],
    [
        ((PCE("AUS", "GER"),), "QRY ( PCE ( AUS GER ) )"),
    ],
    # fmt: on
)
def test_QRY(input, expected_output):
    qry = QRY(*input)
    assert str(qry) == expected_output


@pytest.mark.parametrize(
    # fmt: off
    ["input", "expected_output"],
    [
        ((PCE("AUS", "GER"),), "THK ( PCE ( AUS GER ) )"),
    ],
    # fmt: on
)
def test_THK(input, expected_output):
    thk = THK(*input)
    assert str(thk) == expected_output


@pytest.mark.parametrize(
    # fmt: off
    ["input", "expected_output"],
    [
        ((PRP(PCE("AUS", "GER")),), "IDK ( PRP ( PCE ( AUS GER ) ) )"),
    ],
    # fmt: on
)
def test_IDK(input, expected_output):
    idk = IDK(*input)
    assert str(idk) == expected_output


@pytest.mark.parametrize(
    # fmt: off
    ["input", "expected_output"],
    [
        ((PCE("AUS", "GER"),), "SUG ( PCE ( AUS GER ) )"),
    ],
    # fmt: on
)
def test_SUG(input, expected_output):
    sug = SUG(*input)
    assert str(sug) == expected_output


@pytest.mark.parametrize(
    # fmt: off
    ["input", "expected_output"],
    [
        ((Unit("AUS", "FLT", Location("ALB")),), "WHT ( AUS FLT ALB )"),
    ],
    # fmt: on
)
def test_WHT(input, expected_output):
    wht = WHT(*input)

    assert str(wht) == expected_output


@pytest.mark.parametrize(
    # fmt: off
    ["input", "expected_output"],
    [
        (("AUS",), "HOW ( AUS )"),
        ((Location("APU"),), "HOW ( APU )"),
    ],
    # fmt: on
)
def test_HOW(input, expected_output):
    how = HOW(*input)
    assert str(how) == expected_output


@pytest.mark.parametrize(
    # fmt: off
    ["input", "expected_output"],
    [
        ((Turn("SPR", 1901), PRP(PCE("AUS", "ENG")),), "EXP ( SPR 1901 ) ( PRP ( PCE ( AUS ENG ) ) )"),
    ],
    # fmt: on
)
def test_EXP(input, expected_output):
    exp = EXP(*input)

    assert str(exp) == expected_output


@pytest.mark.parametrize(
    # fmt: off
    ["input", "expected_output"],
    [
        ((EXP(Turn("SPR", 1901), PRP(PCE("AUS", "ENG"))),), "SRY ( EXP ( SPR 1901 ) ( PRP ( PCE ( AUS ENG ) ) ) )"),
    ],
    # fmt: on
)
def test_SRY(input, expected_output):
    sry = SRY(*input)

    assert str(sry) == expected_output


@pytest.mark.parametrize(
    # fmt: off
    ["input", "expected_output"],
    [
        ((Turn("SPR", 1901), None, PCE("AUS", "ENG"),), "FOR ( SPR 1901 ) ( PCE ( AUS ENG ) )"),
        ((Turn("SPR", 1901), Turn("FAL", 1903), PCE("AUS", "ENG"),), "FOR ( ( SPR 1901 ) ( FAL 1903 ) ) ( PCE ( AUS ENG ) )"),
    ],
    # fmt: on
)
def test_FOR(input, expected_output):
    for_1 = FOR(*input)
    assert str(for_1) == expected_output


@pytest.mark.parametrize(
    # fmt: off
    ["input", "expected_output"],
    [
        ((PCE("AUS", "ENG"), PRP(PCE("AUS", "GER")),), "IFF ( PCE ( AUS ENG ) ) THN ( PRP ( PCE ( AUS GER ) ) )"),
        ((PCE("AUS", "ENG"), PRP(PCE("AUS", "GER")), PRP(PCE("GER", "FRA")),), "IFF ( PCE ( AUS ENG ) ) THN ( PRP ( PCE ( AUS GER ) ) ) ELS ( PRP ( PCE ( GER FRA ) ) )"),
    ],
    # fmt: on
)
def test_IFF(input, expected_output):
    iff = IFF(*input)
    assert str(iff) == expected_output


@pytest.mark.parametrize(
    # fmt: off
    ["input", "expected_output"],
    [
        (("AUS", "ENG",), "XOY ( AUS ) ( ENG )"),
    ],
    # fmt: on
)
def test_XOY(input, expected_output):
    xoy_1 = XOY(*input)
    assert str(xoy_1) == expected_output


@pytest.mark.parametrize(
    # fmt: off
    ["input", "expected_output"],
    [
        (("AUS", Unit("AUS", "FLT", Location("ALB")),), "YDO ( AUS ) ( AUS FLT ALB )"),
        (("AUS", Unit("AUS", "FLT", Location("ALB")), Unit("ENG", "AMY", Location("ANK")),), "YDO ( AUS ) ( AUS FLT ALB ) ( ENG AMY ANK )"),
    ],
    # fmt: on
)
def test_YDO(input, expected_output):
    ydo = YDO(*input)
    assert str(ydo) == expected_output


@pytest.mark.parametrize(
    # fmt: off
    ["input", "expected_output"],
    [
        (("AUS", ["GER", "FRA"], PRP(PCE("TUR", "RUS")),), "SND ( AUS ) ( GER FRA ) ( PRP ( PCE ( TUR RUS ) ) )"),
    ],
    # fmt: on
)
def test_SND(input, expected_output):
    snd = SND(*input)
    assert str(snd) == expected_output


@pytest.mark.parametrize(
    # fmt: off
    ["input", "expected_output"],
    [
        ((["GER", "ITA"], "FRA", "AUS",), "FWD ( GER ITA ) ( FRA ) ( AUS )"),
    ],
    # fmt: on
)
def test_FWD(input, expected_output):
    fwd = FWD(*input)
    assert str(fwd) == expected_output


@pytest.mark.parametrize(
    # fmt: off
    ["input", "expected_output"],
    [
        (("AUS", ["GER", "FRA"], "ITA",), "BCC ( AUS ) ( GER FRA ) ( ITA )"),
    ],
    # fmt: on
)
def test_BCC(input, expected_output):
    bcc = BCC(*input)
    assert str(bcc) == expected_output


@pytest.mark.parametrize(
    # fmt: off
    ["input", "expected_output"],
    [
        ((PRP(PCE("AUS", "GER")),), "WHY ( PRP ( PCE ( AUS GER ) ) )"),
    ],
    # fmt: on
)
def test_WHY(input, expected_output):
    why = WHY(*input)
    assert str(why) == expected_output


@pytest.mark.parametrize(
    # fmt: off
    ["input", "expected_output"],
    [
        ((WHY(PRP(PCE("AUS", "GER"))),), "POB ( WHY ( PRP ( PCE ( AUS GER ) ) ) )"),
    ],
    # fmt: on
)
def test_POB(input, expected_output):
    pob = POB(*input)
    assert str(pob) == expected_output
