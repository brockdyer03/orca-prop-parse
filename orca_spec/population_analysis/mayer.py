from pydantic import BaseModel, Field


class Mayer(BaseModel):

    NAtoms:           int = Field(description="Total number of atoms")
    NBondOrdersPrint: int = Field(description="The number of bond orders larger than threshold")
    bondThresh:       float = Field(description="The threshold for printing")
    components:       list[int] | None = Field(description="The indices and atomic numbers of the bonding atoms")
    BondOrders:       list[float] | None = Field(description="The bond orders")
    ATNO:             list[int] = Field(description="Atomic number of the elements")
    NA:               list[float] = Field(description="Mulliken gross atomic population")
    ZA:               list[float] = Field(description="Total nuclear charge")
    QA:               list[float] = Field(description="Mulliken gross atomic charge")
    VA:               list[float] = Field(description="Mayer's total valence")
    BVA:              list[float] = Field(description="Mayer's bonded valence")
    FA:               list[float] = Field(description="Mayer's free valence")
    Method:           str
    Level:            str
    Mult:             int
    State:            int
    Irrep:            int
