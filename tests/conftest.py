import pytest

from daidepp.grammar import create_daide_grammar
from daidepp.grammar.grammar import DAIDELevel


@pytest.fixture(scope="session")
def sample_daide_messages():
    return [
        "PRP(XDO((ENG FLT EDI) SUP (ENG AMY LVP) MTO CLY))",
        "PRP(XDO((ENG FLT (STP SCS)) SUP (ENG AMY LVP) MTO CLY))",
    ]


@pytest.fixture(scope="session")
def _grammar():
    return {
        level: create_daide_grammar(level=level, allow_just_arrangement=True)
        for level in range(10, DAIDELevel.__args__[-1] + 10, 10)
    }


@pytest.fixture
def grammar(_grammar, request):
    return _grammar[request.param]


@pytest.fixture
def level_10_messages():
    return [
        "PCE (AUS GER)",
        "PCE (AUS FRA ENG)",
        "CCL (PRP (PCE (AUS FRA GER)))",
        "TRY (PRP PCE ALY VSS)",
        "HUH (CCL (PRP (PCE (AUS FRA GER))))",
        "PRP (PCE (AUS TUR))",
        "ALY (ITA TUR) VSS (ENG RUS)",
        "SLO (ENG)",
        "NOT (PCE (AUS FRA))",
        "NAR (PCE (AUS FRA))",
        "DRW",
        "DRW (ENG ITA)",
        "YES (PRP (ALY (ITA TUR) VSS (ENG RUS)))",
        "REJ (PRP (ALY (ITA TUR) VSS (ENG RUS)))",
        "BWX(PRP (ALY (     ITA      TUR)     VSS (    ENG RUS )  ))",
        "FCT (PCE (TUR RUS))",
        "FRM (AUS) (ENG GER) (PRP (PCE (AUS GER)))",
        "FRM ( AUS      ) (ENG GER) (PRP (ALY (ITA TUR) VSS (ENG RUS)))",
    ]


@pytest.fixture
def level_20_messages():
    return [
        "XDO ((ENG FLT EDI) HLD)",
        "XDO ((ENG FLT EDI) MTO CLY)",
        "XDO ((ENG FLT EDI) SUP (ENG AMY LVP))",
        "XDO ((ENG FLT EDI) SUP (ENG AMY LVP) MTO CLY)",
        "XDO ((ENG FLT (STP SCS)) SUP (ENG AMY LVP) MTO CLY)",
        "XDO ((ENG FLT EDI) CTO LVP VIA (ADR))",
        "XDO ((ENG FLT EDI) CTO LVP VIA (ADR AEG))",
        "XDO ((ENG FLT EDI) RTO LVP)",
        "XDO ((ENG FLT EDI) DSB)",
        "XDO ((ENG FLT EDI) BLD)",
        "XDO ((ENG FLT EDI) REM)",
        "XDO (AUS WVE)",
        "DMZ (AUS) (LVP)",
        "DMZ (AUS GER) (LVP CLY)",
    ]


