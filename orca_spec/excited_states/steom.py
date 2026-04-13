from pydantic import BaseModel, Field


class STEOM(BaseModel):

    S2:                        list[float] = Field(description="<S**2>")
    PercentageActiveCharacter: list[float]
    Method:                    str
    excitationEnergies:        list[float]        = Field(description="Total energy of each state")
    Mult:                      list[int]   | None = Field(description="Multiplicity of each state")
    Irrep:                     list[int]   | None = Field(description="Irreducible representation of each state")
    RelCorr:                   str         | None = Field(description="Relativistic correction (SOC and/or SSC)")
    NBlocks:                   int         | None = Field(description="Number of multiplicity blocks")
    NRoots:                    list[int]   | None = Field(description="Number of roots in each block")
    NTotalRoots:               int         | None = Field(description="Total number of roots")
    Block:                     list[int]   | None = Field(description="Block index of each state")
    Root:                      list[int]   | None = Field(description="Root index within the block")
    FollowIRoot:               int         | None = Field(description="Index of the followed root")
    AvgMult:                   list[float] | None = Field(description="Average multiplicity of each SO-/SS-coupled state")
