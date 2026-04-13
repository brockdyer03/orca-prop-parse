from pydantic import BaseModel, Field


class Broken_Symmetry(BaseModel):

    enHighSpin:  float = Field(description="The High Spin Energy")
    enBrokenSym: float = Field(description="The Broken Symmetry Energy")
    SHighSpin:   float = Field(description="The High Spin Spin")
    S2HighSpin:  float = Field(description="The Expectation value of S**2 for the High Spin case")
    S2BrokenSym: float = Field(description="The Expectation value of S**2 for the Broken symmetry case")
