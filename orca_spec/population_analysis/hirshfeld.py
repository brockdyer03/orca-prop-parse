from pydantic import BaseModel, Field


class Hirshfeld(BaseModel):

    NAtoms:        int
    ATNO:          list[int]
    DENSA:         float = Field(description="Total integrated alpha density")
    DENSB:         float = Field(description="Total integrated beta density")
    AtomicCharges: list[float]
    Spin:          list[float]
    Method:        str
    Level:         str
    Mult:          int
    State:         int
    Irrep:         int
