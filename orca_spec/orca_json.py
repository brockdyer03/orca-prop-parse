from pydantic import BaseModel
from .core import (
    Broken_Symmetry,
    CIPSI_Energies,
    DFT_Energy,
    Energy_Extrapolation,
    Energy,
    gCP_Energy,
    Geometry,
    MDCI_LED,
    Natural_Orbitals,
    Nuclear_Gradient,
    Solvation_Details,
    VdW_Correction,
)
from .elprop import (
    DipoleMoment,
    Quadrupole_Moment,
    Polarizability,
    Hyperpolarizability,
)
from .eprnmr import (
    A_Tensor,
    D_Tensor,
    G_Tensor,
    EFG_Tensor,
    Spin_Spin_Coupling,
    Chemical_Shift,
)
from .excited_states import (
    Absorption_Spectrum,
    ECD_Spectrum,
    Excited_States_Dynamics,
    MDCI_EOM_Energies,
    ROCIS_Energies,
    STEOM,
)
from .freq import (
    DBOC_Energy,
    SOC_Energy_Correction,
    Hessian,
    Thermochemistry_Energies,
)
from .population_analysis import (
    CHELPG,
    Hirshfeld,
    Loewdin,
    Mayer,
    MBIS,
    Mulliken,
)


class MainModel(BaseModel):

    ...
