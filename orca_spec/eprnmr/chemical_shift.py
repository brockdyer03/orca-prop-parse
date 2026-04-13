from pydantic import BaseModel, Field


class Chemical_Shift_Base(BaseModel):

    numOfNucs:   int
    Method:      str
    Level:       str
    Mult:        int
    State:       int
    Irrep:       int
    NUC:         list[int] = Field(description="Index of the nuclei")
    Elems:       list[int] = Field(description="Atomic number of the nuclei")
    SDSO:        list[list[float]] = Field(description="Diamagnetic contribution")
    SPSO:        list[list[float]] = Field(description="Paramagnetic contribution")
    STot:        list[list[float]] = Field(description="Total tensor")
    orientation: list[list[float]] = Field(description="Eigenvectors")
    sTotEigen:   list[list[float]] = Field(description="Eigenvalues")
    siso:        list[float]
    saniso:      list[float]


class AUTOCI_Chemical_Shift(Chemical_Shift_Base):
    pass


class CASSCF_Chemical_Shift(Chemical_Shift_Base):
    pass


class CIS_Chemical_Shift(Chemical_Shift_Base):
    pass


class ICE_Chemical_Shift(Chemical_Shift_Base):
    pass


class MCRPA_Chemical_Shift(Chemical_Shift_Base):
    pass


class MDCI_Chemical_Shift(Chemical_Shift_Base):
    pass


class MP2_Chemical_Shift(Chemical_Shift_Base):
    pass


class MRCI_Chemical_Shift(Chemical_Shift_Base):
    pass


class RASCI_Chemical_Shift(Chemical_Shift_Base):

    d_raw:          list[float]
    d_eigenvalues:  list[float]
    d_eigenvectors: list[float]
    D:              float
    E:              float


class ROCIS_Chemical_Shift(Chemical_Shift_Base):
    pass


class RPA_Chemical_Shift(Chemical_Shift_Base):
    pass


class SCF_Chemical_Shift(Chemical_Shift_Base):
    pass


class Chemical_Shift(BaseModel):

    AUTOCI: AUTOCI_Chemical_Shift | None
    CASSCF: CASSCF_Chemical_Shift | None
    CIS:    CIS_Chemical_Shift | None
    ICE:    ICE_Chemical_Shift | None
    MCRPA:  MCRPA_Chemical_Shift | None
    MDCI:   MDCI_Chemical_Shift | None
    MP2:    MP2_Chemical_Shift | None
    MRCI:   MRCI_Chemical_Shift | None
    RASCI:  RASCI_Chemical_Shift | None
    ROCIS:  ROCIS_Chemical_Shift | None
    RPA:    RPA_Chemical_Shift | None
    SCF:    SCF_Chemical_Shift | None
