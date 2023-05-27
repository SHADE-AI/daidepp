import re
from copy import deepcopy

import pytest

from daidepp.keywords.press_keywords import *


@pytest.mark.parametrize(
    ["input", "expected_output"],
    [
        (("AUS", "ENG"), "PCE ( AUS ENG )"),
        (("AUS", "ENG", "FRA"), "PCE ( AUS ENG FRA )"),
    ],
)
def test_PCE(input, expected_output):
    pce = PCE(*input)
    assert str(pce) == expected_output
    hash(pce)


@pytest.mark.parametrize(
    ["input"],
    [
        (("AUS",),),
    ],
)
def test_PCE_bad(input):
    with pytest.raises(Exception):
        PCE(*input)


@pytest.mark.parametrize(
    ["input", "expected_output"],
    [
        ((PCE("AUS", "ENG"),), "PRP ( PCE ( AUS ENG ) )"),
        ((PCE("AUS", "ENG", "FRA"),), "PRP ( PCE ( AUS ENG FRA ) )"),
    ],
)
def test_PRP(input, expected_output):
    arr = PRP(*input)
    assert str(arr) == expected_output
    hash(arr)


def test_PRP_bad():
    with pytest.raises(Exception):
        PRP(PCE("AUS"))


@pytest.mark.parametrize(
    ["input", "expected_output"],
    [
        ((PRP(PCE("AUS", "ENG")),), "CCL ( PRP ( PCE ( AUS ENG ) ) )"),
        ((PRP(PCE("AUS", "ENG", "FRA")),), "CCL ( PRP ( PCE ( AUS ENG FRA ) ) )"),
    ],
)
def test_CCL(input, expected_output):
    ccl = CCL(*input)
    assert str(ccl) == expected_output
    hash(ccl)


@pytest.mark.parametrize(
    ["input", "expected_output"],
    [
        (("PRP",), "TRY ( PRP )"),
        (
            (
                "PCE",
                "ALY",
            ),
            "TRY ( ALY PCE )",
        ),
        (
            (
                "VSS",
                "DRW",
                "SLO",
            ),
            "TRY ( DRW SLO VSS )",
        ),
    ],
)
def test_TRY(input, expected_output):
    try_1 = TRY(*input)
    assert str(try_1) == expected_output
    hash(try_1)

    reversed_input = reversed(input)
    try_2 = TRY(*reversed_input)
    assert try_1 == try_2


@pytest.mark.parametrize(
    ["input", "expected_output"],
    [
        ((PRP(PCE("AUS", "ENG")),), "HUH ( PRP ( PCE ( AUS ENG ) ) )"),
        ((PRP(PCE("AUS", "ENG", "FRA")),), "HUH ( PRP ( PCE ( AUS ENG FRA ) ) )"),
    ],
)
def test_HUH(input, expected_output):
    huh_1 = HUH(*input)
    assert str(huh_1) == expected_output
    hash(huh_1)


@pytest.mark.parametrize(
    ["input", "expected_output"],
    [
        (
            (
                ["AUS", "GER"],
                ["TUR", "ITA"],
            ),
            "ALY ( AUS GER ) VSS ( ITA TUR )",
        ),
    ],
)
def test_ALYVSS(input, expected_output):
    alyvss = ALYVSS(*input)
    assert str(alyvss) == expected_output
    hash(alyvss)


@pytest.mark.parametrize(
    ["input"],
    [
        (
            (
                ["AUS"],
                ["ENG"],
            ),
        ),
        (
            (
                ["FRA"],
                ["GER", "TUR"],
            ),
        ),
        ((["AUS", "FRA"], []),),
    ],
)
def test_ALYVSS_bad(input):
    with pytest.raises(Exception):
        ALYVSS(*input)


@pytest.mark.parametrize(
    ["input", "expected_output"],
    [
        (("AUS",), "SLO ( AUS )"),
        (("GER",), "SLO ( GER )"),
    ],
)
def test_SLO(input, expected_output):
    slo = SLO(*input)
    assert str(slo) == expected_output
    hash(slo)


@pytest.mark.parametrize(
    ["input", "expected_output"],
    [
        ((PCE("AUS", "ENG"),), "NOT ( PCE ( AUS ENG ) )"),
    ],
)
def test_NOT(input, expected_output):
    not_1 = NOT(*input)
    assert str(not_1) == expected_output
    hash(not_1)


