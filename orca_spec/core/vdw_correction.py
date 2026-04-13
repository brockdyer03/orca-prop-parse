from pydantic import BaseModel


class VdW_Correction(BaseModel):

    vdW:        float
    vdW_atomic: list[float] | None
