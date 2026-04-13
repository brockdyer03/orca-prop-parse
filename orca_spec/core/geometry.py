from pydantic import BaseModel, Field


class Geometry(BaseModel):

    NAtoms:       int
    NCorelessECP: int
    NGhostAtoms:  int
    Coordinates:  list[str, float, float, float]
    ATNO:         list[int]
    coreless_ECP: list[int] | None = Field(description="Non-zero for cECPs")
    ghostAtoms:   list[int] | None = Field(description="Non-zero for ghost atoms")
    fragments:    list[int] | None = Field(description="Fragment ID")
