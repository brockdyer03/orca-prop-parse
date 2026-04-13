from pydantic import BaseModel, Field


class DFT_Energy(BaseModel):

    nAlphaEl:  int
    nBetaEl:   int
    nTotalEl:  int
    finalEn:   float = Field(description="No Van der Waals correction")
    eExchange: float
    eCorr:     float
    eXC:       float
    eCNL:      float
    eEmbed:    float | None
