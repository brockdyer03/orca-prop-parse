from pydantic import BaseModel, Field


class Single_Point_Data(BaseModel):

    FinalEnergy: float = Field(description="Final single point energy")
    Converged:   bool
