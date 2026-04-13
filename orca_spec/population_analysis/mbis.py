from pydantic import BaseModel, Field


class MBIS(BaseModel):

    NAtoms:            int
    ATNO:              list[int]
    Thresh:            float
    Niter:             int
    LargePrint:        bool
    DENSA:             float = Field(description="Total integrated alpha density")
    DENSB:             float = Field(description="Total integrated beta density")
    AtomicCharges:     list[float]
    Spin:              list[float]
    NPOPVAL:           list[float]
    SIGMAVAL:          list[float]
    AtomicDipole:      list[float] | None
    AtomicQuadrupole:  list[float] | None
    AtomicOctupole:    list[float] | None
    ThirdRadialMoment: list[float] | None
    Method:            str
    Level:             str
    Mult:              int
    State:             int
    Irrep:             int
