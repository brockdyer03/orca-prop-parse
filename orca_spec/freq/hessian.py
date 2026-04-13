from pydantic import BaseModel, Field


class Hessian(BaseModel):

    HESSIAN: list[float] = Field(description="The Hessian")
    MODES:   list[float] = Field(description="The modes of vibrations")
