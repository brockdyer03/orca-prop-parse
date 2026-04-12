import json
from typing import Annotated

from pydantic import BaseModel, Field


class SpinSpinCoupling(BaseModel):

    numOfNucPairs:      int = Field(description="Number of nuclei pairs to calculate")
    numOfNucPairsDSO:   int = Field(description="number of nuclear pairs to calculate DSO")
    numOfNucPairsPSO:   int = Field(description="number of nuclear pairs to calculate PSO")
    numOfNucPairsFC:    int = Field(description="number of nuclear pairs to calculate FC")
    numOfNucPairsSD:    int = Field(description="number of nuclear pairs to calculate SD")
    numOfNucPairsSD_FC: int = Field(description="number of nuclear pairs to calculate SD/FC")
    pairsInfo:          list[int] = Field(description="Pairs Info: Col1->Index of A. Col2->Atom. Num. of A.  Col3->Index of B. Col4->Atom. Num. of B.")
    pairsDistances:     list[float] = Field(description="The distances of each pair")
    pairsTotalSSCIso:   list[float] = Field(description="The Spin-Spin coupling constant for each pair")
    Method:             str
    Level:              str
    Mult:               int
    State:              int
    Irrep:              int


class ChemicalShift(BaseModel):

    numOfNucs:   int
    Method:      str
    Level:       str
    Mult:        int
    State:       int
    Irrep:       int
    NUC:         list[int] = Field(description="Index of the nuclei")
    Elems:       list[int] = Field(description="Atomic number of the nuclei")
    SDSO:        list[list[float]] = Field(description="Diamagnetic contribution")
    SPSO:        list[list[float]] = Field(description="Paramagnetic contribution")
    STot:        list[list[float]] = Field(description="Total tensor")
    orientation: list[list[float]] = Field(description="Eigenvectors")
    sTotEigen:   list[list[float]] = Field(description="Eigenvalues")
    siso:        list[float]
    saniso:      list[float]


class EFGTensor(BaseModel):

    numOfNucs:    int = Field(description="Number of active nuclei")
    Method:       str
    Level:        str
    Mult:         int
    State:        int
    Irrep:        int
    NUC:          list[int] = Field(description="Index of the nuclei")
    Elems:        list[int] = Field(description="Atomic number of the nuclei")
    Isotope:      list[float] = Field(description="Atomic mass")
    I:            list[float] = Field(description="Spin of the nuclei")
    QFAC:         list[float] = Field(description="Prefactor")
    V:            list[list[float]] = Field(description="Raw tensor")
    VEigenvalues: list[list[float]] = Field(description="Eigenvalues")
    orientation:  list[list[float]] = Field(description="Eigenvectors")
    VIso:         list[float]


class ATensor(BaseModel):

    numOfNucs:    int = Field(description="Number of active nuclei")
    Method:       str
    Level:        str
    Mult:         int
    State:        int
    Irrep:        int
    NUC:          list[int] = Field(description="Index of the nuclei")
    Elem:         list[int] = Field(description="Atomic number of the nuclei")
    Isotope:      list[float] = Field(description="Atomic mass")
    I:            list[float] = Field(description="Spin of the nuclei")
    PFAC:         list[float] = Field(description="Prefactor PFAC=gegNbe*bN (in MHz)")
    ARaw:         list[list[float]] = Field(description="Raw tensor")
    AEigenvalues: list[list[float]] = Field(description="Eigenvalues")
    orientation:  list[list[float]] = Field(description="Eigenvectors")
    AIso:         list[float]


class DTensor(BaseModel):

    d_raw:          list[float]
    d_eigenvalues:  list[float]
    d_eigenvectors: list[float]
    D:              float
    E:              float
    Method:         str
    Level:          str
    Mult:           int
    State:          int
    Irrep:          int


class GTensor(BaseModel):

    g_matrix:    list[float]
    g_elec:      float = Field(description="The free electron g-value contribution")
    g_RMC:       float = Field(description="The reduced mass correction")
    g_DSO:       list[float]
    g_PSO:       list[float]
    g_Tot:       list[float]
    g_iso:       float
    Delta_g:     list[float]
    Delta_g_iso: float
    orientation: list[float]
    Method:      str
    Level:       str
    Mult:        int
    State:       int
    Irrep:       int


class Polarizability(BaseModel):

    isotropicPolar:     float
    rawCartesian:       list[float]
    diagonalizedTensor: list[float]
    orientation:        list[float]
    doAtomicPolar:      bool
    atomicPolarIso:     list[float] | None = Field(description="Atomic istotropic polarizabilities")
    Method:             str
    Level:              str
    Mult:               int
    State:              int
    Irrep:              int