@pytest.fixture
def level_30_messages():
    return [
        "AND (PCE (AUS GER)) (PCE (AUS ENG))",
        "AND (PCE (AUS GER)) (PCE (AUS FRA))",
        "AND (ALY (ITA TUR) VSS (ENG RUS)) (ALY (ITA TUR) VSS (ENG GER))",
        "AND (DRW) (DRW (ENG FRA))",
        "AND (SLO (ENG)) (DRW (ITA AUS))",
        "AND (NOT (PCE (AUS FRA))) (SLO (ENG))",
        "AND (NAR (PCE (AUS FRA))) (NOT (PCE (AUS GER)))",
        "AND ((ENG FLT EDI) MTO CLY) (SLO (ENG))",
        "AND (XDO ((ENG FLT EDI) HLD)) ((ENG FLT EDI) MTO CLY)",
        "AND (XDO ((ENG FLT EDI) MTO CLY)) ((ENG FLT EDI) MTO CLY)",
        "AND (XDO ((ENG FLT EDI) SUP (ENG AMY LVP))) ((ENG FLT EDI) MTO CLY)",
        "AND (XDO ((ENG FLT EDI) SUP (ENG AMY LVP) MTO CLY)) ((ENG FLT EDI) MTO CLY)",
        "AND (XDO ((ENG FLT (STP SCS)) SUP (ENG AMY LVP) MTO CLY)) ((ENG FLT EDI) MTO CLY)",
        "AND (XDO ((ENG FLT EDI) CTO LVP VIA (ADR))) ((ENG FLT EDI) MTO CLY)",
        "AND (XDO ((ENG FLT EDI) CTO LVP VIA (ADR AEG))) ((ENG FLT EDI) MTO CLY)",
        "AND (XDO ((ENG FLT EDI) RTO LVP)) ((ENG FLT EDI) MTO CLY)",
        "AND (XDO ((ENG FLT EDI) DSB)) ((ENG FLT EDI) MTO CLY)",
        "AND (XDO ((ENG FLT EDI) BLD)) ((ENG FLT EDI) MTO CLY)",
        "AND (DMZ (AUS) (LVP)) (DMZ (AUS GER) (LVP CLY))",
        "ORR (PCE (AUS GER)) (PCE (AUS FRA))",
        "ORR (ALY (ITA TUR) VSS (ENG RUS)) (ALY (ITA TUR) VSS (ENG GER))",
        "ORR (DRW) (DRW (ENG FRA))",
        "ORR (SLO (ENG)) (DRW (ITA AUS))",
        "ORR (NOT (PCE (AUS FRA))) (SLO (ENG))",
        "ORR (NAR (PCE (AUS FRA))) (NOT (PCE (AUS GER)))",
        "ORR ((ENG FLT EDI) MTO CLY) (SLO (ENG))",
        "ORR (XDO ((ENG FLT EDI) HLD)) ((ENG FLT EDI) MTO CLY)",
        "ORR (XDO ((ENG FLT EDI) MTO CLY)) ((ENG FLT EDI) MTO CLY)",
        "ORR (XDO ((ENG FLT EDI) SUP (ENG AMY LVP))) ((ENG FLT EDI) MTO CLY)",
        "ORR (XDO ((ENG FLT EDI) SUP (ENG AMY LVP) MTO CLY)) ((ENG FLT EDI) MTO CLY)",
        "ORR (XDO ((ENG FLT (STP SCS)) SUP (ENG AMY LVP) MTO CLY)) ((ENG FLT EDI) MTO CLY)",
        "ORR (XDO ((ENG FLT EDI) CTO LVP VIA (ADR))) ((ENG FLT EDI) MTO CLY)",
        "ORR (XDO ((ENG FLT EDI) CTO LVP VIA (ADR AEG))) ((ENG FLT EDI) MTO CLY)",
        "ORR (XDO ((ENG FLT EDI) RTO LVP)) ((ENG FLT EDI) MTO CLY)",
        "ORR (XDO ((ENG FLT EDI) DSB)) ((ENG FLT EDI) MTO CLY)",
        "ORR (XDO ((ENG FLT EDI) BLD)) ((ENG FLT EDI) MTO CLY)",
        "ORR (DMZ (AUS) (LVP)) (DMZ (AUS GER) (LVP CLY))",
    ]


@pytest.fixture
def level_40_messages():
    return [
        "SCD (AUS ANK) (GER BRE)",
        "SCD (AUS ANK BEL BER) (GER BRE BUD BUL DEN)",
        "SCD (AUS ANK BEL BER) (GER BRE BUD BUL DEN) (FRA GRE HOL KIE)",
        "OCC (GER FLT ALB) (FRA FLT ALB)",
        "OCC (AUS FLT ALB) (ENG AMY ANK) (FRA FLT APU)",
    ]


@pytest.fixture
def level_50_messages():
    return [
        "AND (AND (XDO ((ENG FLT EDI) BLD)) ((ENG FLT EDI) MTO CLY)) (ORR (DMZ (AUS) (LVP)) (DMZ (AUS GER) (LVP CLY)))",
        "AND (ORR (XDO ((ENG FLT EDI) SUP (ENG AMY LVP) MTO CLY)) ((ENG FLT EDI) MTO CLY)) (AND (AND (XDO ((ENG FLT EDI) BLD)) ((ENG FLT EDI) MTO CLY)) (ORR (DMZ (AUS) (LVP)) (DMZ (AUS GER) (LVP CLY))))",
        "ORR (AND (XDO ((ENG FLT EDI) BLD)) ((ENG FLT EDI) MTO CLY)) (ORR (DMZ (AUS) (LVP)) (DMZ (AUS GER) (LVP CLY)))",
        "ORR (ORR (XDO ((ENG FLT EDI) SUP (ENG AMY LVP) MTO CLY)) ((ENG FLT EDI) MTO CLY)) (AND (AND (XDO ((ENG FLT EDI) BLD)) ((ENG FLT EDI) MTO CLY)) (ORR (DMZ (AUS) (LVP)) (DMZ (AUS GER) (LVP CLY))))",
        "CHO (1 2) (PCE (AUS ENG)) (ALY (ITA TUR) VSS (ENG RUS))",
    ]


