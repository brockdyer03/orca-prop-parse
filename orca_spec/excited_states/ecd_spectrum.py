from pydantic import BaseModel, Field


class ECD_Spectrum_Base(BaseModel):

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


class AutoCI_ECD_Spectrum(ECD_Spectrum_Base):
    pass


class AutoCI_MRCI_ECD_Spectrum(ECD_Spectrum_Base):
    pass


class CASSCF_ECD_Spectrum(ECD_Spectrum_Base):
    pass


class CASSCF_PT_ECD_Spectrum(ECD_Spectrum_Base):
    pass


class CASSCF_QDPT_ECD_Spectrum(ECD_Spectrum_Base):
    pass


class CASSCF_DCD_ECD_Spectrum(ECD_Spectrum_Base):
    pass


class CASSCF_Custom_ECD_Spectrum(ECD_Spectrum_Base):
    pass


class CIS_ECD_Spectrum(ECD_Spectrum_Base):
    pass


class ICE_ECD_Spectrum(ECD_Spectrum_Base):
    pass


class LFT_ECD_Spectrum(ECD_Spectrum_Base):
    pass


class MCRPA_ECD_Spectrum(ECD_Spectrum_Base):
    pass


class MDCI_ECD_Spectrum(ECD_Spectrum_Base):
    pass


class MP2_ECD_Spectrum(ECD_Spectrum_Base):
    pass


class MRCI_ECD_Spectrum(ECD_Spectrum_Base):
    pass


class RASCI_ECD_Spectrum(ECD_Spectrum_Base):
    pass


class ROCIS_ECD_Spectrum(ECD_Spectrum_Base):
    pass


class RPA_ECD_Spectrum(ECD_Spectrum_Base):
    pass


class SCF_ECD_Spectrum(ECD_Spectrum_Base):
    pass


class ECD_Spectrum(BaseModel):

    AutoCI:        AutoCI_ECD_Spectrum
    AutoCI_MRCI:   AutoCI_MRCI_ECD_Spectrum
    CASSCF:        CASSCF_ECD_Spectrum
    CASSCF_PT:     CASSCF_PT_ECD_Spectrum
    CASSCF_QDPT:   CASSCF_QDPT_ECD_Spectrum
    CASSCF_DCD:    CASSCF_DCD_ECD_Spectrum
    CASSCF_Custom: CASSCF_Custom_ECD_Spectrum
    CIS:           CIS_ECD_Spectrum
    ICE:           ICE_ECD_Spectrum
    LFT:           LFT_ECD_Spectrum
    MCRPA:         MCRPA_ECD_Spectrum
    MDCI:          MDCI_ECD_Spectrum
    MP2:           MP2_ECD_Spectrum
    MRCI:          MRCI_ECD_Spectrum
    RASCI:         RASCI_ECD_Spectrum
    ROCIS:         ROCIS_ECD_Spectrum
    RPA:           RPA_ECD_Spectrum
    SCF:           SCF_ECD_Spectrum