class QuadrupoleMoment(BaseModel):

    isotropicQuadMoment: float
    quadElecContrib:     list[float] = Field(description="Electronic contribution.  Order: XX, YY, ZZ, XY, XZ, YZ")
    quadNucContrib:      list[float] = Field(description="Nuclear contribution.  Order: XX, YY, ZZ, XY, XZ, YZ")
    quadTotal:           list[float] = Field(description="Total.  Order: XX, YY, ZZ, XY, XZ, YZ")
    quadDiagonalized:    list[float] = Field(description="The diagonalized tensor")
    doAtomicQuad:        bool
    atomicQuad:          list[float] | None = Field(description="Atomic quadrupoles (NAtoms * XX, YY, ZZ, XY, XZ, YZ)")
    Method:              str
    Level:               str
    Mult:                int
    State:               int
    Irrep:               int


class DipoleMoment(BaseModel):

    dipoleMagnitude:   float
    dipoleElecContrib: list[float] = Field(description="Electronic contribution")
    dipoleNucContrib:  list[float] = Field(description="Nuclear contribution")
    dipoleTotal:       list[float] = Field(description="Total")
    doAtomicDipole:    bool
    atomicDipole:      list[float] | None = Field(description="Atomic dipoles (NAtoms * X,Y,Z)")
    Method:            str
    Level:             str
    Mult:              int
    State:             int
    Irrep:             int


class Hyperpolarizability(BaseModel):

    rawCartesian: list[float]
    Method:       str
    Level:        str
    Mult:         int
    State:        int
    Irrep:        int


class gCPEnergy(BaseModel):

    gCP_Energy: float


class VdWCorrection(BaseModel):

    vdW:        float
    vdW_atomic: list[float] | None


class ThermochemistryEnergies(BaseModel):

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


class SOCEnergyCorrection(BaseModel):

    total_SOC_energy:     float
    total_non_SOC_energy: float
    nuclear_energy:       float
    SOC_correction:       float


class DBOCEnergy(BaseModel):

    DBOC_Energy: float


class Hessian(BaseModel):

    HESSIAN: list[float] = Field(description="The Hessian")
    MODES:   list[float] = Field(description="The modes of vibrations")


class AbsorptionSpectrum(BaseModel):

    Method:             int
    RelCorrection:      int = Field(description="Type of relativistic treatment in QDPT. 0->Unknow, 1->None, 2->SOC, 3->SSC, 4->SOC/SSC")
    DensType:           int = Field(description="Type of density (electron/spin …). 0->Unknow, 1->Electronic, 2->Spin, 3->Trans/Electronic, 4->Tran/Spin")
    DeriType:           int = Field(description="Type of derivative (w.r.t. to what perturbation). 0->Unknown, 1->No Derivative, 2->Electric/Dipole, 3->Electric/Quad, 4->Magnetic/Dipole, 5->Magnetic/Quad")
    DensLevel:          int = Field(description="// Source of density: relaxed, unrelaxed, … 0->Unknown, 1->Linearized, 2->Unrelaxed, 3->Relaxed")
    Density_name:       str
    Representation:     str = Field(description="Possible values: Unknown,  Length, Velocity")
    PointGroup:         str
    DoHigherMoments:    bool
    NTrans:             int
    ExcitationEnergies: list[float]
    States:             list[int] = Field(description="The initial and Final states. Col1: Initial State  Col2: Initial Irrep Col3: Final State Col4: Final Irrep")
    Multiplicities:     list[float] = Field(description="Col1: Multiplicity of the initial state  Col2: Multiplicity of the final state")
    Temperature:        float


class ECDSpectrum(BaseModel):

    Method:             int
    RelCorrection:      int = Field(description="Type of relativistic treatment in QDPT. 0->Unknow, 1->None, 2->SOC, 3->SSC, 4->SOC/SSC")
    DensType:           int = Field(description="Type of density (electron/spin …). 0->Unknow, 1->Electronic, 2->Spin, 3->Trans/Electronic, 4->Tran/Spin")
    DeriType:           int = Field(description="Type of derivative (w.r.t. to what perturbation). 0->Unknown, 1->No Derivative, 2->Electric/Dipole, 3->Electric/Quad, 4->Magnetic/Dipole, 5->Magnetic/Quad")
    DensLevel:          int = Field(description="// Source of density: relaxed, unrelaxed, … 0->Unknown, 1->Linearized, 2->Unrelaxed, 3->Relaxed")
    Density_name:       str
    Representation:     str = Field(description="Possible values: Unknown,  Length, Velocity")
    PointGroup:         str
    DoHigherMoments:    bool
    NTrans:             int
    ExcitationEnergies: list[float]
    States:             list[int] = Field(description="The initial and Final states. Col1: Initial State  Col2: Initial Irrep Col3: Final State Col4: Final Irrep")
    Multiplicities:     list[float] = Field(description="Col1: Multiplicity of the initial state  Col2: Multiplicity of the final state")
    Temperature:        float