@pytest.mark.parametrize(
    ["input", "expected_output"],
    [
        ((PCE("AUS", "ENG"),), "NAR ( PCE ( AUS ENG ) )"),
    ],
)
def test_NAR(input, expected_output):
    nar = NAR(*input)
    assert str(nar) == expected_output
    hash(nar)


@pytest.mark.parametrize(
    ["input", "expected_output"],
    [
        ((), "DRW"),
        (
            (
                "AUS",
                "ENG",
            ),
            "DRW ( AUS ENG )",
        ),
    ],
)
def test_DRW(input, expected_output):
    drw = DRW(*input)
    assert str(drw) == expected_output
    hash(drw)


@pytest.mark.parametrize(
    ["input", "expected_output"],
    [
        ((PRP(PCE("AUS", "ENG")),), "YES ( PRP ( PCE ( AUS ENG ) ) )"),
    ],
)
def test_YES(input, expected_output):
    yes = YES(*input)
    assert str(yes) == expected_output
    hash(yes)


@pytest.mark.parametrize(
    ["input", "expected_output"],
    [
        ((PRP(PCE("AUS", "ENG")),), "REJ ( PRP ( PCE ( AUS ENG ) ) )"),
    ],
)
def test_REJ(input, expected_output):
    rej = REJ(*input)
    assert str(rej) == expected_output
    hash(rej)


@pytest.mark.parametrize(
    ["input", "expected_output"],
    [
        ((PRP(PCE("AUS", "ENG")),), "BWX ( PRP ( PCE ( AUS ENG ) ) )"),
    ],
)
def test_BWX(input, expected_output):
    bwx = BWX(*input)
    assert str(bwx) == expected_output
    hash(bwx)


@pytest.mark.parametrize(
    ["input", "expected_output"],
    [
        ((PCE("AUS", "ENG"),), "FCT ( PCE ( AUS ENG ) )"),
        ((NOT(PCE("AUS", "ENG")),), "FCT ( NOT ( PCE ( AUS ENG ) ) )"),
    ],
)
def test_FCT(input, expected_output):
    fct = FCT(*input)
    assert str(fct) == expected_output
    hash(fct)


@pytest.mark.parametrize(
    ["input", "expected_output"],
    [
        (
            (
                "AUS",
                ["GER", "FRA"],
                PRP(PCE("AUS", "ENG")),
            ),
            "FRM ( AUS ) ( FRA GER ) ( PRP ( PCE ( AUS ENG ) ) )",
        ),
    ],
)
def test_FRM(input, expected_output):
    frm = FRM(*input)

    assert str(frm) == expected_output
    hash(frm)


@pytest.mark.parametrize(
    ["input", "expected_output"],
    [
        ((HLD(Unit("AUS", "FLT", Location("ALB"))),), "XDO ( ( AUS FLT ALB ) HLD )"),
        (
            (MTO(Unit("AUS", "FLT", Location("ALB")), Location("BUL")),),
            "XDO ( ( AUS FLT ALB ) MTO BUL )",
        ),
    ],
)
def test_XDO(input, expected_output):
    xdo = XDO(*input)
    assert str(xdo) == expected_output
    hash(xdo)


@pytest.mark.parametrize(
    ["input", "expected_output"],
    [
        (
            (
                ["AUS"],
                [Location("EDI")],
            ),
            "DMZ ( AUS ) ( EDI )",
        ),
        (
            (
                ["ITA", "TUR"],
                [Location("CLY"), Location("ALB")],
            ),
            "DMZ ( ITA TUR ) ( ALB CLY )",
        ),
    ],
)
def test_DMZ(input, expected_output):
    dmz = DMZ(*input)
    assert str(dmz) == expected_output
    hash(dmz)

    reversed_inputs = map(reversed, input)
    dmz_reversed = DMZ(*reversed_inputs)
    assert dmz == dmz_reversed


