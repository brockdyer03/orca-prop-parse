from pydantic import BaseModel, Field


class Natural_Orbitals(BaseModel):

    NEL:       int
    NSOMO:     int
    NDOMO:     int
    NVMO:      int
    NNatoOrbs: int
    OccUno:    list[float] = Field(description="Occupation  of natural orbitals")
    OccUnso:   list[float] = Field(description="Occupation of spin natural orbitals")