class STEOM(BaseModel):

    S2:                        list[float] = Field(description="<S**2>")
    PercentageActiveCharacter: list[float]
    Method:                    str
    excitationEnergies:        list[float] = Field(description="Total energy of each state")
    Mult:                      list[int] | None = Field(description="Multiplicity of each state")
    Irrep:                     list[int] | None = Field(description="Irreducible representation of each state")
    RelCorr:                   str | None = Field(description="Relativistic correction (SOC and/or SSC)")
    NBlocks:                   int | None = Field(description="Number of multiplicity blocks")
    NRoots:                    list[int] | None = Field(description="Number of roots in each block")
    NTotalRoots:               int | None = Field(description="Total number of roots")
    Block:                     list[int] | None = Field(description="Block index of each state")
    Root:                      list[int] | None = Field(description="Root index within the block")
    FollowIRoot:               int | None = Field(description="Index of the followed root")
    AvgMult:                   list[float] | None = Field(description="Average multiplicity of each SO-/SS-coupled state")


class ROCISEnergies(BaseModel):

    refEnergy:      float
    corrEnergy:     float
    totalEnergy:    float
    numOfRoots:     int
    Energies:       list[float] = Field(description="State energies in Hartree")
    Multiplicities: list[int]


class MDCIEOMEnergies(BaseModel):

    groundRefEnergy:   float = Field(description="Ground State Reference Energy")
    groundCorrEnergy:  float = Field(description="Ground State Correlation Energy")
    groundTotalEnergy: float = Field(description="Ground State Total MDCI Energy")


class ExcitedStatesDynamics(BaseModel):

    fluorRateConstant: float


class MDCILED(BaseModel):

    numOfFragments:  int = Field(description="The number of fragments")
    sumNonDisStrong: float = Field(description="Sum of non dispersive correlation strong pairs")
    sumNonDisWeak:   float = Field(description="Sum of non dispersive correlation weak pairs")
    electrostRef:    list[float] = Field(description="Electrostatics reference")
    exchangeRef:     list[float] = Field(description="Exchange reference")
    dispContr:       list[float] = Field(description="Strong pair dispersion contribution")
    dispWeak:        list[float] = Field(description="Weak pair dispersion contribution")
    refInt:          list[float] = Field(description="Interaction reference")
    corrInt:         list[float] = Field(description="Interaction correlation")
    totInt:          list[float] = Field(description="Interaction total")


class BROKENSYMMETRY(BaseModel):

    enHighSpin:  float = Field(description="The High Spin Energy")
    enBrokenSym: float = Field(description="The Broken Symmetry Energy")
    SHighSpin:   float = Field(description="The High Spin Spin")
    S2HighSpin:  float = Field(description="The Expectation value of S**2 for the High Spin case")
    S2BrokenSym: float = Field(description="The Expectation value of S**2 for the Broken symmetry case")


class NaturalOrbitals(BaseModel):

    NEL:       int
    NSOMO:     int
    NDOMO:     int
    NVMO:      int
    NNatoOrbs: int
    OccUno:    list[float] = Field(description="Occupation  of natural orbitals")
    OccUnso:   list[float] = Field(description="Occupation of spin natural orbitals")


class SolvationDetails(BaseModel):

    Solvent:        str
    Epsilon:        float
    Refrac:         float
    RSolv:          float
    SurfaceType:    str
    CPCMDielEnergy: float
    NPoints:        int
    SurfaceArea:    float


class Geometry(BaseModel):

    NAtoms:       int
    NCorelessECP: int
    NGhostAtoms:  int
    Coordinates:  list[str, float, float, float]
    ATNO:         list[int]
    coreless_ECP: list[int] | None = Field(description="Non-zero for cECPs")
    ghostAtoms:   list[int] | None = Field(description="Non-zero for ghost atoms")
    fragments:    list[int] | None = Field(description="Fragment ID")