@pytest.mark.parametrize(
    ["input", "expected_substrings"],
    [
        (
            (
                PCE("AUS", "GER"),
                PCE("AUS", "ENG"),
            ),
            ["PCE ( AUS GER )", "PCE ( AUS ENG )"],
        ),
        (
            (
                PCE("AUS", "GER"),
                PCE("AUS", "ENG"),
                PCE("AUS", "ENG", "FRA"),
            ),
            ["PCE ( AUS GER )", "PCE ( AUS ENG )", "PCE ( AUS ENG FRA )"],
        ),
    ],
)
def test_AND(input, expected_substrings):
    and_1 = AND(*input)
    for substring in expected_substrings:
        assert substring in str(and_1)

    hash(and_1)

    reversed_input = reversed(input)
    and_2 = AND(*reversed_input)
    assert and_2 == and_1


@pytest.mark.parametrize(
    ["input", "expected_substrings"],
    [
        (
            (
                PCE("AUS", "GER"),
                PCE("AUS", "ENG"),
            ),
            ("PCE ( AUS GER )", "PCE ( AUS ENG )"),
        ),
        (
            (
                PCE("AUS", "GER"),
                PCE("AUS", "ENG"),
                PCE("AUS", "ENG", "FRA"),
            ),
            ("PCE ( AUS GER )", "PCE ( AUS ENG )", "PCE ( AUS ENG FRA )"),
        ),
    ],
)
def test_ORR(input, expected_substrings):
    orr = ORR(*input)
    orr_str = str(orr)
    for substring in expected_substrings:
        assert substring in orr_str

    hash(orr)

    reversed_input = reversed(input)
    orr_2 = ORR(*reversed_input)
    assert orr_2 == orr


@pytest.mark.parametrize(
    ["input", "expected_regex_substrings"],
    [
        (
            (
                PowerAndSupplyCenters(
                    "AUS", Location("ANK"), Location("BEL"), Location("BER")
                ),
                PowerAndSupplyCenters("GER", Location("BRE"), Location("BUD")),
            ),
            (
                r"\( AUS (ANK|BEL|BER) (ANK|BEL|BER) (ANK|BEL|BER) \)",
                r"\( GER (BRE|BUD) (BRE|BUD) \)",
            ),
        ),
    ],
)
def test_SCD(input, expected_regex_substrings):
    scd = SCD(*input)
    scd_str = str(scd)
    for substring in expected_regex_substrings:
        r = re.compile(substring)
        assert re.search(r, scd_str)

    hash(scd_str)

    reversed_input = reversed(input)
    scd_2 = SCD(*reversed_input)
    assert scd_2 == scd


@pytest.mark.parametrize(
    ["input", "expected_substrings"],
    [
        (
            (
                Unit("AUS", "FLT", Location("ALB")),
                Unit("ENG", "AMY", Location("ANK")),
                Unit("FRA", "FLT", Location("APU")),
            ),
            ("( AUS FLT ALB )", "( ENG AMY ANK )", "( FRA FLT APU )"),
        ),
    ],
)
def test_OCC(input, expected_substrings):
    occ = OCC(*input)
    occ_str = str(occ)
    for substring in expected_substrings:
        assert substring in occ_str

    hash(occ)

    reversed_input = reversed(input)
    occ_2 = OCC(*input)
    assert occ == occ_2


@pytest.mark.parametrize(
    ["input"],
    [
        [(1901, 1903, PCE("AUS", "GER"), PCE("AUS", "ENG"))],
    ],
)
def test_CHO(input):
    cho = CHO(*input)
    for arrangement in input[2:]:
        assert arrangement in cho.arrangements

    hash(cho)

    arrangements = list(reversed(input[2:]))
    cho_2 = CHO(input[0], input[1], *arrangements)  # type: ignore
    assert cho == cho_2


@pytest.mark.parametrize(
    ["input", "expected_output"],
    [
        ((PCE("AUS", "GER"),), "INS ( PCE ( AUS GER ) )"),
    ],
)
def test_INS(input, expected_output):
    ins = INS(*input)
    assert str(ins) == expected_output
    hash(ins)


@pytest.mark.parametrize(
    ["input", "expected_output"],
    [
        ((PCE("AUS", "GER"),), "QRY ( PCE ( AUS GER ) )"),
    ],
)
def test_QRY(input, expected_output):
    qry = QRY(*input)
    assert str(qry) == expected_output
    hash(qry)


@pytest.mark.parametrize(
    ["input", "expected_output"],
    [
        ((PCE("AUS", "GER"),), "THK ( PCE ( AUS GER ) )"),
    ],
)
def test_THK(input, expected_output):
    thk = THK(*input)
    assert str(thk) == expected_output
    hash(thk)


