from pydantic import BaseModel


class Thermochemistry_Energies(BaseModel):

    temperature:       float
    pressure:          float
    totalMass:         float
    spinDegeneracy:    int
    elEnergy:          float
    transEnergy:       float
    rotEnergy:         float
    vibEnergy:         float
    numOfFreqs:        int
    freqScalingFactor: float
    FREQ:              list[float]
    zpe:               float
    innerEnergyU:      float
    enthalpyH:         float
    qEl:               float
    qRot:              float
    qVib:              float
    qTrans:            float
    entropyS:          float
    freeEnergyG:       float
    isLinear:          bool
