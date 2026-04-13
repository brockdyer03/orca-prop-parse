from pydantic import BaseModel, Field


class G_Tensor_Base(BaseModel):

    g_matrix:    list[float]
    g_elec:      float = Field(description="The free electron g-value contribution")
    g_RMC:       float = Field(description="The reduced mass correction")
    g_DSO:       list[float]
    g_PSO:       list[float]
    g_Tot:       list[float]
    g_iso:       float
    Delta_g:     list[float]
    Delta_g_iso: float
    orientation: list[float]
    Method:      str
    Level:       str
    Mult:        int
    State:       int
    Irrep:       int


class AutoCI_G_Tensor(G_Tensor_Base):
    pass


class CASSCF_G_Tensor(G_Tensor_Base):
    pass


class CASSCF_2ndOrder_G_Tensor(G_Tensor_Base):
    pass


class CASSCF_Heff_G_Tensor(G_Tensor_Base):
    pass


class NEVPT2_2ndOrder_G_Tensor(G_Tensor_Base):
    pass


class NEVPT2_Heff_G_Tensor(G_Tensor_Base):
    pass


class CUSTOM_2ndOrder_G_Tensor(G_Tensor_Base):
    pass


class CUSTOM_Heff_G_Tensor(G_Tensor_Base):
    pass


class CIS_G_Tensor(G_Tensor_Base):
    pass


class ICE_G_Tensor(G_Tensor_Base):
    pass


class MCRPA_G_Tensor(G_Tensor_Base):
    pass


class MDCI_G_Tensor(G_Tensor_Base):
    pass


class MP2_G_Tensor(G_Tensor_Base):
    pass


class MRCI_G_Tensor(G_Tensor_Base):
    pass


class RASCI_G_Tensor(G_Tensor_Base):
    pass


class ROCIS_G_Tensor(G_Tensor_Base):
    pass


class RPA_G_Tensor(G_Tensor_Base):
    pass


class SCF_G_Tensor(G_Tensor_Base):
    pass


class CASPT2_G_Tensor(G_Tensor_Base):
    pass



class G_Tensor(BaseModel):

    AutoCI:          AutoCI_G_Tensor | None
    CASSCF:          CASSCF_G_Tensor | None
    CASSCF_2ndOrder: CASSCF_2ndOrder_G_Tensor | None
    CASSCF_Heff:     CASSCF_Heff_G_Tensor | None
    NEVPT2_2ndOrder: NEVPT2_2ndOrder_G_Tensor | None
    NEVPT2_Heff:     NEVPT2_Heff_G_Tensor | None
    CUSTOM_2ndOrder: CUSTOM_2ndOrder_G_Tensor | None
    CUSTOM_Heff:     CUSTOM_Heff_G_Tensor | None
    CIS:             CIS_G_Tensor | None
    ICE:             ICE_G_Tensor | None
    MCRPA:           MCRPA_G_Tensor | None
    MDCI:            MDCI_G_Tensor | None
    MP2:             MP2_G_Tensor | None
    MRCI:            MRCI_G_Tensor | None
    RASCI:           RASCI_G_Tensor | None
    ROCIS:           ROCIS_G_Tensor | None
    RPA:             RPA_G_Tensor | None
    SCF:             SCF_G_Tensor | None
    CASPT2:          CASPT2_G_Tensor | None