@pytest.fixture
def level_60_messages():
    return [
        "INS (PCE (ITA TUR))",
        "QRY (PCE (ITA TUR))",
        "THK (PCE (GER FRA))",
        "THK (QRY (PCE (GER FRA)))",
        "THK (NOT (PCE (GER FRA)))",
        "THK (NOT (QRY (PCE (GER FRA))))",
        "IDK (QRY (PCE (GER FRA)))",
        "SUG (PCE (ENG FRA))",
        "FCT (QRY (PCE (GER FRA)))",
        "FCT (NOT (PCE (GER FRA)))",
        "FCT (NOT (QRY (PCE (GER FRA))))",
        "NOT (PCE (GER RUS))",
        "NOT (QRY (PCE (GER FRA)))",
    ]


@pytest.fixture
def level_70_messages():
    return [
        "WHT (ENG FLT EDI)",
        "HOW (LVP)",
        "HOW (AUS)",
    ]


@pytest.fixture
def level_80_messages():
    return [
        "EXP (SPR 1901) (PRP (PCE (ENG GER)))",
        "IDK (EXP (SPR 1901) (PRP (PCE (ENG GER))))",
        "IDK (QRY (PCE (GER FRA)))",
    ]


@pytest.fixture
def level_90_messages():
    return [
        "FOR (SPR 1901) (PCE (GER AUS))",
        "FOR ((SPR 1901) (FAL 1903)) (PCE (FRA ENG))",
    ]


@pytest.fixture
def level_100_messages():
    return [
        "IFF (PCE (ENG FRA)) THN (PRP (PCE (ITA TUR)))",
        "IFF (PCE (ENG FRA)) THN (PRP (PCE (ITA TUR))) ELS (PRP (PCE (RUS ITA)))",
    ]


@pytest.fixture
def level_110_messages():
    return [
        "XOY (ENG) (GER)",
        "YDO (ENG) (GER AMY LVP)",
    ]


@pytest.fixture
def level_120_messages():
    return [
        "SND (ENG) (GER) (PRP (PCE (GER ITA)))",
        "SND (ENG) (GER FRA) (PCE (GER FRA))",
        "FWD (ENG) (GER) (ITA)",
        "FWD (ENG FRA) (GER) (ITA)",
        "BCC (ENG) (FRA) (RUS)",
        "BCC (ENG) (FRA GER) (RUS)",
    ]


@pytest.fixture
def level_130_messages():
    return [
        "WHY (FCT (PCE (TUR RUS)))",
        "WHY (THK (QRY (PCE (GER FRA))))",
        "WHY (PRP(XDO((ENG FLT EDI) SUP (ENG AMY LVP) MTO CLY)))",
        "WHY (INS (PCE (ITA TUR)))",
        "POB (WHY (PRP(XDO((ENG FLT EDI) SUP (ENG AMY LVP) MTO CLY))))",
        "IDK (QRY (PCE (ITA TUR)))",
        "IDK (EXP (SPR 1901) (PRP (PCE (ENG GER))))",
        "IDK (WHT (ENG FLT EDI))",
        "IDK (PRP(XDO((ENG FLT EDI) SUP (ENG AMY LVP) MTO CLY)))",
        "IDK (INS (PCE (ITA TUR)))",
        "IDK (SUG (PCE (ENG FRA)))",
    ]


@pytest.fixture
def level_140_messages():
    return [
        "UHY (PRP (ALY (ITA TUR) VSS (ENG RUS)))",
        "UHY ( PRP ( PCE ( AUS GER ) ) )",
        "HPY (PRP (ALY (ITA TUR) VSS (ENG RUS)))",
        "ANG (PRP (ALY (ITA TUR) VSS (ENG RUS)))",
    ]


@pytest.fixture
def level_150_messages():
    return ["RFO"]


@pytest.fixture
def level_160_messages():
    return [
        "ULB (AUS 0.9)",
        "UUB (GER 0.1)",
    ]


@pytest.fixture
def bad_messages():
    return [
        "PRP (ENNG GER)",
        "DMZ (STP NCS) (STP SCS)",
        "DMZ (SPA NCS) (BUL ECS)",
    ]
