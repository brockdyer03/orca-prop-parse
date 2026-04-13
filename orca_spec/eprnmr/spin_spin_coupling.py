from pydantic import BaseModel, Field


class Spin_Spin_Coupling_Base(BaseModel):

    numOfNucPairs:      int         = Field(description="Number of nuclei pairs to calculate")
    numOfNucPairsDSO:   int         = Field(description="number of nuclear pairs to calculate DSO")
    numOfNucPairsPSO:   int         = Field(description="number of nuclear pairs to calculate PSO")
    numOfNucPairsFC:    int         = Field(description="number of nuclear pairs to calculate FC")
    numOfNucPairsSD:    int         = Field(description="number of nuclear pairs to calculate SD")
    numOfNucPairsSD_FC: int         = Field(description="number of nuclear pairs to calculate SD/FC")
    pairsInfo:          list[int]   = Field(description="Pairs Info: Col1->Index of A. Col2->Atom. Num. of A.  Col3->Index of B. Col4->Atom. Num. of B.")
    pairsDistances:     list[float] = Field(description="The distances of each pair")
    pairsTotalSSCIso:   list[float] = Field(description="The Spin-Spin coupling constant for each pair")
    Method:             str
    Level:              str
    Mult:               int
    State:              int
    Irrep:              int


class AutoCI_Spin_Spin_Coupling(Spin_Spin_Coupling_Base):
    pass


class CASSCF_Spin_Spin_Coupling(Spin_Spin_Coupling_Base):
    pass


class CIS_Spin_Spin_Coupling(Spin_Spin_Coupling_Base):
    pass


class ICE_Spin_Spin_Coupling(Spin_Spin_Coupling_Base):
    pass


class MCRPA_Spin_Spin_Coupling(Spin_Spin_Coupling_Base):
    pass


class MDCI_Spin_Spin_Coupling(Spin_Spin_Coupling_Base):
    pass


class MP2_Spin_Spin_Coupling(Spin_Spin_Coupling_Base):
    pass


class MRCI_Spin_Spin_Coupling(Spin_Spin_Coupling_Base):
    pass


class RASCI_Spin_Spin_Coupling(Spin_Spin_Coupling_Base):
    pass


class ROCIS_Spin_Spin_Coupling(Spin_Spin_Coupling_Base):
    pass


class RPA_Spin_Spin_Coupling(Spin_Spin_Coupling_Base):
    pass


class SCF_Spin_Spin_Coupling(Spin_Spin_Coupling_Base):
    pass


class Spin_Spin_Coupling(BaseModel):

    AutoCI:        AutoCI_Spin_Spin_Coupling
    CASSCF:        CASSCF_Spin_Spin_Coupling
    CIS:           CIS_Spin_Spin_Coupling
    ICE:           ICE_Spin_Spin_Coupling
    MCRPA:         MCRPA_Spin_Spin_Coupling
    MDCI:          MDCI_Spin_Spin_Coupling
    MP2:           MP2_Spin_Spin_Coupling
    MRCI:          MRCI_Spin_Spin_Coupling
    RASCI:         RASCI_Spin_Spin_Coupling
    ROCIS:         ROCIS_Spin_Spin_Coupling
    RPA:           RPA_Spin_Spin_Coupling
    SCF:           SCF_Spin_Spin_Coupling