class NuclearGradient(BaseModel):

    NAtoms:   int
    gradNorm: float
    grad:     list[float]
    Method:   str
    Level:    str
    Mult:     int
    State:    int
    Irrep:    int


class EnergyExtrapolation(BaseModel):

    doEp1:           bool = Field(description="Extrapolation using only one method")
    doEp2:           bool = Field(description="Extrapolation using two different methods (same small basis Set)")
    doEp3:           bool = Field(description="Extrapolation using two different methods (use three basis Sets for the cheap method)")
    doGradients:     bool = Field(description="Extrapolate energy gradients")
    scfEnergies:     list[float]
    scfCBS:          float
    scfGradients:    list[float] | None = Field(description="The SCF Gradients")
    corrEnergies:    list[float]
    corrCBS:         float
    ccsdtEnergyX:    float | None
    totalCBS:        float
    cardinalNumbers: list[int]
    alphas:          list[float]
    betas:           list[float]
    numOfEnergies:   int = Field(description="How many energies we are going to use (e.g. two-point scheme).")
    basisName:       list[str]


class CIPSIEnergies(BaseModel):

    finalEnergy:  float
    numOfRoots:   int
    multiplicity: int
    energies:     list[float]


class DFTEnergy(BaseModel):

    nAlphaEl:  int
    nBetaEl:   int
    nTotalEl:  int
    finalEn:   float = Field(description="No Van der Waals correction")
    eExchange: float
    eCorr:     float
    eXC:       float
    eCNL:      float
    eEmbed:    float | None


class Energy(BaseModel):

    Method:      str
    totalEnergy: list[float] = Field(description="Total energy of each state")
    Mult:        list[int] | None = Field(description="Multiplicity of each state")
    Irrep:       list[int] | None = Field(description="Irreducible representation of each state")
    RelCorr:     str | None = Field(description="Relativistic correction (SOC and/or SSC)")
    NBlocks:     int | None = Field(description="Number of multiplicity blocks")
    NRoots:      list[int] | None = Field(description="Number of roots in each block")
    NTotalRoots: int | None = Field(description="Total number of roots")
    Block:       list[int] | None = Field(description="Block index of each state")
    Root:        list[int] | None = Field(description="Root index within the block")
    FollowIRoot: int | None = Field(description="Index of the followed root")
    AvgMult:     list[float] | None = Field(description="Average multiplicity of each SO-/SS-coupled state")


class CHELPGPopulationAnalysis(BaseModel):

    NAtoms:        int
    ATNO:          list[int]
    AtomicCharges: list[float]
    Method:        str
    Level:         str
    Mult:          int
    State:         int
    Irrep:         int


class HirshfeldPopulationAnalysis(BaseModel):

    NAtoms:        int
    ATNO:          list[int]
    DENSA:         float = Field(description="Total integrated alpha density")
    DENSB:         float = Field(description="Total integrated beta density")
    AtomicCharges: list[float]
    Spin:          list[float]
    Method:        str
    Level:         str
    Mult:          int
    State:         int
    Irrep:         int


class LoewdinPopulationAnalysis(BaseModel):

    NAtoms:        int
    ATNO:          list[int]
    AtomicCharges: list[float]
    Method:        str
    Level:         str
    Mult:          int
    State:         int
    Irrep:         int


class MayerPopulationAnalysis(BaseModel):

    NAtoms:           int = Field(description="Total number of atoms")
    NBondOrdersPrint: int = Field(description="The number of bond orders larger than threshold")
    bondThresh:       float = Field(description="The threshold for printing")
    components:       list[int] | None = Field(description="The indices and atomic numbers of the bonding atoms")
    BondOrders:       list[float] | None = Field(description="The bond orders")
    ATNO:             list[int] = Field(description="Atomic number of the elements")
    NA:               list[float] = Field(description="Mulliken gross atomic population")
    ZA:               list[float] = Field(description="Total nuclear charge")
    QA:               list[float] = Field(description="Mulliken gross atomic charge")
    VA:               list[float] = Field(description="Mayer’s total valence")
    BVA:              list[float] = Field(description="Mayer’s bonded valence")
    FA:               list[float] = Field(description="Mayer’s free valence")
    Method:           str
    Level:            str
    Mult:             int
    State:            int
    Irrep:            int


