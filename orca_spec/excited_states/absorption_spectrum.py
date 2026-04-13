from pydantic import BaseModel, Field


class Absorption_Spectrum_Base(BaseModel):

    Method:             int
    RelCorrection:      int = Field(description="Type of relativistic treatment in QDPT. 0->Unknow, 1->None, 2->SOC, 3->SSC, 4->SOC/SSC")
    DensType:           int = Field(description="Type of density (electron/spin …). 0->Unknow, 1->Electronic, 2->Spin, 3->Trans/Electronic, 4->Tran/Spin")
    DeriType:           int = Field(description="Type of derivative (w.r.t. to what perturbation). 0->Unknown, 1->No Derivative, 2->Electric/Dipole, 3->Electric/Quad, 4->Magnetic/Dipole, 5->Magnetic/Quad")
    DensLevel:          int = Field(description="// Source of density: relaxed, unrelaxed, … 0->Unknown, 1->Linearized, 2->Unrelaxed, 3->Relaxed")
    Density_name:       str
    Representation:     str = Field(description="Possible values: Unknown,  Length, Velocity")
    PointGroup:         str
    DoHigherMoments:    bool
    NTrans:             int
    ExcitationEnergies: list[float]
    States:             list[int] = Field(description="The initial and Final states. Col1: Initial State  Col2: Initial Irrep Col3: Final State Col4: Final Irrep")
    Multiplicities:     list[float] = Field(description="Col1: Multiplicity of the initial state  Col2: Multiplicity of the final state")
    Temperature:        float


class AutoCI_Absorption_Spectrum(Absorption_Spectrum_Base):
    pass


class AutoCI_MRCI_Absorption_Spectrum(Absorption_Spectrum_Base):
    pass


class CASSCF_Absorption_Spectrum(Absorption_Spectrum_Base):
    pass


class CASSCF_PT_Absorption_Spectrum(Absorption_Spectrum_Base):
    pass


class CASSCF_QDPT_Absorption_Spectrum(Absorption_Spectrum_Base):
    pass


class CASSCF_DCD_Absorption_Spectrum(Absorption_Spectrum_Base):
    pass


class CASSCF_PT_Energies_Absorption_Spectrum(Absorption_Spectrum_Base):
    pass


class CASSCF_Custom_Absorption_Spectrum(Absorption_Spectrum_Base):
    pass


class CIS_Absorption_Spectrum(Absorption_Spectrum_Base):
    pass


class ICE_Absorption_Spectrum(Absorption_Spectrum_Base):
    pass


class LFT_Absorption_Spectrum(Absorption_Spectrum_Base):
    pass


class MCRPA_Absorption_Spectrum(Absorption_Spectrum_Base):
    pass


class MDCI_Absorption_Spectrum(Absorption_Spectrum_Base):
    pass


class MP2_Absorption_Spectrum(Absorption_Spectrum_Base):
    pass


class MRCI_Absorption_Spectrum(Absorption_Spectrum_Base):
    pass


class RASCI_Absorption_Spectrum(Absorption_Spectrum_Base):
    pass


class ROCIS_Absorption_Spectrum(Absorption_Spectrum_Base):
    pass


class RPA_Absorption_Spectrum(Absorption_Spectrum_Base):
    pass


class SCF_Absorption_Spectrum(Absorption_Spectrum_Base):
    pass


class Absorption_Spectrum(BaseModel):

    AutoCI:             AutoCI_Absorption_Spectrum
    AutoCI_MRCI:        AutoCI_MRCI_Absorption_Spectrum
    CASSCF:             CASSCF_Absorption_Spectrum
    CASSCF_PT:          CASSCF_PT_Absorption_Spectrum
    CASSCF_QDPT:        CASSCF_QDPT_Absorption_Spectrum
    CASSCF_DCD:         CASSCF_DCD_Absorption_Spectrum
    CASSCF_PT_Energies: CASSCF_PT_Energies_Absorption_Spectrum
    CASSCF_Custom:      CASSCF_Custom_Absorption_Spectrum
    CIS:                CIS_Absorption_Spectrum
    ICE:                ICE_Absorption_Spectrum
    LFT:                LFT_Absorption_Spectrum
    MCRPA:              MCRPA_Absorption_Spectrum
    MDCI:               MDCI_Absorption_Spectrum
    MP2:                MP2_Absorption_Spectrum
    MRCI:               MRCI_Absorption_Spectrum
    RASCI:              RASCI_Absorption_Spectrum
    ROCIS:              ROCIS_Absorption_Spectrum
    RPA:                RPA_Absorption_Spectrum
    SCF:                SCF_Absorption_Spectrum