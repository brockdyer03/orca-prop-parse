from pydantic import BaseModel


class CIPSI_Energies(BaseModel):

    finalEnergy:  float
    numOfRoots:   int
    multiplicity: int
    energies:     list[float]