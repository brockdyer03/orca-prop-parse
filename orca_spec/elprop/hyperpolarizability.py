from pydantic import BaseModel


class Hyperpolarizability(BaseModel):

    rawCartesian: list[float]
    Method:       str
    Level:        str
    Mult:         int
    State:        int
    Irrep:        int