@pytest.mark.parametrize(
    ["input", "expected_output"],
    [
        ((PRP(PCE("AUS", "GER")),), "IDK ( PRP ( PCE ( AUS GER ) ) )"),
    ],
)
def test_IDK(input, expected_output):
    idk = IDK(*input)
    assert str(idk) == expected_output
    hash(idk)


@pytest.mark.parametrize(
    ["input", "expected_output"],
    [
        ((PCE("AUS", "GER"),), "SUG ( PCE ( AUS GER ) )"),
    ],
)
def test_SUG(input, expected_output):
    sug = SUG(*input)
    assert str(sug) == expected_output
    hash(sug)


@pytest.mark.parametrize(
    ["input", "expected_output"],
    [
        ((Unit("AUS", "FLT", Location("ALB")),), "WHT ( AUS FLT ALB )"),
    ],
)
def test_WHT(input, expected_output):
    wht = WHT(*input)

    assert str(wht) == expected_output
    hash(wht)


@pytest.mark.parametrize(
    ["input", "expected_output"],
    [
        (("AUS",), "HOW ( AUS )"),
        ((Location("APU"),), "HOW ( APU )"),
    ],
)
def test_HOW(input, expected_output):
    how = HOW(*input)
    assert str(how) == expected_output
    hash(how)


@pytest.mark.parametrize(
    ["input", "expected_output"],
    [
        (
            (
                Turn("SPR", 1901),
                PRP(PCE("AUS", "ENG")),
            ),
            "EXP ( SPR 1901 ) ( PRP ( PCE ( AUS ENG ) ) )",
        ),
    ],
)
def test_EXP(input, expected_output):
    exp = EXP(*input)

    assert str(exp) == expected_output
    hash(exp)


@pytest.mark.parametrize(
    ["input", "expected_output"],
    [
        (
            (EXP(Turn("SPR", 1901), PRP(PCE("AUS", "ENG"))),),
            "SRY ( EXP ( SPR 1901 ) ( PRP ( PCE ( AUS ENG ) ) ) )",
        ),
    ],
)
def test_SRY(input, expected_output):
    sry = SRY(*input)

    assert str(sry) == expected_output
    hash(sry)


@pytest.mark.parametrize(
    ["input", "expected_output"],
    [
        (
            (
                Turn("SPR", 1901),
                None,
                PCE("AUS", "ENG"),
            ),
            "FOR ( SPR 1901 ) ( PCE ( AUS ENG ) )",
        ),
        (
            (
                Turn("SPR", 1901),
                Turn("FAL", 1903),
                PCE("AUS", "ENG"),
            ),
            "FOR ( ( SPR 1901 ) ( FAL 1903 ) ) ( PCE ( AUS ENG ) )",
        ),
    ],
)
def test_FOR(input, expected_output):
    for_1 = FOR(*input)
    assert str(for_1) == expected_output
    hash(for_1)


@pytest.mark.parametrize(
    ["input", "expected_output"],
    [
        (
            (
                PCE("AUS", "ENG"),
                PRP(PCE("AUS", "GER")),
            ),
            "IFF ( PCE ( AUS ENG ) ) THN ( PRP ( PCE ( AUS GER ) ) )",
        ),
        (
            (
                PCE("AUS", "ENG"),
                PRP(PCE("AUS", "GER")),
                PRP(PCE("GER", "FRA")),
            ),
            "IFF ( PCE ( AUS ENG ) ) THN ( PRP ( PCE ( AUS GER ) ) ) ELS ( PRP ( PCE ( FRA GER ) ) )",
        ),
    ],
)
def test_IFF(input, expected_output):
    iff = IFF(*input)
    assert str(iff) == expected_output
    hash(iff)


@pytest.mark.parametrize(
    ["input", "expected_output"],
    [
        (
            (
                "AUS",
                "ENG",
            ),
            "XOY ( AUS ) ( ENG )",
        ),
    ],
)
def test_XOY(input, expected_output):
    xoy_1 = XOY(*input)
    assert str(xoy_1) == expected_output
    hash(xoy_1)


