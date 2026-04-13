from pydantic import BaseModel, Field


class MDCI_EOM_Energies(BaseModel):

    groundRefEnergy:   float = Field(description="Ground State Reference Energy")
    groundCorrEnergy:  float = Field(description="Ground State Correlation Energy")
    groundTotalEnergy: float = Field(description="Ground State Total MDCI Energy")
