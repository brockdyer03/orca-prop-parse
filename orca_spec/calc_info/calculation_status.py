from pydantic import BaseModel


class Calculation_Status(BaseModel):

    version:  str
    progName: str
    Status:   str