@pytest.mark.parametrize(
    ["input", "expected_output"],
    [
        (
            (
                "AUS",
                Unit("AUS", "FLT", Location("ALB")),
            ),
            "YDO ( AUS ) ( AUS FLT ALB )",
        ),
        (
            (
                "AUS",
                Unit("AUS", "FLT", Location("ALB")),
                Unit("ENG", "AMY", Location("ANK")),
            ),
            "YDO ( AUS ) ( AUS FLT ALB ) ( ENG AMY ANK )",
        ),
    ],
)
def test_YDO(input, expected_output):
    ydo = YDO(*input)
    assert str(ydo) == expected_output
    hash(ydo)


@pytest.mark.parametrize(
    ["input", "expected_output"],
    [
        (
            (
                "AUS",
                ["GER", "FRA"],
                PRP(PCE("TUR", "RUS")),
            ),
            "SND ( AUS ) ( FRA GER ) ( PRP ( PCE ( RUS TUR ) ) )",
        ),
    ],
)
def test_SND(input, expected_output):
    snd = SND(*input)
    assert str(snd) == expected_output
    hash(snd)


@pytest.mark.parametrize(
    ["input", "expected_output"],
    [
        (
            (
                ["GER", "ITA"],
                "FRA",
                "AUS",
            ),
            "FWD ( GER ITA ) ( FRA ) ( AUS )",
        ),
    ],
)
def test_FWD(input, expected_output):
    fwd = FWD(*input)
    assert str(fwd) == expected_output
    hash(fwd)


@pytest.mark.parametrize(
    ["input", "expected_output"],
    [
        (
            (
                "AUS",
                ["GER", "FRA"],
                "ITA",
            ),
            "BCC ( AUS ) ( FRA GER ) ( ITA )",
        ),
    ],
)
def test_BCC(input, expected_output):
    bcc = BCC(*input)
    assert str(bcc) == expected_output
    hash(bcc)


@pytest.mark.parametrize(
    ["input", "expected_output"],
    [
        ((PRP(PCE("AUS", "GER")),), "WHY ( PRP ( PCE ( AUS GER ) ) )"),
    ],
)
def test_WHY(input, expected_output):
    why = WHY(*input)
    assert str(why) == expected_output
    hash(why)


@pytest.mark.parametrize(
    ["input", "expected_output"],
    [
        ((WHY(PRP(PCE("AUS", "GER"))),), "POB ( WHY ( PRP ( PCE ( AUS GER ) ) ) )"),
    ],
)
def test_POB(input, expected_output):
    pob = POB(*input)
    assert str(pob) == expected_output
    hash(pob)


@pytest.mark.parametrize(
    ["input", "expected_output"],
    [
        ((PRP(PCE("AUS", "GER")),), "UHY ( PRP ( PCE ( AUS GER ) ) )"),
    ],
)
def test_UHY(input, expected_output):
    uhy = UHY(*input)
    assert str(uhy) == expected_output
    hash(uhy)


@pytest.mark.parametrize(
    ["input", "expected_output"],
    [
        ((PRP(PCE("AUS", "GER")),), "HPY ( PRP ( PCE ( AUS GER ) ) )"),
    ],
)
def test_HPY(input, expected_output):
    hpy = HPY(*input)
    assert str(hpy) == expected_output
    hash(hpy)


@pytest.mark.parametrize(
    ["input", "expected_output"],
    [
        ((PRP(PCE("AUS", "GER")),), "ANG ( PRP ( PCE ( AUS GER ) ) )"),
    ],
)
def test_ANG(input, expected_output):
    ang = ANG(*input)
    assert str(ang) == expected_output
    hash(ang)


def test_ROF():
    rof = ROF()
    assert str(rof) == "ROF"
    hash(rof)


@pytest.mark.parametrize(
    ["input", "expected_output"],
    [
        (("GER", 0.9), "ULB ( GER 0.9 )"),
        (("GER", 1.9), "ULB ( GER 1.9 )"),
        (("AUS", 0.2), "ULB ( AUS 0.2 )"),
    ],
)
def test_ULB(input, expected_output):
    ulb = ULB(*input)
    assert str(ulb) == expected_output
    hash(ulb)


@pytest.mark.parametrize(
    ["input", "expected_output"],
    [
        (("GER", 0.9), "UUB ( GER 0.9 )"),
        (("GER", 1.9), "UUB ( GER 1.9 )"),
        (("AUS", 0.2), "UUB ( AUS 0.2 )"),
    ],
)
def test_UUB(input, expected_output):
    uub = UUB(*input)
    assert str(uub) == expected_output
    hash(uub)
