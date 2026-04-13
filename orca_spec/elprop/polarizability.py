from pydantic import BaseModel, Field


class Polarizability_Base(BaseModel):

    isotropicPolar:     float
    rawCartesian:       list[float]
    diagonalizedTensor: list[float]
    orientation:        list[float]
    doAtomicPolar:      bool
    atomicPolarIso:     list[float] | None = Field(description="Atomic istotropic polarizabilities")
    Method:             str
    Level:              str
    Mult:               int
    State:              int
    Irrep:              int


class AutoCI_Polarizability(Polarizability_Base):
    pass


class CASSCF_Polarizability(Polarizability_Base):
    pass


class CIS_Polarizability(Polarizability_Base):
    pass


class ICE_Polarizability(Polarizability_Base):
    pass


class MCRPA_Polarizability(Polarizability_Base):
    pass


class MDCI_Polarizability(Polarizability_Base):
    pass


class MP2_Polarizability(Polarizability_Base):
    pass


class MRCI_Polarizability(Polarizability_Base):
    pass


class RASCI_Polarizability(Polarizability_Base):
    pass


class ROCIS_Polarizability(Polarizability_Base):
    pass


class RPA_Polarizability(Polarizability_Base):
    pass


class SCF_Polarizability(Polarizability_Base):
    pass


class Polarizability(BaseModel):

    AutoCI:        AutoCI_Polarizability | None
    CASSCF:        CASSCF_Polarizability | None
    CIS:           CIS_Polarizability | None
    ICE:           ICE_Polarizability | None
    MCRPA:         MCRPA_Polarizability | None
    MDCI:          MDCI_Polarizability | None
    MP2:           MP2_Polarizability | None
    MRCI:          MRCI_Polarizability | None
    RASCI:         RASCI_Polarizability | None
    ROCIS:         ROCIS_Polarizability | None
    RPA:           RPA_Polarizability | None
    SCF:           SCF_Polarizability | None
