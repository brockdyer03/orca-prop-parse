from pydantic import BaseModel, Field


class D_Tensor_Base(BaseModel):

    d_raw:          list[float]
    d_eigenvalues:  list[float]
    d_eigenvectors: list[float]
    D:              float
    E:              float
    Method:         str
    Level:          str
    Mult:           int
    State:          int
    Irrep:          int


class AutoCI_D_Tensor(D_Tensor_Base):
    pass


class CASSCF_D_Tensor(D_Tensor_Base):
    pass


class CASSCF_2ndOrder_D_Tensor(D_Tensor_Base):
    pass


class CASSCF_2ndOrder_ES_D_Tensor(D_Tensor_Base):
    pass


class CASSCF_Heff_D_Tensor(D_Tensor_Base):
    pass


class CASSCF_Heff_ES_D_Tensor(D_Tensor_Base):
    pass


class NEVPT2_2ndOrder_D_Tensor(D_Tensor_Base):
    pass


class NEVPT2_2ndOrder_ES_D_Tensor(D_Tensor_Base):
    pass


class NEVPT2_Heff_D_Tensor(D_Tensor_Base):
    pass


class NEVPT2_Heff_ES_D_Tensor(D_Tensor_Base):
    pass


class CUSTOM_2ndOrder_D_Tensor(D_Tensor_Base):
    pass


class CUSTOM_2ndOrder_ES_D_Tensor(D_Tensor_Base):
    pass


class CUSTOM_Heff_D_Tensor(D_Tensor_Base):
    pass


class CUSTOM_Heff_ES_D_Tensor(D_Tensor_Base):
    pass


class CIS_D_Tensor(D_Tensor_Base):
    pass


class ICE_D_Tensor(D_Tensor_Base):
    pass


class MCRPA_D_Tensor(D_Tensor_Base):
    pass


class MDCI_D_Tensor(D_Tensor_Base):
    pass


class MP2_D_Tensor(D_Tensor_Base):
    pass


class MRCI_D_Tensor(D_Tensor_Base):
    pass


class MRCI_2ndOrder_D_Tensor(D_Tensor_Base):
    pass


class MRCI_2ndOrder_ES_D_Tensor(D_Tensor_Base):
    pass


class MRCI_Heff_D_Tensor(D_Tensor_Base):
    pass


class MRCI_Heff_ES_D_Tensor(D_Tensor_Base):
    pass


class RASCI_D_Tensor(D_Tensor_Base):
    pass


class ROCIS_D_Tensor(D_Tensor_Base):
    pass


class RPA_D_Tensor(D_Tensor_Base):
    pass


class SCF_D_Tensor(D_Tensor_Base):
    pass


class D_Tensor(BaseModel):

    AutoCI:             AutoCI_D_Tensor
    CASSCF:             CASSCF_D_Tensor
    CASSCF_2ndOrder:    CASSCF_2ndOrder_D_Tensor
    CASSCF_2ndOrder_ES: CASSCF_2ndOrder_ES_D_Tensor
    CASSCF_Heff:        CASSCF_Heff_D_Tensor
    CASSCF_Heff_ES:     CASSCF_Heff_ES_D_Tensor
    NEVPT2_2ndOrder:    NEVPT2_2ndOrder_D_Tensor
    NEVPT2_2ndOrder_ES: NEVPT2_2ndOrder_ES_D_Tensor
    NEVPT2_Heff:        NEVPT2_Heff_D_Tensor
    NEVPT2_Heff_ES:     NEVPT2_Heff_ES_D_Tensor
    CUSTOM_2ndOrder:    CUSTOM_2ndOrder_D_Tensor
    CUSTOM_2ndOrder_ES: CUSTOM_2ndOrder_ES_D_Tensor
    CUSTOM_Heff:        CUSTOM_Heff_D_Tensor
    CUSTOM_Heff_ES:     CUSTOM_Heff_ES_D_Tensor
    CIS:                CIS_D_Tensor
    ICE:                ICE_D_Tensor
    MCRPA:              MCRPA_D_Tensor
    MDCI:               MDCI_D_Tensor
    MP2:                MP2_D_Tensor
    MRCI:               MRCI_D_Tensor
    MRCI_2ndOrder:      MRCI_2ndOrder_D_Tensor
    MRCI_2ndOrder_ES:   MRCI_2ndOrder_ES_D_Tensor
    MRCI_Heff:          MRCI_Heff_D_Tensor
    MRCI_Heff_ES:       MRCI_Heff_ES_D_Tensor
    RASCI:              RASCI_D_Tensor
    ROCIS:              ROCIS_D_Tensor
    RPA:                RPA_D_Tensor
    SCF:                SCF_D_Tensor
