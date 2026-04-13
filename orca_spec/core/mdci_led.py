from pydantic import BaseModel, Field


class MDCI_LED(BaseModel):

    numOfFragments:  int         = Field(description="The number of fragments")
    sumNonDisStrong: float       = Field(description="Sum of non dispersive correlation strong pairs")
    sumNonDisWeak:   float       = Field(description="Sum of non dispersive correlation weak pairs")
    electrostRef:    list[float] = Field(description="Electrostatics reference")
    exchangeRef:     list[float] = Field(description="Exchange reference")
    dispContr:       list[float] = Field(description="Strong pair dispersion contribution")
    dispWeak:        list[float] = Field(description="Weak pair dispersion contribution")
    refInt:          list[float] = Field(description="Interaction reference")
    corrInt:         list[float] = Field(description="Interaction correlation")
    totInt:          list[float] = Field(description="Interaction total")
