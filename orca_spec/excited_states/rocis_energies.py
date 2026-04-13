from pydantic import BaseModel, Field


class ROCIS_Energies(BaseModel):

    refEnergy:      float
    corrEnergy:     float
    totalEnergy:    float
    numOfRoots:     int
    Energies:       list[float] = Field(description="State energies in Hartree")
    Multiplicities: list[int]