class MBISPopulationAnalysis(BaseModel):

    NAtoms:            int
    ATNO:              list[int]
    Thresh:            float
    Niter:             int
    LargePrint:        bool
    DENSA:             float = Field(description="Total integrated alpha density")
    DENSB:             float = Field(description="Total integrated beta density")
    AtomicCharges:     list[float]
    Spin:              list[float]
    NPOPVAL:           list[float]
    SIGMAVAL:          list[float]
    AtomicDipole:      list[float] | None
    AtomicQuadrupole:  list[float] | None
    AtomicOctupole:    list[float] | None
    ThirdRadialMoment: list[float] | None
    Method:            str
    Level:             str
    Mult:              int
    State:             int
    Irrep:             int


class MullikenPopulationAnalysis(BaseModel):

    NAtoms:        int
    ATNO:          list[int]
    AtomicCharges: list[float]
    Method:        str
    Level:         str
    Mult:          int
    State:         int
    Irrep:         int


class SinglePointData(BaseModel):

    FinalEnergy: float = Field(description="Final single point energy")
    Converged:   bool


class SCFTimings(BaseModel):

    TOTAL:         float | None
    PREP:          float | None
    GUESS:         float | None
    FOCK:          float | None
    DENS:          float | None
    DIAG:          float | None
    ETOT:          float | None
    POP:           float | None
    TRAFO:         float | None
    ORTHO:         float | None
    DIIS:          float | None
    SOSCF:         float | None
    NR:            float | None
    J:             float | None
    X:             float | None
    XC:            float | None
    GRID:          float | None
    FSYMMETR:      float | None
    PSYMMETR:      float | None
    FOCKSTART:     float | None
    SOLV:          float | None
    SOLV_INIT:     float | None
    SOLV_FINAL:    float | None
    INT_PREP:      float | None
    INT_PRESCREEN: float | None
    INT_BF:        float | None
    INT_DENS:      float | None
    INT_DENSIO:    float | None
    INT_FUNC:      float | None
    INT_POT:       float | None
    INT_POTIO:     float | None
    INT_SUM:       float | None
    SPLITRIJ:      float | None
    COSX:          float | None
    COSX1C:        float | None
    RIJK:          float | None
    STABANA:       float | None
    DFET:          float | None
    ADFT_GUESS:    float | None
    ADFT_JDENS:    float | None
    ADFT_JMAT:     float | None
    ADFT_XDENS:    float | None
    ADFT_XMAT:     float | None
    ADFT_TMAT:     float | None
    ADFT_EQNSOLV:  float | None
    ECRISM:        float | None
    ECRISM_QESP:   float | None
    ECRISM_TOOL:   float | None
    ECRISM_FOCK:   float | None
    FROZCORE:      float | None


class CalculationInfo(BaseModel):

    Mult:                  int
    Charge:                int
    NumOfAtoms:            int
    NumOfElectrons:        int
    NumOfBasisFuncts:      int
    NumOfAuxCBasisFuncts:  int
    NumOfAuxJBasisFuncts:  int
    NumOfAuxJKBasisFuncts: int
    NumOfCABSBasisFuncts:  int


class CalculationStatus(BaseModel):

    version:  str
    progName: str
    Status:   str


class CalculationTimings(BaseModel):

    GTOINT:     float | None
    STOINT:     float | None
    SCF:        float | None
    SCFGRAD:    float | None
    GSTEP:      float | None
    PLOT:       float | None
    MOM:        float | None
    MP2:        float | None
    CPSCF:      float | None
    LOC:        float | None
    CIS:        float | None
    MRCI:       float | None
    REL:        float | None
    SOC:        float | None
    EPRNMR:     float | None
    CASSCF:     float | None
    MDCI:       float | None
    CHELPG:     float | None
    ROCIS:      float | None
    MRCC:       float | None
    FCI:        float | None
    MD:         float | None
    FREQ:       float | None
    FREQ_NUM:   float | None
    COMPOUND:   float | None
    CIPSI:      float | None
    AUTOCI:     float | None
    ESD:        float | None
    DLPNOCC:    float | None
    MCRPA:      float | None
    NEB:        float | None
    CONFSC:     float | None
    ANMR:       float | None
    MM:         float | None
    MMGRAD:     float | None
    XTB:        float | None
    XTBGRAD:    float | None
    LFT:        float | None
    EXT:        float | None
    ONIOM_S:    float | None
    ONIOM_M:    float | None
    ONIOM_L:    float | None
    PROPINT:    float | None
    RESPONSE:   float | None
    PROP:       float | None
    CASRESP:    float | None
    MP2RESP:    float | None
    COSMORS:    float | None
    AUTOCIRESP: float | None
    GOAT:       float | None
    CISRESP:    float | None
    EDA:        float | None
    SUM:        float | None