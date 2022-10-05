import pytest


@pytest.fixture(scope="session")
def sample_daide_messages():
    return [
        "PRP(XDO((ENG FLT EDI) SUP (ENG AMY LVP) MTO CLY))",
        "PRP(XDO((ENG FLT (STP SCS)) SUP (ENG AMY LVP) MTO CLY))",
    ]
