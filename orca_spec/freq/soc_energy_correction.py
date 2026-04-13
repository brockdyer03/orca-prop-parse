from pydantic import BaseModel


class SOC_Energy_Correction(BaseModel):

    total_SOC_energy:     float
    total_non_SOC_energy: float
    nuclear_energy:       float
    SOC_correction:       float
