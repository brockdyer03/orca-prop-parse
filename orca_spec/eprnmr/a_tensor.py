from pydantic import BaseModel, Field


class A_Tensor_Base(BaseModel):

    numOfNucs:               int = Field(description="Number of active nuclei")
    Method:                  str
    Level:                   str
    Mult:                    int
    State:                   int
    Irrep:                   int
    NUC:                     list[int]         = Field(description="Index of the nuclei")
    Elem:                    list[int]         = Field(description="Atomic number of the nuclei")
    Isotope:                 list[float]       = Field(description="Atomic mass")
    I:                       list[float]       = Field(description="Spin of the nuclei")
    PFAC:                    list[float]       = Field(description="Prefactor PFAC=gegNbe*bN (in MHz)")
    ARaw:                    list[list[float]] = Field(description="Raw tensor")
    AEigenvalues:            list[list[float]] = Field(description="Eigenvalues")
    orientation:             list[list[float]] = Field(description="Eigenvectors")
    AIso:                    list[float]


class AutoCI_A_Tensor(A_Tensor_Base):
    pass


class CASSCF_A_Tensor(A_Tensor_Base):
    pass


class CIS_A_Tensor(A_Tensor_Base):
    pass


class ICE_A_Tensor(A_Tensor_Base):
    pass


class MCRPA_A_Tensor(A_Tensor_Base):
    pass


class MDCI_A_Tensor(A_Tensor_Base):
    pass


class MP2_A_Tensor(A_Tensor_Base):
    pass


class MRCI_A_Tensor(A_Tensor_Base):
    pass


class RASCI_A_Tensor(A_Tensor_Base):
    pass


class ROCIS_A_Tensor(A_Tensor_Base):
    pass


class RPA_A_Tensor(A_Tensor_Base):
    pass


class SCF_A_Tensor(A_Tensor_Base):
    pass


class A_Tensor(BaseModel):

    AutoCI:        AutoCI_A_Tensor
    CASSCF:        CASSCF_A_Tensor
    CIS:           CIS_A_Tensor
    ICE:           ICE_A_Tensor
    MCRPA:         MCRPA_A_Tensor
    MDCI:          MDCI_A_Tensor
    MP2:           MP2_A_Tensor
    MRCI:          MRCI_A_Tensor
    RASCI:         RASCI_A_Tensor
    ROCIS:         ROCIS_A_Tensor
    RPA:           RPA_A_Tensor
    SCF:           SCF_A_Tensor