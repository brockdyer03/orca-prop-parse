from pydantic import BaseModel, Field


class Quadrupole_Moment_Base(BaseModel):

    isotropicQuadMoment: float
    quadElecContrib:     list[float] = Field(description="Electronic contribution.  Order: XX, YY, ZZ, XY, XZ, YZ")
    quadNucContrib:      list[float] = Field(description="Nuclear contribution.  Order: XX, YY, ZZ, XY, XZ, YZ")
    quadTotal:           list[float] = Field(description="Total.  Order: XX, YY, ZZ, XY, XZ, YZ")
    quadDiagonalized:    list[float] = Field(description="The diagonalized tensor")
    doAtomicQuad:        bool
    atomicQuad:          list[float] | None = Field(description="Atomic quadrupoles (NAtoms * XX, YY, ZZ, XY, XZ, YZ)")
    Method:              str
    Level:               str
    Mult:                int
    State:               int
    Irrep:               int


class AutoCI_Quadrupole_Moment(Quadrupole_Moment_Base):
    pass


class CASSCF_Quadrupole_Moment(Quadrupole_Moment_Base):
    pass


class CIS_Quadrupole_Moment(Quadrupole_Moment_Base):
    pass


class ICE_Quadrupole_Moment(Quadrupole_Moment_Base):
    pass


class MCRPA_Quadrupole_Moment(Quadrupole_Moment_Base):
    pass


class MDCI_Quadrupole_Moment(Quadrupole_Moment_Base):
    pass


class MP2_Quadrupole_Moment(Quadrupole_Moment_Base):
    pass


class MRCI_Quadrupole_Moment(Quadrupole_Moment_Base):
    pass


class RASCI_Quadrupole_Moment(Quadrupole_Moment_Base):
    pass


class ROCIS_Quadrupole_Moment(Quadrupole_Moment_Base):
    pass


class RPA_Quadrupole_Moment(Quadrupole_Moment_Base):
    pass


class SCF_Quadrupole_Moment(Quadrupole_Moment_Base):
    pass


class Quadrupole_Moment(BaseModel):

    AutoCI: AutoCI_Quadrupole_Moment | None
    CASSCF: CASSCF_Quadrupole_Moment | None
    CIS:    CIS_Quadrupole_Moment | None
    ICE:    ICE_Quadrupole_Moment | None
    MCRPA:  MCRPA_Quadrupole_Moment | None
    MDCI:   MDCI_Quadrupole_Moment | None
    MP2:    MP2_Quadrupole_Moment | None
    MRCI:   MRCI_Quadrupole_Moment | None
    RASCI:  RASCI_Quadrupole_Moment | None
    ROCIS:  ROCIS_Quadrupole_Moment | None
    RPA:    RPA_Quadrupole_Moment | None
    SCF:    SCF_Quadrupole_Moment | None
