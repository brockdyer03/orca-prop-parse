from pydantic import BaseModel


class Solvation_Details(BaseModel):

    Solvent:        str
    Epsilon:        float
    Refrac:         float
    RSolv:          float
    SurfaceType:    str
    CPCMDielEnergy: float
    NPoints:        int
    SurfaceArea:    float
