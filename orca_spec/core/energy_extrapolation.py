from pydantic import BaseModel, Field


class Energy_Extrapolation(BaseModel):

    doEp1:           bool = Field(description="Extrapolation using only one method")
    doEp2:           bool = Field(description="Extrapolation using two different methods (same small basis Set)")
    doEp3:           bool = Field(description="Extrapolation using two different methods (use three basis Sets for the cheap method)")
    doGradients:     bool = Field(description="Extrapolate energy gradients")
    scfEnergies:     list[float]
    scfCBS:          float
    scfGradients:    list[float] | None = Field(description="The SCF Gradients")
    corrEnergies:    list[float]
    corrCBS:         float
    ccsdtEnergyX:    float | None
    totalCBS:        float
    cardinalNumbers: list[int]
    alphas:          list[float]
    betas:           list[float]
    numOfEnergies:   int = Field(description="How many energies we are going to use (e.g. two-point scheme).")
    basisName:       list[str]
