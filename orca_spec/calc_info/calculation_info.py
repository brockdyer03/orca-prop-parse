from pydantic import BaseModel


class Calculation_Info(BaseModel):

    Mult:                  int
    Charge:                int
    NumOfAtoms:            int
    NumOfElectrons:        int
    NumOfBasisFuncts:      int
    NumOfAuxCBasisFuncts:  int
    NumOfAuxJBasisFuncts:  int
    NumOfAuxJKBasisFuncts: int
    NumOfCABSBasisFuncts:  int
