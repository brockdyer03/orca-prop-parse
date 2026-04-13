from pydantic import BaseModel, Field


class Energy_Base(BaseModel):

    totalEnergy: list[float]        = Field(description="Total energy of each state")
    Mult:        list[int]   | None = Field(description="Multiplicity of each state")
    Irrep:       list[int]   | None = Field(description="Irreducible representation of each state")
    RelCorr:     str         | None = Field(description="Relativistic correction (SOC and/or SSC)")
    NBlocks:     int         | None = Field(description="Number of multiplicity blocks")
    NRoots:      list[int]   | None = Field(description="Number of roots in each block")
    NTotalRoots: int         | None = Field(description="Total number of roots")
    Block:       list[int]   | None = Field(description="Block index of each state")
    Root:        list[int]   | None = Field(description="Root index within the block")
    FollowIRoot: int         | None = Field(description="Index of the followed root")
    AvgMult:     list[float] | None = Field(description="Average multiplicity of each SO-/SS-coupled state")


class AutoCI_Energy(Energy_Base):

    numOfEl:          int
    numOfCorrEl:      int
    numOfAlphaCorrEl: int | None
    numOfBetaCorrEl:  int | None
    refEnergy:        list[float] = Field(description="Reference energy for each state")
    corrEnergy:       list[float] = Field(description="Total correlation energy for each state")


class CAS_DCD_Energy(Energy_Base):

    finalEnergy:      float = Field(description="Final GS or SA energy")
    numOfElectrons:   int
    numOfActiveEl:    int   = Field(description="Number of active electrons")
    numOfActiveOrbs:  int   = Field(description="Number of active orbitals")
    numOfFCElectrons: int


class CAS_MSPT2_Energy(Energy_Base):

    finalEnergy:      float = Field(description="Final GS or SA energy")
    numOfElectrons:   int
    numOfActiveEl:    int   = Field(description="Number of active electrons")
    numOfActiveOrbs:  int   = Field(description="Number of active orbitals")
    numOfFCElectrons: int


class CAS_PT2_Energy(Energy_Base):

    finalEnergy:      float = Field(description="Final GS or SA energy")
    numOfElectrons:   int
    numOfActiveEl:    int   = Field(description="Number of active electrons")
    numOfActiveOrbs:  int   = Field(description="Number of active orbitals")
    numOfFCElectrons: int


class CAS_SCF_Energy(Energy_Base):

    finalEnergy:      float = Field(description="Final GS or SA energy")
    numOfElectrons:   int
    numOfActiveEl:    int   = Field(description="Number of active electrons")
    numOfActiveOrbs:  int   = Field(description="Number of active orbitals")
    numOfFCElectrons: int


class CIS_Energy(Energy_Base):

    e0:     float = Field(description="Ground state energy")
    multP1: bool  = Field(description="Do the higher multiplicity too?")
    mode:   str   = Field(description="CIS mode: CIS, RPA, TDA, TD-DFT, sTDA, sTD-DFT")
    dCorr:  int   = Field(description="(D) Correction algorithm")


class MDCI_Energy(Energy_Base):

    numOfEl:          int
    numOfCorrEl:      int
    numOfAlphaCorrEl: int
    numOfBetaCorrEl:  int
    refEnergy:        list[float]        = Field(description="Reference Energy")
    corrEnergy:       list[float]        = Field(description="Total Correlation Energy")
    aaCorrEn:         list[float]        = Field(description="Alpha-Alpha Pairs Correlation Energy (No (T))")
    bbCorrEn:         list[float]        = Field(description="Beta-Beta Pairs Correlation Energy (No (T))")
    abCorrEn:         list[float]        = Field(description="Alpha-Beta Pairs Correlation Energy (No (T))")
    CorrDS:           list[float] | None = Field(description="Singlet pairs energy of double amplitudes (No (T))")
    CorrDT:           list[float] | None = Field(description="Triplet pairs energy of double amplitudes (No (T))")
    CorrSS:           list[float] | None = Field(description="Singlet pairs energy of quadratic single amplitudes (No (T))")
    CorrST:           list[float] | None = Field(description="Triplet pairs energy of quadratic single amplitudes (No (T))")
    triplesEnergy:    list[float]        = Field(description="Triples Correction Energy")


class MP2_Energy(Energy_Base):

    refEnergy:  list[float] = Field(description="Reference energy for each state")
    corrEnergy: list[float] = Field(description="MP2 correlation energy for each state")


class Energy(BaseModel):

    AutoCI:     AutoCI_Energy
    CAS_DCD:    CAS_DCD_Energy
    CAS_MSPT2:  CAS_MSPT2_Energy
    CAS_PT2:    CAS_PT2_Energy
    CAS_SCF:    CAS_SCF_Energy
    CIS:        CIS_Energy
    MDCI:       MDCI_Energy
    MP2:        MP2_Energy
    SCF:        Energy_Base
