from pydantic import BaseModel


class Nuclear_Gradient_Base(BaseModel):

    NAtoms:   int
    gradNorm: float
    grad:     list[float]
    Method:   str
    Level:    str
    Mult:     int
    State:    int
    Irrep:    int


class CIS_Nuclear_Gradient(Nuclear_Gradient_Base):
    pass


class MDCI_Nuclear_Gradient(Nuclear_Gradient_Base):
    pass


class MP2_Nuclear_Gradient(Nuclear_Gradient_Base):
    pass


class RASCI_Nuclear_Gradient(Nuclear_Gradient_Base):
    pass


class SCF_Nuclear_Gradient(Nuclear_Gradient_Base):
    pass


class Nuclear_Gradient(BaseModel):

    CIS:   CIS_Nuclear_Gradient | None
    MDCI:  MDCI_Nuclear_Gradient | None
    MP2:   MP2_Nuclear_Gradient | None
    RASCI: RASCI_Nuclear_Gradient | None
    SCF:   SCF_Nuclear_Gradient | None
