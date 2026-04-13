from pydantic import BaseModel, Field


class EFG_Tensor_Base(BaseModel):

    numOfNucs:               int = Field(description="Number of active nuclei")
    Method:                  str
    Level:                   str
    Mult:                    int
    State:                   int
    Irrep:                   int
    NUC:                     list[int]         = Field(description="Index of the nuclei")
    Elems:                   list[int]         = Field(description="Atomic number of the nuclei")
    Isotope:                 list[float]       = Field(description="Atomic mass")
    I:                       list[float]       = Field(description="Spin of the nuclei")
    QFAC:                    list[float]       = Field(description="Prefactor")
    V:                       list[list[float]] = Field(description="Raw tensor")
    VEigenvalues:            list[list[float]] = Field(description="Eigenvalues")
    orientation:             list[list[float]] = Field(description="Eigenvectors")
    VIso:                    list[float]


class CASSCF_EFG_Tensor(EFG_Tensor_Base):
    pass


class CIS_EFG_Tensor(EFG_Tensor_Base):
    pass


class ICE_EFG_Tensor(EFG_Tensor_Base):
    pass


class MCRPA_EFG_Tensor(EFG_Tensor_Base):
    pass


class MDCI_EFG_Tensor(EFG_Tensor_Base):
    pass


class MP2_EFG_Tensor(EFG_Tensor_Base):
    pass


class MRCI_EFG_Tensor(EFG_Tensor_Base):
    pass


class RASCI_EFG_Tensor(EFG_Tensor_Base):
    pass


class ROCIS_EFG_Tensor(EFG_Tensor_Base):
    pass


class RPA_EFG_Tensor(EFG_Tensor_Base):
    pass


class SCF_EFG_Tensor(EFG_Tensor_Base):
    pass


class EFG_Tensor(BaseModel):

    CASSCF:        CASSCF_EFG_Tensor
    CIS:           CIS_EFG_Tensor
    ICE:           ICE_EFG_Tensor
    MCRPA:         MCRPA_EFG_Tensor
    MDCI:          MDCI_EFG_Tensor
    MP2:           MP2_EFG_Tensor
    MRCI:          MRCI_EFG_Tensor
    RASCI:         RASCI_EFG_Tensor
    ROCIS:         ROCIS_EFG_Tensor
    RPA:           RPA_EFG_Tensor
    SCF:           SCF_EFG_Tensor