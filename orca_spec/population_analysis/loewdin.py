from pydantic import BaseModel


class Loewdin(BaseModel):

    NAtoms:        int
    ATNO:          list[int]
    AtomicCharges: list[float]
    Method:        str
    Level:         str
    Mult:          int
    State:         int
    Irrep:         int
