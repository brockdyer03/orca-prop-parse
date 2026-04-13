from pydantic import BaseModel, Field


class Dipole_Moment_Base(BaseModel):

    dipoleMagnitude:   float
    dipoleElecContrib: list[float] = Field(description="Electronic contribution")
    dipoleNucContrib:  list[float] = Field(description="Nuclear contribution")
    dipoleTotal:       list[float] = Field(description="Total")
    doAtomicDipole:    bool
    atomicDipole:      list[float] | None = Field(description="Atomic dipoles (NAtoms * X,Y,Z)")
    Method:            str
    Level:             str
    Mult:              int
    State:             int
    Irrep:             int


class AutoCI_Dipole_Moment(Dipole_Moment_Base):
    pass


class CASSCF_Dipole_Moment(Dipole_Moment_Base):
    pass


class CIS_Dipole_Moment(Dipole_Moment_Base):
    pass


class ICE_Dipole_Moment(Dipole_Moment_Base):
    pass


class MCRPA_Dipole_Moment(Dipole_Moment_Base):
    pass


class MDCI_Dipole_Moment(Dipole_Moment_Base):
    pass


class MP2_Dipole_Moment(Dipole_Moment_Base):
    pass


class MRCI_Dipole_Moment(Dipole_Moment_Base):
    pass


class RASCI_Dipole_Moment(Dipole_Moment_Base):
    pass


class ROCIS_Dipole_Moment(Dipole_Moment_Base):
    pass


class RPA_Dipole_Moment(Dipole_Moment_Base):
    pass


class SCF_Dipole_Moment(Dipole_Moment_Base):
    pass


class CASPT2_Dipole_Moment(Dipole_Moment_Base):
    pass


class CAS_CUSTOM_Dipole_Moment(Dipole_Moment_Base):
    pass


class DipoleMoment(BaseModel):

    AutoCI:     AutoCI_Dipole_Moment | None
    CASSCF:     CASSCF_Dipole_Moment | None
    CIS:        CIS_Dipole_Moment | None
    ICE:        ICE_Dipole_Moment | None
    MCRPA:      MCRPA_Dipole_Moment | None
    MDCI:       MDCI_Dipole_Moment | None
    MP2:        MP2_Dipole_Moment | None
    MRCI:       MRCI_Dipole_Moment | None
    RASCI:      RASCI_Dipole_Moment | None
    ROCIS:      ROCIS_Dipole_Moment | None
    RPA:        RPA_Dipole_Moment | None
    SCF:        SCF_Dipole_Moment | None
    CASPT2:     CASPT2_Dipole_Moment | None
    CAS_CUSTOM: CAS_CUSTOM_Dipole_Moment | None
