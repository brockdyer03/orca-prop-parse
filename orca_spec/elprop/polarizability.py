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
    AutoCI:        AutoCI_Polarizability
    CASSCF:        CASSCF_Polarizability
    CIS:           CIS_Polarizability
    ICE:           ICE_Polarizability
    MCRPA:         MCRPA_Polarizability
    MDCI:          MDCI_Polarizability
    MP2:           MP2_Polarizability
    MRCI:          MRCI_Polarizability
    RASCI:         RASCI_Polarizability
    ROCIS:         ROCIS_Polarizability
    RPA:           RPA_Polarizability
    SCF:           SCF_Polarizability